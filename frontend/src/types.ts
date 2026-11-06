export enum Role {
  User = "user",
  Agent = "agent",
}

export interface Message {
  id: string;
  role: Role;
  content: string;
}

export interface MessageThread {
  response_id: string;
  messages: Message[];
}
