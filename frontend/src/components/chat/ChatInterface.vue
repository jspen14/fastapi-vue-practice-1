<script setup lang="ts">
import { ref } from "vue";

import type { Message } from "../../types";
import MessageDisplay from "./MessageDisplay.vue";
import MessageInput from "./MessageInput.vue";

defineProps<{
  messages: Message[];
  waiting: boolean;
}>();

const emit = defineEmits<{ send: [content: string]; newChat: [] }>();

const draft = ref("");
const menuOpen = ref(false);

function submit() {
  const content = draft.value.trim();
  if (!content) return;
  emit("send", content);
  draft.value = "";
}

function startNewChat() {
  menuOpen.value = false;
  draft.value = "";
  emit("newChat");
}
</script>

<template>
  <section class="chat" aria-label="Chat">
    <header class="header">
      <div v-if="menuOpen" class="backdrop" @click="menuOpen = false" />
      <div class="menu">
        <button
          type="button"
          class="menu-button"
          aria-label="Chat menu"
          aria-haspopup="menu"
          :aria-expanded="menuOpen"
          @click="menuOpen = !menuOpen"
        >
          <svg viewBox="0 0 16 16" aria-hidden="true">
            <path
              d="M2 4.5h12M2 8h12M2 11.5h12"
              fill="none"
              stroke="currentColor"
              stroke-width="1.5"
              stroke-linecap="round"
            />
          </svg>
        </button>
        <ul v-if="menuOpen" class="dropdown" role="menu">
          <li role="none">
            <button type="button" class="item" role="menuitem" @click="startNewChat">
              Start a new chat
            </button>
          </li>
        </ul>
      </div>
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

.header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.backdrop {
  position: fixed;
  inset: 0;
}

.menu {
  position: relative;
}

.menu-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2rem;
  height: 2rem;
  padding: 0;
  border: 0;
  border-radius: 0.5rem;
  background: transparent;
  color: inherit;
  cursor: pointer;
}

.menu-button:hover {
  background: #ececec;
}

.menu-button svg {
  width: 1rem;
  height: 1rem;
}

.dropdown {
  position: absolute;
  top: calc(100% + 0.35rem);
  left: 0;
  z-index: 1;
  min-width: 11rem;
  margin: 0;
  padding: 0.25rem;
  list-style: none;
  border: 1px solid #e4e4e4;
  border-radius: 0.5rem;
  background: white;
  box-shadow: 0 0.5rem 1.5rem rgb(0 0 0 / 8%);
}

.item {
  width: 100%;
  padding: 0.5rem 0.75rem;
  border: 0;
  border-radius: 0.35rem;
  background: transparent;
  color: inherit;
  font: inherit;
  text-align: left;
  cursor: pointer;
}

.item:hover {
  background: #f3f3f3;
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
