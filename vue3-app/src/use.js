import components from "./components";

export default {
  install(app) {
    Object.keys(components).forEach((name) => {
      app.component(name, components[name]);
    });
  },
};
