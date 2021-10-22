<template lang="pug">
Header
.login-container 
  form(action="/api/login" method="post")
    div
      label Username
    div
      input(type="text" name="username")
    div
      label Password
    div
      input(type="password" name="password")
    div
      button(type="submit") Submit
</template>
<style scoped lang="stylus">
form
  border .5px solid
  border-radius 5px
  padding 1rem
button
  width 100%
  margin-top .5rem
</style>
<script setup lang="ts">
import Header from '../components/Header.vue'
</script>