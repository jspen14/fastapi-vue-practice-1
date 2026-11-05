from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from openai import NotFoundError, OpenAI

from ..models.message import Message, MessageThread, Role, SendMessage

load_dotenv()

router = APIRouter(prefix="/messages", tags=["messages"])

MODEL = "gpt-5.6-luna"


def messages_from_page(page: object) -> list[Message]:
    return [
        message
        for item in getattr(page, "data", [])
        if (message := message_from_item(item))
    ]


def message_from_item(item: object) -> Message | None:
    if getattr(item, "type", None) != "message":
        return None
    role = getattr(item, "role", None)
    if role == "user":
        text = text_from_parts(item, "input_text")
        mapped = Role.user
    elif role == "assistant":
        text = text_from_parts(item, "output_text") or text_from_parts(item, "input_text")
        mapped = Role.agent
    else:
        return None
    if text is None:
        return None
    return Message(id=item.id, role=mapped, content=text)


def text_from_parts(item: object, part_type: str) -> str | None:
    parts = [
        part.text
        for part in getattr(item, "content", [])
        if getattr(part, "type", None) == part_type
    ]
    text = "".join(parts).strip()
    return text or None


@router.post("")
async def send_message(body: SendMessage) -> MessageThread:
    client = OpenAI()
    response = client.responses.create(
        model=MODEL,
        input=body.content,
        **(
            {"previous_response_id": body.previous_response_id}
            if body.previous_response_id
            else {}
        ),
    )
    page = client.responses.input_items.list(response.id, order="asc", limit=100)
    return MessageThread(response_id=response.id, messages=messages_from_page(page))


@router.get("/{previous_response_id}")
async def get_messages(previous_response_id: str) -> MessageThread:
    client = OpenAI()
    try:
        page = client.responses.input_items.list(
            previous_response_id, order="asc", limit=100
        )
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Response not found")
    return MessageThread(response_id=previous_response_id, messages=messages_from_page(page))
