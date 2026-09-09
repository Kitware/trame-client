import { fileURLToPath, URL } from "node:url";
import react from "@vitejs/plugin-react";

// Shared with vue3-app rather than duplicated: it has no Vue-specific code
// (plain download/get/safe/tree helpers), so react-app reads it straight out
// of the sibling package instead of maintaining its own copy.
const vue3Utils = fileURLToPath(
  new URL("../vue3-app/src/utils", import.meta.url),
);

export default {
  base: "./",
  plugins: [react()],
  resolve: {
    alias: {
      "@vue3-utils": vue3Utils,
    },
  },
  server: {
    // vue3Utils lives outside react-app's own root, which Vite's dev server
    // otherwise refuses to serve (fs.allow defaults to this package only).
    fs: {
      allow: [fileURLToPath(new URL(".", import.meta.url)), vue3Utils],
    },
  },
  build: {
    outDir: "../src/trame_client/module/react-www",
  },
};
