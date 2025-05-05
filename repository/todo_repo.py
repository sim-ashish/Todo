from sqlalchemy.orm import Session
from typing import List, Any
from uuid import UUID


from schemas.todo_schema import (InputTodo,
                                 OutputTodo)
from models import todo as todo_model


def instance_exist(id: UUID, db: Session) -> bool:
    todo_instance = db.query(todo_model.Todo).filter(todo_model.Todo.id == id).first()
    if todo_instance:
        return True
    
    return False


def get_all(db: Session) -> List[OutputTodo]:
    todos = db.query(todo_model.Todo).all()

    return todos

def create(todo: InputTodo, db: Session) -> OutputTodo:
    todo_instance = todo_model.Todo(**todo.model_dump())
    db.add(todo_instance)
    db.commit()
    db.refresh(todo_instance)

    return todo_instance


def retrieve(id: UUID, db: Session) -> OutputTodo:
    todo_instance = db.query(todo_model.Todo).filter(todo_model.Todo.id == id).first()

    return todo_instance


def destroy(id: UUID, db: Session):
    todo_instance = db.query(todo_model.Todo).filter(todo_model.Todo.id == id).first()
    db.delete(todo_instance)
    db.commit()

    return

