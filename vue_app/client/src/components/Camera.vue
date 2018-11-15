<template>
  <div class="video-player">
    <div class="video-container">
      <video ref="videoRef" src="" id="video-container" width="100%" controls></video>
      <!-- <video width="720" height="540" controls>
      <source src="this.activeVideo.videoSource" type="video/mp4">
      </video> -->
      <h3>{{this.activeVideo.title}}</h3>
    </div>
    <div class="video-list">
    <div @click="chooseVideo(video)" :key="video.id" v-for="video in videos" class="thumbnail">
        <div class="thumbnail-img">
          <img :src="video.thumbnail" />
        </div>
    </div>
</div>
  </div>
</template>

<script>
let videos = [
  {
    id: 1,
    title: "MP4 Test",
    thumbnail: "https://assets.pernod-ricard.com/uk/media_images/test.jpg",
    videoSource: "https://www.youtube.com/embed/KB4_WIPE7vo",
  },
  {
    id: 2,
    title: "ToyStory MP4",
    thumbnail: "https://assets.pernod-ricard.com/uk/media_images/test.jpg",
    videoSource: "../assets/toystory.mp4",
  }
  ];


export default {
  name: 'VideoPlayer',
  data () {
    return {
      videos,
      activeVideo: videos[0]
    }
  },
  methods:{
    chooseVideo(video){
      //SET VIDEO AS ACTIVE VIDEO
      this.activeVideo = video;
    },
  },
  
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