from pydantic import BaseModel, Field
from datetime import datetime

class CreateSchema(BaseModel):
    name: str
    description: str

class NodeResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    status: str
    updated_at: datetime

class UpdateSchema(BaseModel):
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    status: str | None = Field(default=None)
