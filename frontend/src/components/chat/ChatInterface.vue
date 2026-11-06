<script setup lang="ts">
import { ref } from "vue";

import type { Message } from "../../types";
import MessageDisplay from "./MessageDisplay.vue";
import MessageInput from "./MessageInput.vue";

defineProps<{
  messages: Message[];
  waiting: boolean;
}>();

const emit = defineEmits<{ send: [content: string] }>();

const draft = ref("");

function submit() {
  const content = draft.value.trim();
  if (!content) return;
  emit("send", content);
  draft.value = "";
}
</script>

<template>
  <section class="chat" aria-label="Chat">
    <header class="header">
      <p class="label">Chat</p>
    </header>
    <div class="thread">
      <MessageDisplay :messages="messages" :waiting="waiting" />
    </div>
    <footer class="composer">
      <MessageInput v-model="draft" @send="submit" />
    </footer>
  </section>
</template>

<style scoped>
.chat {
  display: flex;
  flex-direction: column;
  height: 100vh;
  max-width: 40rem;
  margin: 0 auto;
}

.header,
.composer {
  padding: 1rem 1.5rem;
}

.label {
  margin: 0;
  color: #5c5c5c;
  font-size: 0.875rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.thread {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding: 0.75rem 1.5rem;
}
</style>
