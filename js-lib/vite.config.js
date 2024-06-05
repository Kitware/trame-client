export default {
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "trame",
      formats: ["es", "umd"],
      fileName: "trame",
    },
    assetsDir: ".",
  },
};
