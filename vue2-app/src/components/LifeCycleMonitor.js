const { onMounted, onUpdated, onUnmounted, onBeforeMount, onBeforeUpdate, onBeforeUnmount } =
  window.Vue;

function runNow(fn) {
  fn();
}

const NAME_TO_LIFE_CYCLE = {
  created: runNow,
  beforeMount: onBeforeMount,
  mounted: onMounted,
  beforeUpdate: onBeforeUpdate,
  updated: onUpdated,
  beforeDestroy: onBeforeUnmount,
  destroyed: onUnmounted,
};

export default {
  props: {
    name: {
      type: String,
      default: 'LifeCycleMonitor',
    },
    type: {
      type: String,
      default: 'log',
    },
    value: {
      type: String,
      default: 'value',
    },
    events: {
      type: Array,
      default: () => [
        'created',
        'beforeMount',
        'mounted',
        'beforeUpdate',
        'updated',
        'beforeDestroy',
        'destroyed',
      ],
    },
  },
  emits: Object.keys(NAME_TO_LIFE_CYCLE),
  setup(props, { emit }) {
    for (let i = 0; i < props.events.length; i++) {
      const name = props.events[i];
      const fn = NAME_TO_LIFE_CYCLE[name];
      fn(() => {
        if (props.type === 'emit') {
          emit(name, { name: props.name, value: props.value });
        } else {
          console[props.type](props.name, name, props.value);
        }
      });
    }
  },
};
