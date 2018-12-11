<template>
  <div class="video-player">
    <div class="video-container">
      <video id="myVideo" controls autoplay>
      <source id="mp4_src" src=this.activeVideo.videoSource type="video/mp4">
      Your browser does not support HTML5 video.
      </video>
      <h3>{{this.activeVideo.title}}</h3>
    </div>
    <div class="video-list">
      <div @click="chooseVideo(video)" :key="video.id" v-for="video in videos">
          <button type="button" class="btn btn-info btn-sm">Video: {{video.id}}</button>
      </div>
    </div>
  </div>
</template>

<script>
let videos = [
  {
    id: 1,
    videoSource: require('../assets/video1.mp4')
  }
  // {
  //   id: 2,
  //   videoSource: require('../assets/toystory.mp4')
  // },
  // {
  //   id: 3,
  //   videoSource: require('../assets/toystory.mp4')
  // },
  // {
  //   id: 4,
  //   videoSource: require('../assets/toystory.mp4')
  // },
  // {
  //   id: 5,
  //   videoSource: require('../assets/toystory.mp4')
  // }
]

export default {
  name: 'VideoPlayer',
  data () {
    return {
      videos,
      activeVideo: videos[0]
    }
  },
  methods: {
    chooseVideo (video) {
      // SET VIDEO AS ACTIVE VIDEO
      this.activeVideo = video
      console.log(this.activeVideo.videoSource)
      document.getElementById('mp4_src').setAttribute('src', video.videoSource)
      document.getElementById('myVideo').load()
    }
  }

}
</script>

<style scoped>
  .thumbnail{
    display:flex;
  }
  .thumbnail img{
    width:168px;
}

.thumbnail-info{
    margin-left:20px;
}

.thumbnail h3{
    font-size:16px;
}

h3,
p{
    margin:0;
    padding:0;
}
.thumbnail-views{
    font-size:14px;
}
.video-player{
    display:flex;
    width:1200px;
    margin:auto;
}
.video-container{
    margin-right:40px;
}
</style>
