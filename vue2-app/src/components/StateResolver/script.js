export function generateData(...keys) {
  const data = {};
  for (let i = 0; i < keys.length; i++) {
    data[keys[i]] = null;
  }
  return data;
}

export function createStateListener(trame, dest, ...keys) {
  return (names) => {
    const { state } = trame;
    const changeNames = new Set(names);
    for (let i = 0; i < keys.length; i++) {
      const name = keys[i];
      if (changeNames.has(name)) {
        dest[name] = state.get(name);
      }
    }
  };
}

export default {
  inject: ['trame'],
  name: 'TrameStateResolver',
  props: {
    names: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return generateData(...this.names);
  },
  computed: {
    state() {
      const filteredState = {
        trame: this.trame,
        set: (...args) => this.trame.state.set(...args),
      };
      for (let i = 0; i < this.names.length; i++) {
        const name = this.names[i];
        filteredState[name] = this[name];
      }
      return filteredState;
    },
  },
  created() {
    this.onStateChange = createStateListener(this.trame, this, ...this.names);
    this.trame.$on('stateChange', this.onStateChange);
    this.onStateChange(this.names);
  },
  beforeDestroy() {
    this.trame.$off('stateChange', this.onStateChange);
  },
  provide() {
    return { state: this };
  },
};
