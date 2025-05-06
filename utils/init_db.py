from config.database import engine
from models.todo import Todo


def create_tables():
    Todo.metadata.create_all(bind=engine)