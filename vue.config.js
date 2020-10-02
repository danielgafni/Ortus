// const IS_PRODUCTION = process.env.NODE_ENV === 'production'
// let VUE_APP_BASE = process.env.VUE_APP_BASE
// let APP_API_PORT = process.env.APP_API_PORT
// let VUE_APP_API_ENDPOINT = VUE_APP_BASE.concat(":", APP_API_PORT)

// import axios from 'axios'
// axios.defaults.baseURL = VUE_APP_API_ENDPOINT.concat('/api')

module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  // publicPath: process.env.VUE_APP_BASE_URL.concat(":", process.env.VUE_APP_UI_PORT),
  devServer: {
    proxy: {
      '/api*': {
        // Forward frontend dev server request for /api to Flask server
        // target: VUE_APP_API_ENDPOINT
        target: "http://0.0.0.0:5000"
      }
    },
    port: "8080",
    disableHostCheck: true
  }
}
