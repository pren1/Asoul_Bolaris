<template>
  <div  class="background_img">
    <div id="rating">
      <div class="item" v-for="info_str in global_list.slice(0, list_length)" :key="info_str">
        <router-link class="avatar" :to="'/' + info_str">
          <img width="128" height="128" :src="provide_correct_url(info_str)" alt="头像"/>
        </router-link>
        <div class="detail">
            <p class="title">
              {{provide_live_date(info_str)}}
            </p>
  <!--          <p class="value">同传总字数：</p>-->
            <p class="desc">
              一代鬃狮：数据获取错误，你仅仅只得到了一只狮子。
            </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import mixin from '../global_list_mixin.js'
export default {
  name: "homepage",
  mixins: [mixin],
  data: () => ({
    global_list: [],
    list_length: 10
  }),
  watch: {
    my_global_list(value) {
      // console.log(logs)
      this.global_list = value
      console.log(this.global_list[0])
    }
  },
  created() {
    this.global_list_url = `https://asoulmonitor.xyz/api/data/real_live_list.json`
  },
  mounted() {
    this.scroll()
  },
  methods: {
    scroll() {
      let isLoading = false
      window.onscroll = () => {
        // 距离底部200px时加载一次
        let bottomOfWindow = document.documentElement.offsetHeight - document.documentElement.scrollTop - window.innerHeight <= 200
        if (bottomOfWindow && isLoading === false) {
          isLoading = true
          this.list_length += 10
          setTimeout(() => {
              isLoading = false
          }, 500);
          // console.log("hello~")
        }
      }
    },
    provide_correct_url(info_str){
      let header_selector = {
        "22625025": "AvA",
        "22632424": "Bira",
        "22634198": "Carlo",
        "22637261": "diana",
        "22625027": "Queen",
        "22632157": "asoul"
      }
      let room_id = info_str.split('&')[1]
      return `https://asoulmonitor.xyz/api/data/avatar/${header_selector[room_id]}.webp`
    },
    provide_live_date(info_str){
      return '直播日期：' + info_str.split('&')[0]
    }
  }
}
</script>

<style scoped lang="scss">
#rating {
  max-width: 700px;
  margin: 0 auto;
  //margin-top: -1.5rem;

  .item {
    position: relative;
    padding: 1rem;
    border-radius: 10px;
    transition: 0.3s ease;
    box-shadow: 1px 1px 4px #0000;
    background-color: white;
    //margin-top: 1.5rem;

    &:hover {
      box-shadow: 1px 1px 4px #0000005F;
    }
  }

  .avatar {
    left: 1rem;
    height: 128px;
    position: absolute;

    img {
      position: absolute;
      border-radius: 12px;
      box-shadow: 1px 1px 4px #0000005F;
      transition: 0.3s ease;

      &:hover {
        box-shadow: 1px 1px 8px #0000005F;
      }
    }
  }

  .icon {
    right: 1px;
    position: absolute;

    .inner {
        margin: 2px; // Or whatever you want your spacing to be
    }
  }

  .detail {
    text-align: left;
    min-height: 128px;
    padding-left: 9rem;

    @media (min-width: 720px) {
      padding-left: 11rem;
    }

    .title {
      font-weight: bold;
      font-size: 1.5rem;
    }

    p {
      margin: 0.5rem 0;
      line-height: 1.6;

      &:first-child {
        margin-top: 0;
      }

      &:last-child {
        margin-bottom: 0;
      }
    }
  }
}

.background_img{
  /*background-color: black;*/
   background-image: url("https://asoulmonitor.xyz/api/data/background.webp");
   background-repeat: no-repeat;
   background-position: center center; /* Center the image */
   background-size: 105%, contain;
   background-attachment: fixed;
}
</style>