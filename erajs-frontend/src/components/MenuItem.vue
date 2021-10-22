<template lang="pug">
.menu-item
  .menu-button(@click="clickButton")
    span {{ t(props.items.text) }}
    i.fa-solid.fa-caret-right(v-if="'submenu' in props.items")
  .menu-anchor(v-if="'submenu' in props.items && show")
    .menu-container
      MenuItem(v-for="v in props.items.submenu" :items="v" @iclick="clickChildren")
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
const props = defineProps(['items'])
const emits = defineEmits(['click', 'iclick'])
const show = ref(false)
function clickButton() {
  console.log(props.items);
  console.log('submenu' in props.items);
  if ('submenu' in props.items) {
    show.value = !show.value
  } else {
    emits('iclick')
  }
}
function clickChildren() {
  show.value = !show.value
  emits('iclick')
}
// onMounted(() => {
//   addEventListener('click', (e) => {
//     if (!this.contains(e.target)) {
//       show.value = !show.value
//     }
//   })
// })
</script>