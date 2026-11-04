<script setup lang="ts">
import { onMounted, ref } from 'vue'

const message = ref('Loading…')
const error = ref<string | null>(null)

onMounted(async () => {
  try {
    const response = await fetch('/api')
    if (!response.ok) {
      throw new Error(`Request failed (${response.status})`)
    }
    const data = (await response.json()) as { message: string }
    message.value = data.message
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Request failed'
  }
})
</script>

<template>
  <main>
    <p class="label">API</p>
    <h1 v-if="error">{{ error }}</h1>
    <h1 v-else>{{ message }}</h1>
  </main>
</template>

<style>
body {
  margin: 0;
  background: #fafafa;
  color: #1a1a1a;
  font-family: system-ui, sans-serif;
}
</style>

<style scoped>
main {
  max-width: 40rem;
  margin: 4rem auto;
  padding: 0 1.5rem;
}

.label {
  margin: 0;
  color: #5c5c5c;
  font-size: 0.875rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

h1 {
  margin: 0.5rem 0 0;
  font-size: 2rem;
  font-weight: 600;
}
</style>
