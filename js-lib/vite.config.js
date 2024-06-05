export default {
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "Trame",
      formats: ["es", "umd"],
      fileName: "trame",
    },
    assetsDir: ".",
  },
};
