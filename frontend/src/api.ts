import axios from "axios";

import type { Message, MessageThread } from "./types";

export const api = axios.create({
  baseURL: "/api",
});

export async function getMessages(responseId: string): Promise<Message[]> {
  const { data } = await api.get<MessageThread>(
    `/messages/${encodeURIComponent(responseId)}`,
  );
  return data.messages;
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
