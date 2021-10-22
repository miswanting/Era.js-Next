<template lang="pug">
RouterView
</template>

<script setup lang="ts">
import { RouterView, useRouter } from 'vue-router'
const router = useRouter()
router.push('/idle')
</script>