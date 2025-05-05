from schemas.todo_schema import (InputTodo,
                                OutputTodo,)
from fastapi import HTTPException, status
from typing import List, Any
from uuid import UUID
from repository import todo_repo
from sqlalchemy.orm import Session

def list_service(db: Session) -> List[OutputTodo]:
    return todo_repo.get_all(db)

def create_service(todo: InputTodo, db: Session) -> OutputTodo:
    return todo_repo.create(todo, db)

def retrieve_service(id: UUID, db: Session) -> OutputTodo:
    if todo_repo.instance_exist(id, db):
        return todo_repo.retrieve(id, db)
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'object with id not found')

def destroy_service(id: UUID, db: Session):
    if todo_repo.instance_exist(id, db):
        return todo_repo.destroy(id, db)
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'object with this id not found')