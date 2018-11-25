<template>
<div id="title">
  <h1>Welcome to my video library!</h1>
    Scroll through the videos below and click the one you want to play.
  </div>
  <div id="thumbnail-container">
  </div>
  <div id="player-container">
  <video id="player">
  </video>
  <div id="controls">
  </div>
  </div>
</template>

<script>
var videoFiles = ["1.mp4", "2.mp4", "3.mp4", "4.mp4", "5.mp4"];
var player;
var playerSource = document.createElement("source");
document.addEventListener("DOMContentLoaded",function() { initialise(); }, false);

function generateThumbnail(video) {
  var canvas = document.createElement("canvas");
  var container = document.getElementById("thumbnail-container");
  var width = container.clientWidth;
  var height = container.clientHeight;
  canvas.width = (width / 3);
  canvas.height = height;
  canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
  var image = document.createElement("img");
  image.src = canvas.toDataURL();
  return image; }

function initialise() {
  player = document.getElementById("player");
  player.appendChild(playerSource);
  player.controls = false;
  videoFiles.forEach(function(file) {
  var thumbSource = document.createElement("source");
  thumbSource.src = file;
  var thumbVideo = document.createElement("video");
  thumbVideo.addEventListener("loadeddata", function() {
  var container = document.getElementById("thumbnail-container")
  var image = generateThumbnail(thumbVideo);
  container.appendChild(image);
  }, false);
  thumbVideo.appendChild(thumbSource);
  }); }

thumbVideo.addEventListener("loadeddata", function() {
  var container = document.getElementById("thumbnail-container")
  var image = generateThumbnail(thumbVideo);
  var link = document.createElement("a");
  link.href = "javascript:play(\"" + thumbSource.src + "\")";
  link.appendChild(image);
  container.appendChild(link);
  }, 
false);

function play(url) 
{
  playerSource.src = url;
  player.controls = true;
  player.load();
  player.play(); 
}

export default {
}
</script>



<style>
body {
  background-color: #cccccc;
  font-family: sans-serif;
}
#player-container {
  margin-left: auto;
  margin-right: auto;
  width: 640px;
  height: 480px;
  background-color: #538c99;
  border-radius: 20px;
}
#title {
  margin-left: auto;
  margin-right: auto;
  width: 640px;
  text-align: center;
  padding-top: 30px;
  padding-bottom: 50px;
  background-color: #538c99;
  color: #333333;
  border-radius: 20px; }

#thumbnail-container {
  background-color: #cccccc;
  margin-top: 30px;
  margin-left: auto;
  margin-right: auto;
  width: 640px;
  height: 120px;
  overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
  border-radius: 20px; }

video {
  width: 100%;
  height: 100%; }
</style>