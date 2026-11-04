from fastapi import APIRouter

from ..models.group import Group

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/")
async def read_groups() -> list[Group]:
    return [
        Group(id="1", name="Engineering"),
        Group(id="2", name="Design"),
        Group(id="3", name="Support"),
    ]
