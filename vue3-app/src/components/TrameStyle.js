let ID = 1;

function getNextId() {
  return `trame_style_elem_${ID++}`;
}

export default {
  props: {
    css: {
      type: String,
      default: "",
    },
  },
  watch: {
    css(cssContent) {
      this.updateStyle(cssContent);
    },
  },
  created() {
    this.elemId = getNextId();
    this.updateStyle(this.css);
  },
  beforeUnmount() {
    this.removeStyle();
  },
  methods: {
    updateStyle(cssContent) {
      cssContent = window.Vue.unref(cssContent);
      let elem = document.querySelector(`#${this.elemId}`);
      if (cssContent) {
        if (!elem) {
          elem = document.createElement("style");
          elem.id = this.elemId;
          document.head.appendChild(elem);
        }
        elem.innerHTML = cssContent;
      } else {
        this.removeStyle();
      }
    },
    removeStyle() {
      const elem = document.querySelector(`#${this.elemId}`);
      if (elem) {
        elem.parentNode.removeChild(elem);
      }
    },
  },
  template: `<div class="trame-style" />`,
};
