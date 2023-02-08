export default {
  props: {
    message: {
      type: String,
      default: "Loading...",
    },
  },
  template: `
        <div style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:1000;">
            <div class="trame__loader"></div>
            <div class="trame__message">{{ message }}</div>
        </div>
    `,
};
