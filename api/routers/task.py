from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import api.cruds.task as task_crud
from api.db import get_db

import api.schemas.task as task_schema

router = APIRouter()

@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks(db: Session = Depends(get_db)):
    return task_crud.get_tasks_with_done(db)

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db: Session = Depends(get_db)):
    return task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return