<template>
  <div class="content-box">
    <!-- vue的ref可以通过this.$refs.获取到DOM节点 -->
    <!-- echart容器div必须设置高度，否则不显示 -->
    <div ref="keyWords" style="height:300px;"></div>
  </div>
</template>
<script>
export default {
  props: ['input_data'],
  data: () => ({
    title: 'HelloWorld',
    input_wordCloud_data: []
  }),
  watch: {
    input_data(value) {
      console.log(this.sort_dict(value))
      let sorted_value = this.sort_dict(value)
      // for (const [key, dict_val] of Object.entries(this.sort_dict(value))) {
      //   this.x_data.push(key)
      //   this.y_data.push(dict_val)
      // }
      for (let i = 0; i < sorted_value.length; i++) {
        this.input_wordCloud_data.push(
            {
              'name': sorted_value[i][0],
              'value': sorted_value[i][1]
            }
        )
      }
      console.log(this.input_wordCloud_data)
      // this.update_chart()
      this.initEchart();
    }
  },
  // mounted() {
  //   this.$nextTick(() => {
  //     this.initEchart();
  //   });
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
    initEchart() {
      //获取DOM节点并初始化
      let myChart = this.$echarts.init(this.$refs.keyWords);
      let option = {
        tooltip: {
          show: true
        },
        series: [
          {
            name: "",
            type: "wordCloud",
            size: ["95%", "95%"],
            textRotation: [0, 45, 90, -45],
            textPadding: 0,
            autoSize: {
              enable: true,
              minSize: 14
            },
            textStyle: {
              normal: {
                color: function() {
                  return (
                    "rgb(" +
                    Math.round(Math.random() * 255) +
                    ", " +
                    Math.round(Math.random() * 255) +
                    ", " +
                    Math.round(Math.random() * 255) +
                    ")"
                  );
                }
              }
            },
            data: this.input_wordCloud_data
          }
        ]
      };

      //设置图表的参数
      myChart.setOption(option);
    }
  }
};
</script>