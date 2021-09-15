<template>
  <div  class="background_img">
    <div id="navbar" class="sticky">
      <a>A-soul 直播数据统计（来源：A-soul 数据组)</a>
    </div>
    <div id="rating" class="content">
      <div class="item" v-for="info_str in global_list.slice(0, list_length)" :key="info_str">
        <router-link class="avatar" :to="'/' + info_str">
          <img width="128" height="128" :src="provide_correct_url(info_str)" alt="头像"/>
        </router-link>
        <div class="detail">
            <div v-if="info_str.split('&')[1] === '22625025'">
              <p class="title" style="color: #9AC8E2">
                {{provide_live_name(info_str)}}
              </p>
            </div>
            <div v-else-if="info_str.split('&')[1] === '22632424'">
              <p class="title" style="color: #DB7D74">
                {{provide_live_name(info_str)}}
              </p>
            </div>
            <div v-else-if="info_str.split('&')[1] === '22634198'">
              <p class="title" style="color: #B8A6D9">
                {{provide_live_name(info_str)}}
              </p>
            </div>
            <div v-else-if="info_str.split('&')[1] === '22637261'">
              <p class="title" style="color: #E799B0">
                {{provide_live_name(info_str)}}
              </p>
            </div>
            <div v-else-if="info_str.split('&')[1] === '22625027'">
              <p class="title" style="color: #576690">
                {{provide_live_name(info_str)}}
              </p>
            </div>
            <div v-else-if="info_str.split('&')[1] === '22632157'">
                <p class="title" style="color: #000000">
                  {{provide_live_name(info_str)}}
                </p>
            </div>
  <!--          <p class="value">同传总字数：</p>-->
            <p class="desc">
              {{provide_live_date(info_str)}}
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
    this.global_list_url = `https://asoulmonitor.xyz/api/active/real_live_list.json`
    document.title = 'A-soul 直播数据统计'
    let icon_path =  `https://asoulmonitor.xyz/api/data/avatar/asoul.webp`
    document.querySelector("[rel='icon']").setAttribute('href', icon_path);
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
        // myFunction()
      }
      // // Get the navbar
      // var navbar = document.getElementById("navbar");
      //
      // // Get the offset position of the navbar
      // var sticky = navbar.offsetTop;
      //
      // // Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
      // function myFunction() {
      //   if (window.pageYOffset >= sticky) {
      //     navbar.classList.add("sticky")
      //   } else {
      //     // navbar.classList.remove("sticky");
      //   }
      // }
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
    },
    provide_live_name(info_str){
      return info_str.split('&')[2]
    }
  }
}
</script>

<style scoped lang="scss">
#rating {
  max-width: 500px;
  //width: 50%;
  margin: 0 auto;

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
      padding-left: 9rem;
    }

    .title {
      font-weight: bold;
      font-size: 1.8rem;
      //padding-left: 0.5rem;
    }

    .desc {
      font-size: 1.8rem;
      font-weight: bold;
      padding-left: 1rem;
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
   background-size: cover;
   background-attachment: fixed;
   display: flex;
   justify-content: center;
   align-items: center;
}

/* Style the navbar */
#navbar {
  overflow: hidden;
  background-color: #333;
  z-index: 100;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  box-shadow: 1px 1px 4px #0000;
}

/* Navbar links */
#navbar a {
  //float: start;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px;
  text-decoration: none;
}

///* Page content */
.content {
  padding-top: 50px;
}

/* The sticky class is added to the navbar with JS when it reaches its scroll position */
.sticky {
  position: fixed;
  top: 0;
  width: 100%;
  //min-width: 750px;
}

</style>