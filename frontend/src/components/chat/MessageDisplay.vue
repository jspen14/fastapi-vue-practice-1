<script setup lang="ts">
import { Role, type Message } from "../../types";

defineProps<{
  messages: Message[];
  waiting: boolean;
}>();
</script>

<template>
  <ol class="messages">
    <li
      v-for="message in messages"
      :key="message.id"
      class="message"
      :class="message.role === Role.User ? 'user' : 'agent'"
    >
      {{ message.content }}
    </li>
    <li v-if="waiting" class="message agent typing" aria-label="Agent is typing">
      <span class="dot" />
      <span class="dot" />
      <span class="dot" />
    </li>
  </ol>
</template>

<style scoped>
.messages {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  margin: 0;
  margin-top: auto;
  padding: 0;
  list-style: none;
}

.message {
  max-width: 75%;
  margin: 0;
  padding: 0.5rem 0.85rem;
  border-radius: 1.15rem;
  line-height: 1.35;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
}

.agent {
  align-self: flex-start;
  background: #e5e5ea;
  color: #1a1a1a;
  border-bottom-left-radius: 0.25rem;
}

.user {
  align-self: flex-end;
  background: #007aff;
  color: white;
  border-bottom-right-radius: 0.25rem;
}

.typing {
  display: flex;
  align-items: center;
  gap: 0.28rem;
  padding: 0.75rem 0.85rem;
}

.dot {
  width: 0.45rem;
  height: 0.45rem;
  border-radius: 50%;
  background: #8e8e93;
  animation: bounce 1.2s infinite ease-in-out;
}

.dot:nth-child(2) {
  animation-delay: 0.15s;
}

.dot:nth-child(3) {
  animation-delay: 0.3s;
}

@keyframes bounce {
  0%,
  60%,
  100% {
    transform: translateY(0);
    opacity: 0.45;
  }

  30% {
    transform: translateY(-0.22rem);
    opacity: 1;
  }
}
</style>
