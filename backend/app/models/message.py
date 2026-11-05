from typing import Literal

from pydantic import BaseModel


class Message(BaseModel):
    id: str
    role: Literal["user", "assistant"]
    content: str


class SendMessage(BaseModel):
    conversation_id: str
    content: str
