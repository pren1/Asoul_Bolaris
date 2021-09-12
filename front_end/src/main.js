// import '@babel/polyfill'
// import 'mutationobserver-shim'
import Vue from 'vue'
// import './plugins/bootstrap-vue'
import App from './App.vue'
import ECharts from 'vue-echarts'
import './index.scss'
import axios from 'axios'
// import * as echarts from 'echarts'
import router from './router'

// require('echarts-wordcloud')
// Vue.prototype.$echarts = echarts;
Vue.component('chart', ECharts)
Vue.config.productionTip = false
Vue.prototype.$axios = axios
// axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*'

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
