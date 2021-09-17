<template>
  <div class="card2">
    <h2 class="title">{{ title }}</h2>
    <v-chart class="chart" :option="option" autoresize :theme="input_theme"/>
  </div>
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { LineChart } from "echarts/charts";
import {
  // TitleComponent,
  GridComponent,
  TooltipComponent,
  ToolboxComponent,
  DataZoomComponent,
  LegendComponent
} from "echarts/components";
import VChart from "vue-echarts";

use([
  CanvasRenderer,
  LineChart,
  // TitleComponent,
  GridComponent,
  TooltipComponent,
  ToolboxComponent,
  DataZoomComponent,
  LegendComponent
]);

export default {
  props: ['input_data', 'input_theme', 'input_title', 'input_x_label', 'input_y_label', 'calculate_total', 'time_scale', 'input_color', 'my_show_chart'],
  name: "line_chart",
  components: {
    VChart
  },
  data: () => ({
    title: '加载中...',
    option: {},
    line_data: {},
    data_array_1d: []
  }),
  watch: {
    input_data(value) {
      // console.log(value)
      this.line_data = value
      // this.data_array_1d = value
      // console.log(this.line_data[0])
      this.update_chart()
    },
    my_show_chart(value){
      // console.log("triggered! " + value)
      if (value === true){
        // console.log("Update charts!")
        this.update_chart()
      } else {
        console.log("Hide!")
      }
    }
  },
  // created() {
  //   this.update_chart()
  // },
  methods: {
    update_chart() {
      this.title = this.input_title
      this.option = {
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        xAxis: {
        type: 'category',
        boundaryGap: false,
        data: this.line_data.date_list
    },
    yAxis: {
        type: 'value'
    },
    grid: {
      left: '3%',
      bottom: '14%',
      containLabel: true
    },
    dataZoom: [
        {
            type: 'slider',
            show: true,
            xAxisIndex: [0],
            bottom: '6%',
            start: 70,
            end: 100
        },
        {
            type: 'slider',
            show: true,
            yAxisIndex: [0],
            left: '93%',
            start: 0,
            end: 100
        },
    ],
    legend: {
        textStyle: {
          fontSize: 10
        },
        top: '2%',
        data: ['弹幕数量', '入场人次', '送礼人次', '舰团数量', '新增粉丝', '新增粉丝团', '营收', 'sc数量']
    },
    toolbox: {
        show: false,
        right: '3%',
        top: '1.5%',
        feature: {
            dataZoom: {
                yAxisIndex: 'none',
                iconStyle: {
                  borderColor: '#e01f54'
                },
                emphasis: {
                    iconStyle: {
                        borderColor: '#e01f54'
                    },
                }
            },
            dataView: {
              readOnly: false,
              iconStyle: {
                    borderColor: '#a092f1'
                },
                emphasis: {
                    iconStyle: {
                        borderColor: '#a092f1'
                    },
                }
              },
            saveAsImage: {
              iconStyle: {
                  borderColor: '#001852'
              },
              emphasis: {
                  iconStyle: {
                      borderColor: '#001852'
                  },
              }
            }
        }
    },
    tooltip: {
        trigger: 'axis'
    },
    series: [
        {
          name: '弹幕数量',
          data: this.line_data.danmu,
          type: 'line',
          smooth: true,
        },
        {
          name: '入场人次',
          data: this.line_data.entry,
          type: 'line',
          smooth: true,
        },
        {
          smooth: true,
          name: '送礼人次',
          data: this.line_data.gift,
          type: 'line'
        },
        {
          smooth: true,
          name: '舰团数量',
          data: this.line_data.guard_data,
          type: 'line'
        },
        {
          smooth: true,
          name: '新增粉丝',
          data: this.line_data.new_fans_data,
          type: 'line'
        },
        {
          smooth: true,
          name: '新增粉丝团',
          data: this.line_data.new_medal_fans_data,
          type: 'line'
        },
        {
          smooth: true,
          name: '营收',
          data: this.line_data.revenue,
          type: 'line'
        },{
          smooth: true,
          name: 'sc数量',
          data: this.line_data.sc_data,
          type: 'line'
        }
        ]
      }
    }
  }
}
</script>

<style scoped>
.chart {
  height: 85%;
  width: 90%;
  max-width: 90%;
  /*padding-left: 1rem;*/
}
</style>