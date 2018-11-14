<template>
  <div id="playlist">
    <div id="secborder" ref="playlist" @click="changeSource">
    <div class="video" url-value="https://media.w3.org/2010/05/sintel/trailer.mp4">Sintel &nbsp;∘&nbsp; Trailer</div>
    <div class="video" url-value="https://player.vimeo.com/external/219608960.hd.mp4?s=5956858697e5a70c422499a327862c75aeba037a&profile_id=119">Laravel &nbsp;∘&nbsp; Tutorial</div>
    </div>
  </div>
</template>

<script>

import { bus } from '../main';

export default {

  name: 'playlist',

  props : {
 
 currentVideo: {
  type : String
 }

  },

  data () {
    return {

    }
  },
  
  methods: {
    changeSource : function(e) {
      let videoValue = e.target.attributes[1].value;
      this.$emit('updateData', videoValue);
      bus.$emit('reload');
    }

  }
}

</script>

<style scoped>

#secborder {
    border: 10px solid white;
    border-radius: 15px;
    margin: 2rem 0.5rem;
    background: black;
    height: 35rem;
    width: 40%;
    float: right;
}

.video {
    width: 100%;
    height: 10%;
    padding: 0.5em;
    border-bottom: 0.5px solid #172951;
    font-size: 1.5rem;
    font-weight: bold;
    text-align: center;
    color: white;
    cursor: pointer;
}

</style>
