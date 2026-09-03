import react from "@vitejs/plugin-react";

export default {
  base: "./",
  plugins: [react()],
  build: {
    outDir: "../src/trame_client/module/react-www",
  },
};
