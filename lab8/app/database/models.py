from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Node(Base):
    __tablename__ = "nodes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    description: Mapped[str]
    status: Mapped[str] = mapped_column(default="not-completed")
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]