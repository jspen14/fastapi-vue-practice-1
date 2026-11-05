from uuid import uuid4

from fastapi import APIRouter, HTTPException

from ..models.message import Message, Role, SendMessage

router = APIRouter(prefix="/messages", tags=["messages"])

messages: dict[str, Message] = {}


@router.post("")
async def send_message(body: SendMessage) -> Message:
    print("JTP-1")
    message = Message(id=str(uuid4()), role=Role.user, content=body.content)
    messages[body.previous_response_id] = message
    return message


@router.get("/{previous_response_id}")
async def get_message(previous_response_id: str) -> Message:
    print("JTP-2")

    message = messages.get(previous_response_id)

    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")

    return message
