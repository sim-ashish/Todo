from fastapi import APIRouter, status
from schemas import (InputTodo,OutputTodo) 

router = APIRouter (
    prefix = "/todo",
    tags = ['Todo']
)

@router.get(
        '/',
        status_code=status.HTTP_200_OK, 
        summary="List all todos",
        description="List all the todos for the authenticated user"
        )
def all_todo():
    return {'Todo' : 'Working'}


@router.post(
            '/', 
            status_code=status.HTTP_201_CREATED,
            summary="Create a Todo",
            description="Create a new todo"
            )
def create_todo(todo: InputTodo) -> OutputTodo :
    return todo


@router.put('/', status_code=status.HTTP_200_OK)
def update_todo():
    return {'Todo Put' : 'Working'}


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def destroy_todo():
    return {'Todo Delete' : 'Working'}