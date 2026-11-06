<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { getMessages, sendMessage } from './api'
import { Role, type Message } from './types'
import ChatInterface from './components/chat/ChatInterface.vue'

const previousResponseIdKey = 'previous_response_id'

const messages = ref<Message[]>([])
const responseId = ref<string | null>(null)
const waiting = ref(false)

onMounted(async () => {
  const stored = localStorage.getItem(previousResponseIdKey)
  if (!stored) return
  responseId.value = stored
  messages.value = await getMessages(stored)
})

async function onSend(content: string) {
  messages.value = [
    ...messages.value,
    { id: crypto.randomUUID(), role: Role.User, content },
  ]
  waiting.value = true
  try {
    const thread = await sendMessage(content, responseId.value)
    messages.value = thread.messages
    responseId.value = thread.response_id
    localStorage.setItem(previousResponseIdKey, thread.response_id)
  } finally {
    waiting.value = false
  }
}
</script>

<template>
  <ChatInterface :messages="messages" :waiting="waiting" @send="onSend" />
</template>

<style>
body {
  margin: 0;
  background: #fafafa;
  color: #1a1a1a;
  font-family: system-ui, sans-serif;
}
</style>
