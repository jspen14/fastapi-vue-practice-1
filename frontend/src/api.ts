import axios from 'axios'

import type { Message } from './types'

export const api = axios.create({
  baseURL: '/api',
})

const messages: Message[] = [
  { id: '1', role: 'user', content: 'Where do I find the holiday hours?' },
  { id: '2', role: 'assistant', content: 'Holiday hours are posted on the store page.' },
]

export async function getMessages(): Promise<Message[]> {
  return messages
}
