<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { getMessages, type Message } from './api'
import ChatInterface from './components/chat/ChatInterface.vue'

const messages = ref<Message[]>([])

onMounted(async () => {
  messages.value = await getMessages()
})
</script>

<template>
  <ChatInterface :messages="messages" />
</template>

<style>
body {
  margin: 0;
  background: #fafafa;
  color: #1a1a1a;
  font-family: system-ui, sans-serif;
}
</style>
