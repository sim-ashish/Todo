from fastapi import FastAPI
from router import (todo_route, user_route)
from utils.init_db import create_tables

description = """
Todo API helps you do awesome stuff. 🚀

## Todos

* You can **read todos** (_implemented_).
* You can **update todos** (_implemented_).


## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    docs_url="/documentation",
    redoc_url=None,
    debug = True,
    title = "Todo App",
    description = description,
    summary="User's favorite app for todos.",
    version="0.0.1",
    contact={
        "name": "Ashish Chaudhary",
        "url": "https://github.com/sim-ashish",
        "email": "chauashish21@gmail.com",
    },
)

@app.on_event("startup")
def on_startup() -> None:
    create_tables()

app.include_router(todo_route.router)
app.include_router(user_route.router)
