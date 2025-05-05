from fastapi import APIRouter, status,  Depends
from sqlalchemy.orm import Session
from schemas import (InputTodo,OutputTodo) 
from services import todo_services
from typing_extensions import Annotated
from config.database import get_db
from typing import List, Any
from uuid import UUID


router = APIRouter (
    prefix = "/todo",
    tags = ['Todo']
)

DB_CONNECTION = Annotated[Session, Depends(get_db)]

@router.get(
        '/',
        status_code=status.HTTP_200_OK, 
        summary="List all todos",
        description="List all the todos for the authenticated user"
        )
def all_todo(db: DB_CONNECTION) -> List[OutputTodo]:
    return todo_services.list_service(db)


@router.post(
            '/', 
            status_code=status.HTTP_201_CREATED,
            summary="Create a Todo",
            description="Create a new todo"
            )
def create_todo(todo: InputTodo, db: DB_CONNECTION) -> OutputTodo :
    return todo_services.create_service(todo, db)


@router.put('/', status_code=status.HTTP_200_OK)
def update_todo():
    return {'Todo Put' : 'Working'}



@router.get('/{id: UUID}', status_code=status.HTTP_200_OK)
def retrieve(id: UUID, db: DB_CONNECTION) -> OutputTodo :
    return todo_services.retrieve_service(id, db)


@router.delete('/{id: UUID}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_todo(id: UUID, db: DB_CONNECTION):
    return todo_services.destroy_service(id, db)