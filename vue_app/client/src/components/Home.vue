<template>
  <div class="homepage-container">
    <div class="header">
      <div class="home-button">
        <router-link to="/home" tag="button" class="btn btn-danger">Homepage</router-link>
      </div>
      <router-link to="/door/front" tag="button" class="btn btn-outline-warning"
        >Front Door</router-link>
      <router-link to="/temp/all" tag="button" class="btn btn-outline-warning"
        >Temp Sensor</router-link>
      <div class="github-button">
        <a href="https://github.com/Project-semyonov/adam" tag="button"
        class="btn btn-outline-success">Github Repo</a>
      </div>
      <h1>Home</h1>
    </div>
      <p> Project Semyonov is in your house! </p>
  </div>
</template>

