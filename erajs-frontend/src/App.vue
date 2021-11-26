<template lang="pug">
RouterView
</template>

<script setup lang="ts">
import { RouterView, useRouter } from 'vue-router'
import { get } from 'js-cookie'
const router = useRouter()
router.push('/idle')
// Auto Login
const uid = get('uid')
if (uid) {
  // fetch
}
</script>