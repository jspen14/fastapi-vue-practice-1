from fastapi import APIRouter, FastAPI

from .routers import groups, messages, users

app = FastAPI(title="Vue FastAPI Demo")
api_router = APIRouter(prefix="/api")


@app.get("/")
@api_router.get("")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


api_router.include_router(users.router)
api_router.include_router(groups.router)
api_router.include_router(messages.router)
app.include_router(api_router)
