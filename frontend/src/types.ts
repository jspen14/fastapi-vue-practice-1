export enum Role {
  User = "user",
  Agent = "agent",
}

export interface Message {
  id: string;
  role: Role;
  content: string;
}
