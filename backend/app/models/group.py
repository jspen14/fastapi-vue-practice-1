from pydantic import BaseModel


class Group(BaseModel):
    id: str
    name: str

    def get_name(self) -> str:
        return self.name
