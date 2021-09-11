<template>
  <div>
    <MoneyPie :input_data="input_money_pie_data" :input_theme = "custheme" input_title = "单次礼物价格统计"/>
    <MoneyPie :input_data="input_type_pie_data" :input_theme = "custheme" input_title="礼物营收总计"/>
    <LineChart :input_data="input_danmu_line_data" :input_theme="custheme"
               input_title="弹幕数量" input_x_label="开播时长/1mins——时间区段：1mins"
               input_y_label="弹幕数量" calculate_total="计算总和" time_scale="1"/>
  </div>
</template>

<script>
import mixin from '../mixin.js'
import MoneyPie from './money_pie.vue'
import LineChart from './line_chart.vue'

export default {
  name: "whole_page",
  mixins: [mixin],
  components: {
    MoneyPie,
    LineChart
  },
  data: () => ({
    custheme: require("../roma.json"),
    input_money_pie_data: [],
    input_type_pie_data: [],
    input_danmu_line_data: [],
    input_entry_line_data: [],
    input_gift_line_data: [],
    input_guard_data_line_data: [],
    input_new_fans_data_line_data: [],
    input_new_medal_fans_data_line_data: [],
    input_revenue_data_line_data: [],
    input_sc_data_line_data: [],
    input_simu_interact_line_data: []
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
    my_stat_data(value) {
      console.log('my_stat_data available!' + value)
      this.input_danmu_line_data = value.danmu
      this.input_entry_line_data = value.entry
      this.input_gift_line_data = value.gift
      this.input_guard_data_line_data = value.guard_data
      this.input_new_fans_data_line_data = value.new_fans_data
      this.input_new_medal_fans_data_line_data = value.new_medal_fans_data
      this.input_revenue_data_line_data = value.revenue
      this.input_sc_data_line_data = value.sc_data
      this.input_simu_interact_line_data = value.simu_interact
    },
    // my_wordCloud_data(value) {
    //   console.log('my_wordCloud_data available!' + value)
    // },
  },
}
</script>

<style scoped>

</style>