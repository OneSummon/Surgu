from pydantic import BaseModel

class CreateSchema(BaseModel):
    name: str
    description: str