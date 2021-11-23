let localConfig

try {
  localConfig = require('./local.config')
} catch (e) {
  localConfig = null
}

const publicPath = process.env.NODE_ENV === 'production' ? '/static' : '/'

const defaultapi = 'http://127.0.0.1:8000/'
const api = localConfig ? localConfig.api : defaultapi

module.exports = {
  publicPath: publicPath,
  outputDir: '../dist/',
  productionSourceMap: false,
  css: {
    loaderOptions: {
      less: {
        modifyVars: {
          'primary-color': '#993030',
          'link-color': '#ca9999',
          'border-radius-base': '3px',
          'border-radius-sm': '3px',
          'table-padding-vertical': '4px',
          'table-padding-horizontal': '8px',
        },
        javascriptEnabled: true,
      },
    },
  },
  devServer: {
    compress: true,
    disableHostCheck: true,
    proxy: {
      '/api': {
        target: api,
      },
    },
  },
}
