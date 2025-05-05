from fastapi import FastAPI
from router import todo_route
from utils.init_db import create_tables

app = FastAPI(
    debug = True,
    title = "Todo"
)

@app.on_event("startup")
def on_startup() -> None:
    create_tables()

app.include_router(todo_route.router)