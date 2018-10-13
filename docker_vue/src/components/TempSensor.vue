<template>
  <ul id="Temps">
  <li v-for="temp in tempData">
    {{ temp }}
  </li>
</ul>
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
      const path = 'http://localhost:5000/temp/all';
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
