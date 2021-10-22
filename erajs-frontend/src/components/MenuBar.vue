<template lang="pug">
.menu-bar
  MenuItem(v-for="v in items" :items="v")
</template>
<script setup lang="ts">
import MenuItem from "./MenuItem.vue";
const items = [
  {
    text: 'File',
    submenu: [
      { text: 'New' },
      { text: 'Open' },
      {
        text: 'Open Recent',
        submenu: [
          { text: '123' },
          { text: '123' },
        ]
      },
    ]
  },
  { text: 'Edit' },
]
</script>