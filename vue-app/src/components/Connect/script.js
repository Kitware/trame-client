import wslink from './wslink';
import { TrameState } from './trame/state';
import { setAddAttachment } from './trame/decorators';

export default {
  name: 'TrameConnect',
  props: {
    name: {
      type: String,
      default: 'TrameConnect',
    },
    config: {
      type: Object,
      default: () => ({
        application: 'trame',
      }),
    },
    exclude: {
      type: Array,
      default: () => [],
    },
    useUrl: {
      type: Boolean,
      default: false,
    },
    forwardErrors: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      ready: false,
      connected: false,
      busy: 1,
      status: { type: 'created', message: 'Connecting...' },
    };
  },
  async created() {
    this.subscriptions = [];
    this.client = wslink.getClient(this.name);

    // Monitor busy
    this.subscriptions.push(
      this.client.onBusyChange((count) => {
        const emitBusyChange = !count !== !this.busy;
        this.busy = count;
        if (emitBusyChange && this.state) {
          this.state.set('trame__busy', count);
        }
        if (count === 0) {
          this.state.flush();
        }
        if (emitBusyChange) {
          this.$emit('busyChange', count);
        }
      })
    );

    // Connection Error/Close
    this.subscriptions.push(
      this.client.onConnectionError((httpReq) => {
        this.connected = false;
        this.status = {
          type: 'Connection error',
          message: httpReq?.response?.error,
        };
        this.reportError(httpReq?.response?.error || 'Connection error');
        this.$emit('statusChange', this.status);
      })
    );
    this.subscriptions.push(
      this.client.onConnectionClose((httpReq) => {
        this.connected = false;
        this.status = {
          type: 'Connection close',
          message: httpReq?.response?.error,
        };
        this.reportError(httpReq?.response?.error || 'Connection close');
        this.$emit('statusChange', this.status);
      })
    );

    // Connect if new client
    if (this.client.isConnected()) {
      this.status = wslink.getStatus(this.name);
      this.$emit('statusChange', this.status);
    } else {
      await this.client.connect(
        wslink.configDecorator({
          ...this.config,
          useUrl: this.useUrl,
        })
      );
      setAddAttachment(this.client.getConnection().getSession().addAttachment);
      this.status = { type: 'Connected' };
    }
    this.connected = this.client.isConnected();
    this.busy = this.client.isBusy();
    this.$emit('statusChange', this.status);

    // Fill our trame instance with what make trame magical
    if (this.connected) {
      this.state = new TrameState(this);
    }

    // Attach lifecycles
    this.client.getRemote().Trame.lifeCycleUpdate('client_connected');
    window.addEventListener('beforeunload', () =>
      this.client.getRemote().Trame.lifeCycleUpdate('client_exited')
    );

    // Forward JS errors to Python
    if (this.forwardErrors) {
      const _error = console.error;
      console.error = (...args) => {
        try {
          this.client.getRemote().Trame.sendError(args.join(' '));
        } catch (e) {
          _error(e);
        } finally {
          _error(...args);
        }
      };
      window.addEventListener('error', (event) => {
        console.error(`${event.type}: ${event.message}`);
      });
    }
  },
  beforeDestroy() {
    this.client.getRemote().Trame.lifeCycleUpdate('client_unmounted');
    while (this.subscriptions.length) {
      this.subscriptions.pop().unsubscribe();
    }
    if (this.state) {
      this.state.delete();
      this.state = null;
    }
  },
  methods: {
    reportError(message = 'Something unexpected happened...') {
      this.state.set('trame__template_main', `<trame-loading message="${message}"/>`);
    },
    async trigger(name, args = [], kwargs = {}) {
      return await this.client.getRemote().Trame.trigger(name, args, kwargs);
    },
  },
  provide() {
    return { trame: this };
  },
};
