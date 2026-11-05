from uuid import uuid4

from fastapi import APIRouter, HTTPException

from ..models.message import Message, Role, SendMessage

router = APIRouter(prefix="/messages", tags=["messages"])

messages: dict[str, Message] = {}


@router.post("")
async def send_message(body: SendMessage) -> Message:
    message = Message(id=str(uuid4()), role=Role.user, content=body.content)
    messages[body.conversation_id] = message
    return message


@router.get("/{conversation_id}")
async def get_message(conversation_id: str) -> Message:
    message = messages.get(conversation_id)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return message
