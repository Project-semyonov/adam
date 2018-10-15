<template>
  <div class="temp-container">
    <link href="https://afeld.github.io/emoji-css/emoji.css" rel="stylesheet">
    <div class="header">
      <router-link to="/temp/all" tag="button" class="btn btn-danger btn-sm">Temp</router-link>
      <router-link to="/home" tag="button" class="btn btn-warning btn-sm">Homepage</router-link>
      <a href="https://github.com/Project-semyonov/adam" tag="button"
        class="btn btn-success btn-sm">Github Repo</a>
      <h1>Temp</h1>
    </div>
    <div class="temp-alert">
      <button type="button" class="btn btn-success btn-sm"
        v-on:click="getTemps">Update Temp </button>
      <alert :message=message v-if="showMessage"></alert>
    </div>
    <div class="temp-table">
      <div class="col-lg-4">
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Time</th>
              <th scope="col">Temp</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="temp in tempData" :key="temp">
              <td>{{ temp }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      tempData: '',
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getTemps() {
      const path = 'http://localhost:5000/temp/all';
      // eslint-disable-next-line
      const updateTime = require('time-stamp');
      const currentTime = updateTime('HH:mm:ss');
      this.showMessage = true;
      axios.get(path)
        .then((res) => {
          this.tempData = res.data;
          // eslint-disable-next-line
          this.message = 'Got temps from the sensor at ' + currentTime + '! 🤘 ';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.message = 'Failed to get temps from the sensor 🚨';
        });
    },
  },
  created() {
    this.getTemps();
  },

};

</script>

