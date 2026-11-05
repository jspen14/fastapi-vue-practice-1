from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from openai import NotFoundError, OpenAI

from ..models.message import Message, MessageThread, Role, SendMessage

load_dotenv()

router = APIRouter(prefix="/messages", tags=["messages"])

MODEL = "gpt-5.6-luna"

ROLES = {"user": Role.user, "assistant": Role.agent}


def messages_from(items: list[object]) -> list[Message]:
    messages: list[Message] = []

    for item in items:
        role = ROLES.get(getattr(item, "role", ""))
        if getattr(item, "type", None) != "message" or role is None:
            continue
        text = "".join(
            part.text
            for part in getattr(item, "content", [])
            if getattr(part, "type", None) in {"input_text", "output_text"}
        ).strip()
        if text:
            messages.append(Message(id=item.id, role=role, content=text))
    return messages


# JTODO - move this into a messaging service
def get_message_history_by_response_id(
    client: OpenAI, response_id: str
) -> list[Message]:
    response = client.responses.retrieve(response_id)
    page = client.responses.input_items.list(response.id, order="asc", limit=100)
    messages = messages_from(page.data)
    messages.extend(messages_from(response.output))
    return messages


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

    return MessageThread(
        response_id=response.id,
        messages=get_message_history_by_response_id(client, response.id),
    )


@router.get("/{response_id}")
async def get_messages(response_id: str) -> MessageThread:
    client = OpenAI()

    try:
        messages = get_message_history_by_response_id(client, response_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Response not found")

    return MessageThread(response_id=response_id, messages=messages)
