<template>
  <div class="card">
    <h2 class="title">{{ title }}</h2>
    <v-chart ref="pie" class="chart" :option="option" autoresize theme="light"/>
  </div>
</template>

<script>
import mixin from '../mixin.js'
// import logs from '../test.js'

import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  // LegendComponent
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  // LegendComponent
]);
let dataIndex = -1;
let new_dataIndex = -1; // record the new position
let delay_time = 1000; // specific delay
export default {
  mixins: [mixin],
  name: "Type_pie",
  components: {
    VChart
  },
  provide: {
    [THEME_KEY]: "dark"
  },
  data: () => ({
    title: 'Type_pie',
    option: {},
    money_pie: [],
    type_pie: [],
    stopped: false,
    timeout: null
  }),
  created() {
    // this.update_chart()
    this.url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_pie_picture.json`
  },
  watch: {
    data(value) {
      // console.log(logs)
      // this.money_pie = value.money_pie
      this.type_pie = value.type_pie
      // console.log(this.money_pie[0][0])
      console.log(this.type_pie)
      this.update_chart()
    },
  },
  methods: {
    update_chart() {
      this.title = "礼物营收统计"
      this.option = {
        tooltip: {
          trigger: "item",
          formatter(data) {
            if (data.dataIndex !== dataIndex){
              new_dataIndex = data.dataIndex; // record the mouse position
              delay_time = 2000; // if the mouse put in the pie chart, change delay here
            }
            // console.log(data.data.name)
            return "礼物营收统计：" + data.data.name
          }
        },
        series:
            [
          {
            name: "Traffic Sources",
            type: "pie",
            radius: "55%",
            center: ["50%", "50%"],
            data: [
              { value: Math.round(this.type_pie[0][1]), name: this.type_pie[0][0] },
              { value: Math.round(this.type_pie[1][1]), name: this.type_pie[1][0] },
              { value: Math.round(this.type_pie[2][1]), name: this.type_pie[2][0] }
            ],
            minShowLabelAngle: 3,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
        // [
        //   {
        //     name: "Traffic Sources",
        //     type: "pie",
        //     radius: "55%",
        //     center: ["50%", "50%"],
        //     data: [
        //       { value: 335, name: "Direct" },
        //       { value: 310, name: "Email" },
        //       { value: 234, name: "Ad Networks" },
        //       { value: 135, name: "Video Ads" },
        //       { value: 1548, name: "Search Engines" }
        //     ],
        //     emphasis: {
        //       itemStyle: {
        //         shadowBlur: 10,
        //         shadowOffsetX: 0,
        //         shadowColor: "rgba(0, 0, 0, 0.5)"
        //       }
        //     }
        //   }
        // ]
      }
    },
    highlight() {
      try {
        const pie = this.$refs.pie;
        // console.log(this.option.series[0].data)
        if (typeof this.option.series != "undefined") {
          const dataLen = this.option.series[0].data.length;
          pie.dispatchAction({
            type: 'downplay',
            seriesIndex: 0,
            dataIndex
          });
          if (delay_time===1000){ // If the delay is sometime else, do not highlight current dataIndex
            dataIndex = (dataIndex + 1) % dataLen;
            pie.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex
            });
            // 显示 tooltip
            pie.dispatchAction({
              type: 'showTip',
              seriesIndex: 0,
              dataIndex,
              position: 'inside'
            });
          }
        }
        if (this.stopped) return;
        this.timeout = setTimeout(this.highlight, delay_time);
          if(delay_time !== 1000){ // Only when the delay time is not 1000, renew the dataIndex, begin at the new data Index
            dataIndex = new_dataIndex;
            delay_time = 1000; // recover the delay_time
          }
        }
        catch (error) {
          console.error(error);
          if (this.stopped) return;
          this.timeout = setTimeout(this.highlight, delay_time);
          if(delay_time !== 1000){
              dataIndex = new_dataIndex;
              delay_time = 1000;
            }
      }
    }
  },
  mounted () {
     this.highlight()
  },
  beforeDestroy() {
    this.stopped = true;
    clearTimeout(this.timeout)
  },

  // data() {
  //   return {
  //     option: {
  //       // title: {
  //       //   text: "Traffic Sources",
  //       //   left: "center"
  //       // },
  //       tooltip: {
  //         trigger: "item",
  //         formatter: "{a} <br/>{b} : {c} ({d}%)"
  //       },
  //       series: [
  //         {
  //           name: "Traffic Sources",
  //           type: "pie",
  //           radius: "55%",
  //           center: ["50%", "50%"],
  //           data: [
  //             { value: 335, name: "Direct" },
  //             { value: 310, name: "Email" },
  //             { value: 234, name: "Ad Networks" },
  //             { value: 135, name: "Video Ads" },
  //             { value: 1548, name: "Search Engines" }
  //           ],
  //           emphasis: {
  //             itemStyle: {
  //               shadowBlur: 10,
  //               shadowOffsetX: 0,
  //               shadowColor: "rgba(0, 0, 0, 0.5)"
  //             }
  //           }
  //         }
  //       ]
  //     }
  //   };
  // }
};
</script>

<style scoped>
.chart {
  height: 400px;
}
</style>