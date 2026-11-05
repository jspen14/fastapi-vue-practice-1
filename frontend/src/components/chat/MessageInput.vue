<script setup lang="ts">
const draft = defineModel<string>({ required: true });
const emit = defineEmits<{ send: [] }>();
</script>

<template>
  <form class="row" @submit.prevent="emit('send')">
    <input v-model="draft" class="input" type="text" aria-label="Message" />
    <button type="submit">Send</button>
  </form>
</template>

<style scoped>
.row {
  display: flex;
  gap: 0.5rem;
}

.input {
  flex: 1;
  min-width: 0;
  box-sizing: border-box;
  padding: 0.75rem 1rem;
  border: 1px solid #e4e4e4;
  border-radius: 0.5rem;
  background: white;
  color: inherit;
  font: inherit;
}

button {
  padding: 0.75rem 1rem;
  border: 0;
  border-radius: 0.5rem;
  background: #1a1a1a;
  color: white;
  font: inherit;
}
</style>
