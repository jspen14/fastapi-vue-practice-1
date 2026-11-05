from enum import StrEnum

from pydantic import BaseModel


class Role(StrEnum):
    user = "user"
    agent = "agent"


class Message(BaseModel):
    id: str
    role: Role
    content: str


class SendMessage(BaseModel):
    previous_response_id: str
    content: str
