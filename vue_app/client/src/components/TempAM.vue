<template>
  <div class="house-temp-container">
    <div class="row">
      <div class="col-lg-4">
        <h1>House Temps</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Time</th>
              <th scope="col">Temp</th>
              <th></th>
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

export default {
  data() {
    return {
      tempData: '',
    };
  },
  methods: {
    getTemps() {
      const path = 'http://localhost:5000/temp/am';
      axios.get(path)
        .then((res) => {
          this.tempData = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getTemps();
  },

};

</script>
