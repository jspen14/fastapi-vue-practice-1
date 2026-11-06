from fastapi import APIRouter, FastAPI

from .routers import messages, recommendations

app = FastAPI(title="Vue FastAPI Demo")
api_router = APIRouter(prefix="/api")
api_router.include_router(messages.router)
api_router.include_router(recommendations.router)
app.include_router(api_router)
