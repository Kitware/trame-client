const path = require('path');

module.exports = {
  chainWebpack: (config) => {
    config.externals({
      vue: 'Vue',
    });
  },
  // productionSourceMap: false,
  runtimeCompiler: true,
  outputDir: path.resolve(__dirname, '../trame_client/module/vue2-www'),
  publicPath: './',
};
