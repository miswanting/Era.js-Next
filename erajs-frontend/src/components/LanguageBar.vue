<template lang="pug">
.language-bar
  .language-button(@click="click")
    i.fa-solid.fa-language.fa-fw
  .language-anchor(v-if="show")
    .language-container
      div(v-for="v in $i18n.availableLocales") {{ v }}
</template>
<script setup lang="ts">
import { ref } from 'vue'
const show = ref(false)
import MenuBar from "./MenuBar.vue";
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
function click() {
  show.value = !show.value
}
</script>