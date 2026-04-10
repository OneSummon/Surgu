from fastapi import APIRouter, HTTPException
from session_dep import SessionDep
from schemas.nodes import CreateSchema
from cruds.nodes import get_node_by_name, set_node

router = APIRouter(prefix="/nodes", tags=["Nodes"])

@router.post("")
async def create(data: CreateSchema, session: SessionDep):
    exst_node = await get_node_by_name(data.name, session)
    if exst_node:
        raise HTTPException(status_code=400, detail="Node already exists")
    
    new_node = await set_node(data, session)

    return new_node