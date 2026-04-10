from sqlalchemy import select
from session_dep import SessionDep
from schemas.nodes import CreateSchema
from database.models import Node
from datetime import datetime

async def get_node_by_name(node_name: str, session: SessionDep):
    return await session.scalar(select(Node).where(Node.name == node_name))

async def set_node(data: CreateSchema, session: SessionDep):
    new_node = Node(
        name=data.name,
        description=data.description,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    session.add(new_node)
    await session.commit()

    return new_node