<template>
  <div class="container">
    <BarChart :input_data="input_wordCloud_bar_data" :input_theme="custheme"
               input_title="词频统计" input_x_label="词语" input_y_label="词语数目"
                />
    <div class="card">
      <h2 class="title">词云</h2>
      <img width="50%" src="https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_word_cloud.png" alt="Image">
    </div>
    <div class="container_2">
      <MoneyPie :input_data="input_money_pie_data" :input_theme = "custheme" input_title = "按金额分"/>
      <MoneyPie :input_data="input_type_pie_data" :input_theme = "custheme" input_title="按类型分"/>
    </div>
    <div class="container_2">
      <LineChart :input_data="input_danmu_line_data" :input_theme="custheme"
               input_title="弹幕数量" input_x_label="开播时长/1mins——时间区段：1mins  "
               input_y_label="弹幕数量" calculate_total="计算总和" time_scale="1"/>
      <LineChart :input_data="input_entry_line_data" :input_theme="custheme"
                 input_title="入场人次" input_x_label="开播时长/1mins——时间区段：1mins  "
                 input_y_label="入场人次" calculate_total="计算总和" time_scale="1"/>
      <LineChart :input_data="input_gift_line_data" :input_theme="custheme"
                 input_title="送礼人次" input_x_label="开播时长/1mins——时间区段：1mins  "
                 input_y_label="送礼人次" calculate_total="计算总和" time_scale="1"/>
      <LineChart :input_data="input_guard_data_line_data" :input_theme="custheme"
                 input_title="舰团数量" input_x_label="开播时长/1mins——时间区段：3mins  "
                 input_y_label="舰团数量" calculate_total="计算总和" time_scale="3"/>
      <LineChart :input_data="input_new_fans_data_line_data" :input_theme="custheme"
                 input_title="新增粉丝" input_x_label="开播时长/1mins——时间区段：3mins  "
                 input_y_label="新增粉丝" calculate_total="计算总和" time_scale="3"/>
      <LineChart :input_data="input_new_medal_fans_data_line_data" :input_theme="custheme"
                 input_title="新增粉丝团" input_x_label="开播时长/1mins——时间区段：3mins  "
                 input_y_label="新增粉丝团" calculate_total="计算总和" time_scale="3"/>
      <LineChart :input_data="input_revenue_data_line_data" :input_theme="custheme"
                 input_title="营收" input_x_label="开播时长/1mins——时间区段：1mins  "
                 input_y_label="营收" calculate_total="计算总和" time_scale="1"/>
      <LineChart :input_data="input_sc_data_line_data" :input_theme="custheme"
                 input_title="sc数量" input_x_label="开播时长/1mins——时间区段：3mins  "
                 input_y_label="sc数量" calculate_total="计算总和" time_scale="3"/>
      <LineChart :input_data="input_simu_interact_line_data" :input_theme="custheme"
                 input_title="10分钟同接" input_x_label="开播时长/1mins——时间区段：1mins  "
                 input_y_label="10分钟同接" calculate_total="" time_scale="1"/>
    </div>
    <div></div>
  </div>
</template>

<script>
import mixin from '../mixin.js'
import MoneyPie from './money_pie.vue'
import LineChart from './line_chart.vue'
import BarChart from './word_cloud_hist.vue'
// import Test from './test.vue'

export default {
  name: "whole_page",
  beforeCreate () {
    document.querySelector('body').setAttribute('style', 'background:#a092f1')
  },
  beforeDestroy () {
    document.querySelector('body').setAttribute('style', '')
  },
  mixins: [mixin],
  components: {
    MoneyPie,
    LineChart,
    BarChart,
    // Test
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
    input_simu_interact_line_data: [],
    input_wordCloud_bar_data: [],
    input_wordCloud_image_data: []
  }),
  created() {
    this.pie_url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_pie_picture.json`
    this.stats_url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_stats_picture.json`
    this.wordCloud_url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_word_cloud.json`

    let color_selector = {
    "22625025": "#9AC8E2",
    "22632424": "#DB7D74",
    "22634198": "#B8A6D9",
    "22637261": "#E799B0",
    "22625027": "#576690",
    "other":  "#000000"
    }

    document.querySelector('body').style.setProperty('--main-color', color_selector["22634198"]);
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
    my_wordCloud_data(value) {
      this.input_wordCloud_bar_data = value.word_freq_bar_dict
      this.input_wordCloud_image_data = value.word_cloud_dict
    },
  },
}
</script>

<style lang="scss" scoped>
$background_color: var(--main-color);
.container {
   /*width: 100%;*/
   padding-top: 3.5rem;
   display: flex;
   flex-direction: column;
   flex-wrap: wrap;
   justify-content: center;
   align-items: center;
   gap: 3.5rem;
   /*background-color: black;*/
   background-image: url("https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_word_cloud.png");
   background-repeat: no-repeat;
   background-position: center center; /* Center the image */
   background-size: 270%;
   background-color: $background_color;
}

.container_2{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 3.5rem;
}
</style>