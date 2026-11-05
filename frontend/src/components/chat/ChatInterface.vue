<template>
  <section class="chat" aria-label="Chat">
    <header class="header">
      <p class="label">Chat</p>
    </header>
    <div class="thread" />
    <footer class="composer" />
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
}
</style>
