from fastapi import FastAPI
from app.routes import todo_route
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo List App")

app.include_router(todo_route.router)
