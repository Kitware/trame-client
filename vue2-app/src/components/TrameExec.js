export default {
  name: 'TrameExec',
  props: ['event'],
  methods: {
    exec(arg) {
      if (arg === undefined) {
        this.$emit('exec', this.event);
      } else {
        this.$emit('exec', arg);
      }
    },
  },
};
