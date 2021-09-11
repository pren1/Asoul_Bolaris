<template>
  <div class="card">
    <h2 class="title">{{ title }}</h2>
    <v-chart class="chart" :option="option" theme="light"/>
  </div>
</template>

<script>
import mixin from '../mixin'

import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent
]);

export default {
  mixins: [mixin],
  name: "HelloWorld",
  components: {
    VChart
  },
  provide: {
    [THEME_KEY]: "dark"
  },
  data: () => ({
    title: 'HelloWorld',
    option: {},
    money_pie: [],
    type_pie: []
  }),
  created() {
    // this.update_chart()
    this.url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_pie_picture.json`
  },
  watch: {
    data(value) {
      this.money_pie = value.money_pie
      this.type_pie = value.type_pie
      console.log(this.money_pie[0][0])
      console.log(this.type_pie)
      this.update_chart()
    },
  },
  methods: {
    update_chart() {
      this.title = "New title"
      this.option = {
        tooltip: {
          trigger: "item",
          formatter(data) {
            console.log(data.data.name)
            return data.data.name.split(":")[1]
          }
        },
        series: [
          {
            name: "Traffic Sources",
            type: "pie",
            radius: "55%",
            center: ["50%", "50%"],
            data: [
              { value: Math.round(this.money_pie[0][1]), name: this.money_pie[0][0] },
              { value: Math.round(this.money_pie[1][1]), name: this.money_pie[1][0] },
              { value: Math.round(this.money_pie[2][1]), name: this.money_pie[2][0] }
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      }
    }
  }

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