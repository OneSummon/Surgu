from sqlalchemy import select, delete
from session_dep import SessionDep
from schemas.nodes import CreateSchema, UpdateSchema
from database.models import Node
from datetime import datetime

async def get_node_by_name(node_name: str, session: SessionDep):
    return await session.scalar(select(Node).where(Node.name == node_name))

async def get_node_by_id(node_id: int, session: SessionDep):
    return await session.scalar(select(Node).where(Node.id == node_id))    

async def get_nodes(session: SessionDep, limit: int, offset: int):
    return await session.scalars(select(Node).limit(limit).offset(offset))

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


async def update_node(node_id: int, data: UpdateSchema, session: SessionDep):
    upd_node = await get_node_by_id(node_id, session)
    if not upd_node:
        return None

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(upd_node, field, value)
    
    upd_node.updated_at = datetime.now()
    
    await session.commit()
    return upd_node


async def delete_node(node_id: int, session: SessionDep):
    del_node = await session.scalar(select(Node).where(Node.id == node_id))
    await session.delete(del_node)
    await session.commit()