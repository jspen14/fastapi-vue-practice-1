from pydantic import BaseModel


class Recommendation(BaseModel):
    id: int
    text: str
