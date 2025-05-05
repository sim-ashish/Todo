from fastapi import FastAPI
from router import todo_route

app = FastAPI()

app.include_router(todo_route.router)