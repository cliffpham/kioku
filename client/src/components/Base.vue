<template>
  <b-container>
    <transition name="fade" mode="out-in">
    <component v-bind:is="component" v-on:startGame="component='Game'"></component>
    </transition>
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

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .3s ease;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
