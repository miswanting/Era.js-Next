<template lang="pug">
header.header
  MenuBar
  .title-bar Era.js
  UserBar
  LanguageBar
  .status-bar
    i.fa-solid.fa-heart-pulse.fa-fw
    i.fa-solid.fa-heart-crack.fa-fw
    i.fa-solid.fa-heart.fa-fw
  .theme-bar
    i.fa-solid.fa-sun.fa-fw
    i.fa-solid.fa-moon.fa-fw
  .window-bar
    i.fa-solid.fa-minus.fa-fw
    i.fa-solid.fa-plus.fa-fw
    i.fa-solid.fa-times.fa-fw
</template>
<script setup lang="ts">
import MenuBar from "./MenuBar.vue";
import LanguageBar from "./LanguageBar.vue";
import UserBar from "./UserBar.vue";
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>