export default {
  name: 'Reconnect',
  props: {
    message: {
      type: String,
      default: 'Click to reconnect...',
    },
    maxRetry: {
      type: Number,
      default: 10,
    },
    delay: {
      type: Number,
      default: 500,
    },
  },
  methods: {
    async reconnect() {
      await this.trame.connect();
    },
    resetRetry() {
      if (this.interval) {
        clearInterval(this.interval);
        this.interval = null;
      }
    },
  },
  mounted() {
    this.retryCount = 0;
    const reconnect = this.trame?.client?.getConfig()?.reconnect;
    if (reconnect) {
      console.log('reconnect', reconnect);
      if (reconnect === 'auto') {
        this.interval = setInterval(() => {
          if (this.retryCount++ < this.maxRetry) {
            this.reconnect();
          } else {
            this.resetRetry();
          }
        }, this.delay);
      }
    }
  },
  beforeDestroy() {
    this.resetRetry();
  },
  inject: ['trame'],
};
