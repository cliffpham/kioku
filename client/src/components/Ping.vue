<template>
  <div>
    <p>{{ msg }}</p>
    <input v-model="test" placeholder="edit me">
    <p>Message is: {{ test }}</p>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
      found_words: {},
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          if (this.msg.valid) {
            this.found_words[this.msg.word] = 1;
          }
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
