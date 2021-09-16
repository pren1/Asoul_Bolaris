<template>
  <div class="card">
    <h2 class="title">{{ title }}</h2>
    <v-chart class="chart" :option="option" autoresize :theme="input_theme"/>
  </div>
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { BarChart } from "echarts/charts";
import {
  // TitleComponent,
  GridComponent,
  TooltipComponent,
  ToolboxComponent,
} from "echarts/components";
import VChart from "vue-echarts";

use([
  CanvasRenderer,
  BarChart,
  // TitleComponent,
  GridComponent,
  TooltipComponent,
  ToolboxComponent
]);

export default {
  props: ['input_data', 'input_theme', 'input_title', 'input_x_label', 'input_y_label', 'input_color'],
  name: "bar_chart",
  components: {
    VChart
  },
  data: () => ({
    title: '加载中...',
    option: {},
    x_data: [],
    y_data: []
  }),
  watch: {
    input_data(value) {
      // console.log(this.sort_dict(value))
      let sorted_value = this.sort_dict(value)
      // for (const [key, dict_val] of Object.entries(this.sort_dict(value))) {
      //   this.x_data.push(key)
      //   this.y_data.push(dict_val)
      // }
      for (let i = 0; i < sorted_value.length; i++) {
        this.x_data.push(sorted_value[i][0])
        this.y_data.push(sorted_value[i][1])
      }
      this.update_chart()
    }
  },
  // created() {
  //   this.update_chart()
  // },
  methods: {
    sort_dict(dict){
      // Create items array
      var items = Object.keys(dict).map(function(key) {
        return [key, dict[key]];
      });

      // Sort the array based on the second element
      items.sort(function(first, second) {
        return second[1] - first[1];
      });
      return items
    },
    update_chart() {
      this.title = this.input_title
      // console.log("xdata: " + this.x_data)
      // console.log("ydata: " + this.y_data)
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
                  magicType: {type: ['line', 'bar'],
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
            type: 'category',
            // splitLine:{
            //   show:false
            // },
            axisLabel: {
              interval: 0,
              rotate: 30 //If the label names are too long you can manage this by rotating the label.
            },
            data: this.x_data,
            // name: this.input_x_label,
            // nameLocation: 'middle',
            // nameGap: 30
          },
          yAxis: {
             type: 'value',
             axisLine:{
              show:false
             },
              name: this.input_y_label,
              // nameLocation: 'middle',
              // nameGap: 40
          },
          tooltip: {
              trigger: 'axis',
              axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                  type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
              }
          },
         // tooltip: {
         //    trigger: 'axis',
         //    axisPointer: {
         //        type: 'cross',
         //        // label: {
         //        //     backgroundColor: '#6a7985'
         //        // }
         //    },
         //    formatter(data) {
         //      if (data){
         //        // console.log(data[0].data)
         //        // var colorSpan = color => '<span style="display:inline-block;margin-right:5px;border-radius:10px;width:9px;height:9px;background-color:' + color + '"></span>';
         //        return '时间：' + data[0].data[0] + '<br>' + '数值：' + data[0].data[1] + '</br>'
         //      }
         //      return null
         //    }
         //  },
        series: [{
          data: this.y_data,
          type: 'bar',
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