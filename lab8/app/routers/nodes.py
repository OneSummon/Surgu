from fastapi import APIRouter, HTTPException, status
from session_dep import SessionDep
from schemas.nodes import CreateSchema, NodeResponseSchema, UpdateSchema
from cruds.nodes import get_node_by_name, set_node, get_nodes, get_node_by_id, update_node, delete_node

router = APIRouter(prefix="/nodes", tags=["Nodes"])

@router.post("", status_code=status.HTTP_201_CREATED)
async def create(data: CreateSchema, session: SessionDep):
    exst_node = await get_node_by_name(data.name, session)
    if exst_node:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Node already exists")
    
    new_node = await set_node(data, session)

    return new_node


@router.get("", response_model=list[NodeResponseSchema])
async def all_nodes(session: SessionDep, limit: int = 10, offset: int = 0):
    nodes = await get_nodes(session, limit, offset)
    return nodes


@router.get("/{node_id}", response_model=NodeResponseSchema)
async def one_node(node_id: int, session: SessionDep):
    node = await get_node_by_id(node_id, session)
    return node


@router.put("/{node_id}", response_model=NodeResponseSchema)
async def update(node_id: int, data: UpdateSchema, session: SessionDep):
    exst_node = await get_node_by_id(node_id, session)

    if not exst_node:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Node is not found")
    
    upd_node = await update_node(node_id, data, session)
    return upd_node

@router.delete("/{node_id}")
async def delete(node_id: int, session: SessionDep):
    exst_node = await get_node_by_id(node_id, session)

    if not exst_node:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Node is not found")
    
    await delete_node(node_id, session)
    return {"delete": "true"}