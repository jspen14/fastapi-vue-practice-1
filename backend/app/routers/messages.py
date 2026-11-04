from fastapi import APIRouter

from ..models.message import Message

router = APIRouter(prefix="/messages", tags=["messages"])


@router.get("/")
async def read_messages() -> list[Message]:
    return [
        Message(id="1", name="Welcome"),
        Message(id="2", name="Design review"),
        Message(id="3", name="Ship notes"),
    ]
