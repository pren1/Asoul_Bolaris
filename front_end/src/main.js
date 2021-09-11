// import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
// import './plugins/bootstrap-vue'
import App from './App.vue'
import ECharts from 'vue-echarts'
import './index.scss'
import axios from 'axios'

Vue.component('chart', ECharts)
Vue.config.productionTip = false
Vue.prototype.$axios = axios
// axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*'

new Vue({
  render: h => h(App),
}).$mount('#app')
