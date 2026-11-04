from pydantic import BaseModel


class Message(BaseModel):
    id: str
    name: str

    def get_name(self) -> str:
        return self.name
