import axios from 'axios'

import { Role, type Message } from './types'

export const api = axios.create({
  baseURL: '/api',
})

const messages: Message[] = [
  { id: '1', role: Role.User, content: 'Where do I find the holiday hours?' },
  { id: '2', role: Role.Agent, content: 'Holiday hours are posted on the store page.' },
]

export async function getMessages(): Promise<Message[]> {
  return messages
}
