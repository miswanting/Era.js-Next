<template lang="pug">
.user-bar
  .user-button(@click="click")
    i.fa-solid.fa-user-secret.fa-fw(v-if="!store.state.user.isLogined")
    i.fa-solid.fa-user.fa-fw(v-else-if="!store.state.user.isAdmin")
    i.fa-solid.fa-user-tie.fa-fw(v-else)
    span(v-if="store.state.user.isLogined") {{ store.state.user.username }}
</template>
<script setup lang="ts">
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
const store = useStore()
const router = useRouter()
function click() {
  router.push('/login')
}
</script>