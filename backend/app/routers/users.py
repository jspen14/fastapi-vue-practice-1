from fastapi import APIRouter

from ..models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def read_users() -> list[User]:
    return [
        User(id="1", name="Ada"),
        User(id="2", name="Grace"),
        User(id="3", name="Lin"),
    ]
