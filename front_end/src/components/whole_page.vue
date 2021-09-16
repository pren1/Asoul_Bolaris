<template>
  <div class="container background_img" id="myPElement">
    <BarChart :input_data="input_wordCloud_bar_data" :input_theme="custheme"
               input_title="词频统计" input_x_label="词语" input_y_label="词语数目" :input_color="this.target_color"
                />
    <div class="card">
      <h2 class="title" style="background-color: white; color: black">词云</h2>
      <img width="50%" :src="image_url" alt="Image">
    </div>
    <div class="container_2">
      <MoneyPie :input_data="input_money_pie_data" :input_theme = "custheme" input_title = "营收构成图（金额）"/>
      <MoneyPie :input_data="input_type_pie_data" :input_theme = "custheme" input_title="营收构成图（类型）"/>
    </div>
    <div class="container_2">
      <LineChart :input_data="input_danmu_line_data" :input_theme="custheme"
               input_title="弹幕数量" input_x_label="开播时长/1mins——时间区段：1mins  "
               input_y_label="弹幕数量" calculate_total="计算总和" time_scale="1" :input_color="this.target_color"/>
      <LineChart :input_data="input_entry_line_data" :input_theme="custheme"
                 input_title="入场人次" input_x_label="开播时长/1mins——时间区段：1mins  "
                 input_y_label="入场人次" calculate_total="计算总和" time_scale="1" :input_color="this.target_color"/>
      <LineChart :input_data="input_gift_line_data" :input_theme="custheme"
                 input_title="送礼人次" input_x_label="开播时长/1mins——时间区段：1mins  "
                 input_y_label="送礼人次" calculate_total="计算总和" time_scale="1" :input_color="this.target_color"/>
    </div>
    <div class="container_2">
      <LineChart :input_data="input_guard_data_line_data" :input_theme="custheme"
                 input_title="舰团数量" input_x_label="开播时长/1mins——时间区段：3mins  "
                 input_y_label="舰团数量" calculate_total="计算总和" time_scale="3" :input_color="this.target_color"/>
      <LineChart :input_data="input_new_fans_data_line_data" :input_theme="custheme"
                 input_title="新增粉丝" input_x_label="开播时长/1mins——时间区段：3mins  "
                 input_y_label="新增粉丝" calculate_total="计算总和" time_scale="3" :input_color="this.target_color"/>
      <LineChart :input_data="input_new_medal_fans_data_line_data" :input_theme="custheme"
                 input_title="新增粉丝团" input_x_label="开播时长/1mins——时间区段：3mins  "
                 input_y_label="新增粉丝团" calculate_total="计算总和" time_scale="3" :input_color="this.target_color"/>
    </div>
    <div class="container_2">
      <LineChart :input_data="input_revenue_data_line_data" :input_theme="custheme"
                 input_title="营收" input_x_label="开播时长/1mins——时间区段：1mins  "
                 input_y_label="营收" calculate_total="计算总和" time_scale="1" :input_color="this.target_color"/>
      <LineChart :input_data="input_sc_data_line_data" :input_theme="custheme"
                 input_title="sc数量" input_x_label="开播时长/1mins——时间区段：3mins  "
                 input_y_label="sc数量" calculate_total="计算总和" time_scale="3" :input_color="this.target_color"/>
      <LineChart :input_data="input_simu_interact_line_data" :input_theme="custheme"
                 input_title="10分钟同接" input_x_label="开播时长/1mins——时间区段：1mins  "
                 input_y_label="10分钟同接" calculate_total="" time_scale="1" :input_color="this.target_color"/>
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
    input_wordCloud_image_data: [],
    target_color: ""
  }),
  created() {
    // console.log("live info" + this.$route.params.live_info)
    let info = this.$route.params.live_info.split("&")
    let target_link = info[0] + '_' + info[1]

    this.pie_url = `https://asoulmonitor.xyz/api/data/${target_link}_dm_pie_picture.json`
    this.stats_url = `https://asoulmonitor.xyz/api/data/${target_link}_dm_stats_picture.json`
    this.wordCloud_url = `https://asoulmonitor.xyz/api/data/${target_link}_dm_word_cloud.json`
    this.image_url = `https://asoulmonitor.xyz/api/data/${target_link}_dm_word_cloud.webp`

    // let test = "https://asoulmonitor.xyz/api/data/" + target_link + "_dm_word_cloud.png"
    // console.log(test)
    let user_id = info[1]

    let color_selector = {
    "22625025": "#9AC8E2",
    "22632424": "#DB7D74",
    "22634198": "#B8A6D9",
    "22637261": "#E799B0",
    "22625027": "#576690",
    "22632157":  "#000000"
    }
    // document.querySelector('body').style.setProperty('example', test);
    this.target_color = color_selector[user_id];
    document.querySelector('body').style.setProperty('--main-color', this.target_color);

    let title_selector = {
    "22625025": "向晚大魔王",
    "22632424": "贝拉kira",
    "22634198": "珈乐Carol",
    "22637261": "嘉然今天吃什么",
    "22625027": "乃琳Queen",
    "22632157":  "A-SOUL_Official"
    }
    document.title = title_selector[user_id]

    let header_selector = {
        "22625025": "AvA",
        "22632424": "Bira",
        "22634198": "Carlo",
        "22637261": "diana",
        "22625027": "Queen",
        "22632157": "asoul"
      }
    let icon_path =  `https://asoulmonitor.xyz/api/data/avatar/${header_selector[user_id]}.webp`
    document.querySelector("[rel='icon']").setAttribute('href', icon_path);
  },
  mounted() {
    this.$router.onReady(() => this.routeLoaded());
    console.log("mounted called")
    window.addEventListener('load', () => {
        // run after everything is in-place
        console.log("width" + screen.width)
        if (screen.width > 700){
          document.getElementById('myPElement').style.maxWidth = screen.width + 'px';
        }
        document.getElementById('myPElement').style.backgroundImage = 'url(' + this.image_url + ')';
    })
  },
  watch: {
    $route() {
            this.$nextTick(this.routeLoaded);
    },
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
  methods: {
    routeLoaded() {
          //Dom for the current route is loaded
          console.log("Router loaded!")
          console.log("width: " + screen.width)
          if (screen.width > 700){
              document.getElementById('myPElement').style.maxWidth = screen.width + 'px';
            }
            document.getElementById('myPElement').style.backgroundImage = 'url(' + this.image_url + ')';
        }
  }
}
</script>

<style lang="scss" scoped>
//$background_image_url: var(example);
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
}
.background_img{
  /*background-color: black;*/
   //background-image: url("https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_word_cloud.png");
   //background-repeat: no-repeat;
   //background-position: center center; /* Center the image */
   //background-size: 270%;
   background-color: $background_color;
   //background-attachment: scroll;
   position: relative;
   height: 1000%;
   width: 270%;
   //max-height: 300%;
   //max-width: 1792px;
   background-position: center 30%;
   background-repeat: no-repeat;
   background-size: 270%, cover;
   background-attachment: local, fixed;
  //overflow: hidden;
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