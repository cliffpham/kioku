<template>
  <div class="container">
    <div class="landing"> 
      <b-container>
        <b-row class="text-center">
          <b-col>
              <h1>ようこそ！</h1>
              <p> Welcome to Kioku - The Japanese vocabulary building game! The rules are simple: With 9 characters try and create as many words as you know but be careful we will only keep track of the last 7 words you made. Repeating a word or entering an invalid word will result in losing a life and you only have 3. So whenever you're ready go ahead and play!</p>
              <b-button v-on:click="handleClick"> Start </b-button>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Start',
  methods: {
    handleClick() {
      this.$emit('startGame');
    },
  },
};
</script>

<style scoped>
html,
body {
  height: 100%;
}

* {
  font-family: 'M PLUS Rounded 1c', sans-serif;
}

.container {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.landing {
  margin-top: 20%;
  border: solid 2px grey;
  width: 500px;
  height: 500px;
}

</style>
