const path = require('path');

module.exports = {
  // productionSourceMap: false,
  runtimeCompiler: true,
  outputDir: path.resolve(__dirname, '../trame_client/module/www'),
  publicPath: './',
};
