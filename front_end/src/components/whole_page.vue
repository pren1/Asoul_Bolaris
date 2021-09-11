<template>
  <div>
    <MoneyPie :input_data="input_money_pie_data" :input_theme = "custheme" input_title = "单次礼物价格统计"/>
    <MoneyPie :input_data="input_type_pie_data" :input_theme = "custheme" input_title="礼物营收总计"/>
  </div>
</template>

<script>
import mixin from '../mixin.js'
// import stat_data from '../stats.js'
// import wordCloud_data from '../wordCloud.js'
import MoneyPie from './money_pie.vue'
// import TypePie from './type_pie.vue'

export default {
  name: "whole_page",
  mixins: [mixin],
  components: {
    MoneyPie,
    // TypePie
  },
  data: () => ({
    custheme: require("../roma.json"),
    input_money_pie_data: [],
    input_type_pie_data: []
  }),
  created() {
    this.pie_url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_pie_picture.json`
    this.stats_url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_stats_picture.json`
    this.wordCloud_url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_word_cloud.json`
  },
  watch: {
    my_pie_data(value) {
      console.log('my_pie_data available!')
      this.input_money_pie_data = value.money_pie
      this.input_type_pie_data = value.type_pie
    },
    // my_stat_data(value) {
    //   console.log('my_stat_data available!' + value)
    // },
    // my_wordCloud_data(value) {
    //   console.log('my_wordCloud_data available!' + value)
    // },
  },
}
</script>

<style scoped>

</style>