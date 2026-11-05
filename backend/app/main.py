from fastapi import APIRouter, FastAPI

from .routers import messages

app = FastAPI(title="Vue FastAPI Demo")
api_router = APIRouter(prefix="/api")
api_router.include_router(messages.router)
app.include_router(api_router)
