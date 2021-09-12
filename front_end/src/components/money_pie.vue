<template>
  <div class="card">
    <h2 class="title">{{ title }}</h2>
    <v-chart ref="pie" class="chart" :option="option" autoresize :theme="input_theme"/>
  </div>
</template>

<script>

import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  // TitleComponent,
  TooltipComponent,
  ToolboxComponent
  // LegendComponent
} from "echarts/components";
import VChart from "vue-echarts";

use([
  CanvasRenderer,
  PieChart,
  // TitleComponent,
  TooltipComponent,
  ToolboxComponent
  // LegendComponent
]);
let dataIndex = -1;
let new_dataIndex = -1; // record the new position
let delay_time = 1000; // specific delay
export default {
  props: ['input_data', 'input_theme', 'input_title'],
  name: "HelloWorld",
  components: {
    VChart
  },
  data: () => ({
    title: 'HelloWorld',
    option: {},
    money_pie: [],
    // type_pie: [],
    stopped: false,
    timeout: null,
  }),
  watch: {
    input_data(value) {
      // console.log(logs)
      this.money_pie = value
      console.log(this.money_pie[0][0])
      // console.log(this.type_pie)
      this.update_chart()
    }
  },
  methods: {
    update_chart() {
      this.title = this.input_title
      this.option = {
        backgroundColor: 'white',
        toolbox: {
              show: true,
              right: '10%',
              top: '4%',
              feature: {
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
          trigger: "item",
          formatter(data) {
            if (data.dataIndex !== dataIndex){
              new_dataIndex = data.dataIndex; // record the mouse position
              delay_time = 2000; // if the mouse put in the pie chart, change delay here
            }
            // console.log(data.data.name)
            return data.data.name
          }
        },
        series:
            [
          {
            name: "Traffic Sources",
            type: "pie",
            radius: ['40%', '70%'],
            center: ["50%", "50%"],
            itemStyle: {
                borderRadius: 10,
                borderColor: '#fff',
                borderWidth: 2
            },
            data: [
              { value: Math.round(this.money_pie[0][1]), name: this.money_pie[0][0] },
              { value: Math.round(this.money_pie[1][1]), name: this.money_pie[1][0] },
              { value: Math.round(this.money_pie[2][1]), name: this.money_pie[2][0] }
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
    // this.highlight()
  },
  beforeDestroy() {
    this.stopped = true;
    clearTimeout(this.timeout)
  },
};
</script>

<style scoped>
.chart {
  height: 400px;
}
</style>