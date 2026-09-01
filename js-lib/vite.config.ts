import { defineConfig } from "vite";
import dts from "vite-plugin-dts";

export default defineConfig({
  base: "./",
  plugins: [dts({ insertTypesEntry: true })],
  build: {
    lib: {
      entry: "./src/main.ts",
      name: "Trame",
      formats: ["es", "umd"],
      fileName: "trame",
    },
    assetsDir: ".",
  },
});
