from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str

    def get_name(self) -> str:
        return self.name
