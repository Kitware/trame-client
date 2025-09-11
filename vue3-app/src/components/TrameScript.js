const { unref } = window.Vue;
let ID = 1;

function getNextId() {
  return `trame_script_elem_${ID++}`;
}

export default {
  props: {
    script: {
      type: String,
      default: "",
    },
    module: {
      type: Boolean,
      default: false,
    },
  },
  watch: {
    script(scriptContent) {
      this.updateContent(scriptContent);
    },
  },
  created() {
    this.elemId = getNextId();
    this.updateContent(this.script);
  },
  beforeUnmount() {
    this.removeScript();
  },
  methods: {
    updateContent(scriptContent) {
      scriptContent = unref(scriptContent);
      let elem = document.querySelector(`#${this.elemId}`);
      if (scriptContent) {
        if (!elem) {
          elem = document.createElement("script");
          elem.id = this.elemId;
          elem.type = this.module ? "module" : "text/javascript";
          document.head.appendChild(elem);
        }
        elem.innerHTML = scriptContent;
      } else {
        this.removeScript();
      }
    },
    removeScript() {
      const elem = document.querySelector(`#${this.elemId}`);
      if (elem) {
        elem.parentNode.removeChild(elem);
      }
    },
  },
  template: `<slot />`,
};
