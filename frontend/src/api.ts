import axios from "axios";

import type { Message, MessageThread } from "./types";

export const api = axios.create({
  baseURL: "/api",
});

const messages: Message[] = [];

export async function getMessages(): Promise<Message[]> {
  return messages;
}

export async function sendMessage(
  draft: string,
  previousResponseId: string | null,
): Promise<MessageThread> {
  const { data } = await api.post<MessageThread>("/messages", {
    content: draft,
    previous_response_id: previousResponseId,
  });
  return data;
}
