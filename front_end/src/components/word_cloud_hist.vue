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
  TitleComponent,
  GridComponent,
  TooltipComponent,
  ToolboxComponent,
} from "echarts/components";
import VChart from "vue-echarts";

use([
  CanvasRenderer,
  BarChart,
  TitleComponent,
  GridComponent,
  TooltipComponent,
  ToolboxComponent
]);

export default {
  props: ['input_data', 'input_theme', 'input_title', 'input_x_label', 'input_y_label'],
  name: "bar_chart",
  components: {
    VChart
  },
  data: () => ({
    title: 'HelloWorld',
    option: {},
    x_data: [],
    y_data: []
  }),
  watch: {
    input_data(value) {
      // console.log(value)
      for (const [key, dict_val] of Object.entries(value)) {
        this.x_data.push(key)
        this.y_data.push(dict_val)
      }
      this.update_chart()
    }
  },
  // created() {
  //   this.update_chart()
  // },
  methods: {
    update_chart() {
      this.title = this.input_title
      console.log("xdata: " + this.x_data)
      console.log("ydata: " + this.y_data)
      this.option = {
          toolbox: {
              show: true,
              right: '10%',
              top: '4%',
              feature: {
                  dataZoom: {
                      yAxisIndex: 'none'
                  },
                  dataView: {readOnly: false},
                  saveAsImage: {}
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
            data: this.x_data,
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
              nameLocation: 'middle',
              nameGap: 40
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
          type: 'bar'
        }]
      }
    }
  }
}
</script>

<style scoped>
.chart {
  height: 400px;
  padding-left: 1rem;
}
</style>