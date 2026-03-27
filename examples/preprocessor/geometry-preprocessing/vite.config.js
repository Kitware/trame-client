import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    lib: {
      entry: resolve(__dirname, 'lib.js'), 
      name: 'GeometryPreProcessing', 
      formats: ['umd'], 
      fileName: (format) => `geometry-preprocessing.${format}.js` 
    },
  }
});
