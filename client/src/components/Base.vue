<template>
  <b-container>
    <component v-bind:is="component" v-on:startGame="component='Game'"></component>
  </b-container>
</template>

<script>
import Start from './Start.vue';
import Game from './Game.vue';

export default {
  name: 'Base',
  components: {
    Start,
    Game,

  },
  data() {
    return {
      component: 'Start',
    };
  },
};

</script>
