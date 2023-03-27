import wslink from './wslink';
import { TrameState } from './trame/state';
import { decorate, setAddAttachment } from './trame/decorators';
import vtkURLExtract from '@kitware/vtk.js/Common/Core/URLExtract';

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
    await this.connect();
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
      let templateName = 'trame__template_main';
      if (this.useUrl && vtkURLExtract.extractURLParameters().ui) {
        templateName = `trame__template_${vtkURLExtract.extractURLParameters().ui}`;
      }
      if (this?.client?.getConfig()?.reconnect) {
        this.state.set(templateName, `<trame-reconnect message="${message}"/>`);
      } else {
        this.state.set(templateName, `<trame-loading message="${message}"/>`);
      }
    },
    async connect() {
      if (this.connected) {
        return;
      }

      if (this.client) {
        this.previousConfig = this.client.getConfig();
        while (this.subscriptions.length) {
          this.subscriptions.pop().unsubscribe();
        }
        if (this.state) {
          this.state.delete();
          this.state = null;
        }
        wslink.resetClient(this.name);
      }

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
            type: 'Connection closed',
            message: httpReq?.response?.error,
          };
          this.reportError(httpReq?.response?.error || 'Connection closed');
          this.$emit('statusChange', this.status);
        })
      );

      // Connect if new client
      if (this.client.isConnected()) {
        this.status = wslink.getStatus(this.name);
        this.$emit('statusChange', this.status);
      } else {
        const config =
          this.previousConfig ||
          wslink.configDecorator({
            ...this.config,
            useUrl: this.useUrl,
          });
        await this.client.connect(config);
        this.lastConfig = this.client.getConfig();
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
    async trigger(name, args = [], kwargs = {}) {
      let decoratedArgs = [];
      const decoratedKwargs = {};

      if (args) {
        const decorateArgs = args.map((arg) => decorate(arg));
        decoratedArgs = await Promise.all(decorateArgs);
      }

      if (kwargs) {
        const keys = [];
        const values = [];
        Object.entries(kwargs).forEach((entry) => {
          keys.push(entry[0]);
          values.push(decorate(entry[1]));
        });

        const resolvedValues = await Promise.all(values);
        for (let i = 0; i < keys.length; i++) {
          decoratedKwargs[keys[i]] = resolvedValues[i];
        }
      }

      return await this.client.getRemote().Trame.trigger(name, decoratedArgs, decoratedKwargs);
    },
  },
  provide() {
    return { trame: this };
  },
};
