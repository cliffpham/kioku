<template>
  <b-container>
    <b-row class="text-center">
      <b-col>
        <button v-on:click="handleClick"> Start </button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: 'Start',
  methods: {
    handleClick: function() {
      this.$emit('startGame')
    }
  }
}
</script>
