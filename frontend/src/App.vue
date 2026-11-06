<script setup lang="ts">
import { onMounted, ref } from "vue";

import { getMessages, getRecommendations, sendMessage } from "./api";
import { Role, type Message, type Recommendation } from "./types";
import ChatInterface from "./components/chat/ChatInterface.vue";

const previousResponseIdKey = "previous_response_id";

const messages = ref<Message[]>([]);
const recommendations = ref<Recommendation[]>([]);
const responseId = ref<string | null>(null);
const waiting = ref(false);
let sendId = 0;

async function loadRecommendations() {
  recommendations.value = await getRecommendations();

  console.log("JTP-1", recommendations.value);
}

onMounted(async () => {
  const stored = localStorage.getItem(previousResponseIdKey);
  if (!stored) {
    await loadRecommendations();
    return;
  }
  responseId.value = stored;
  messages.value = await getMessages(stored);
  if (messages.value.length === 0) await loadRecommendations();
});

function onNewChat() {
  sendId += 1;
  messages.value = [];
  responseId.value = null;
  waiting.value = false;
  localStorage.removeItem(previousResponseIdKey);
  void loadRecommendations();
}

async function onSend(content: string) {
  const id = ++sendId;
  messages.value = [
    ...messages.value,
    { id: crypto.randomUUID(), role: Role.User, content },
  ];
  waiting.value = true;
  try {
    const thread = await sendMessage(content, responseId.value);
    if (id !== sendId) return;
    messages.value = thread.messages;
    responseId.value = thread.response_id;
    localStorage.setItem(previousResponseIdKey, thread.response_id);
  } finally {
    if (id === sendId) waiting.value = false;
  }
}
</script>

<template>
  <ChatInterface
    :messages="messages"
    :waiting="waiting"
    @send="onSend"
    @new-chat="onNewChat"
  />
</template>

<style>
body {
  margin: 0;
  background: #fafafa;
  color: #1a1a1a;
  font-family: system-ui, sans-serif;
}
</style>
