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
  ToolboxComponent
} from "echarts/components";
import VChart from "vue-echarts";

use([
  CanvasRenderer,
  LineChart,
  // TitleComponent,
  GridComponent,
  TooltipComponent,
  ToolboxComponent
]);

export default {
  props: ['input_data', 'input_theme', 'input_title', 'input_x_label', 'input_y_label', 'calculate_total', 'time_scale', 'input_color'],
  name: "line_chart",
  components: {
    VChart
  },
  data: () => ({
    title: '加载中...',
    option: {},
    line_data: [],
    data_array_1d: []
  }),
  watch: {
    input_data(value) {
      // console.log(logs)
      this.line_data = this.format_data(value)
      this.data_array_1d = value
      // console.log(this.line_data[0])
      this.update_chart()
    }
  },
  // created() {
  //   this.update_chart()
  // },
  methods: {
    format_data(value){
      var result = []
      const start_index = -10
      for (let i = 0; i < value.length; i++){
        result.push([start_index + i * parseInt(this.time_scale), value[i]])
      }
      return result
    },
    update_chart() {
      this.title = this.input_title
      if (this.calculate_total === "计算总和") {
        this.title += "合计：" + Math.round(this.data_array_1d.reduce((x, y) => x + y))
      }
      this.option = {
          backgroundColor: 'rgba(255, 255, 255, 1.0)',
          toolbox: {
              show: true,
              right: '10%',
              top: '4%',
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
          xAxis: {
            // type: 'category',
            // // boundaryGap: false,
            // // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            // data: [0,1 ,2 ,3, 4, 5, 6]
            type: 'value',
            interval:10, // 步长
            min: -5,
            max: this.line_data[this.line_data.length-1][0],
            splitLine:{
              show:false
            },
            name: this.input_x_label,
            nameLocation: 'middle',
            nameGap: 30
          },
          yAxis: {
             type: 'value',
             axisLine:{
              show:false
             },
             name: this.input_y_label,
             // nameLocation: 'middle',
             // nameGap: 50
          },
         tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                // label: {
                //     backgroundColor: '#6a7985'
                // }
            },
            formatter(data) {
              if (data){
                // console.log(data[0].data)
                // var colorSpan = color => '<span style="display:inline-block;margin-right:5px;border-radius:10px;width:9px;height:9px;background-color:' + color + '"></span>';
                return '时间：' + data[0].data[0] + '<br>' + '数值：' + data[0].data[1] + '</br>'
              }
              return null
            }
          },
        series: [{
          data: this.line_data,
          type: 'line',
          smooth: true,
          showSymbol: false,
          itemStyle: {
            color: this.input_color
          },
          areaStyle: {
              color: this.input_color
          }
        }]
      }
    }
  }
}
</script>

<style scoped>
.chart {
  height: 400px;
  /*padding-left: 1rem;*/
}
</style>