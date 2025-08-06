from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.todo_schema import ToDoCreate, ToDoUpdate, ToDoResponse
from app.crud import todo_crud

router = APIRouter(prefix="/todos", tags=["ToDos"])

@router.get("/", response_model=list[ToDoResponse])
def list_todos(db: Session = Depends(get_db)):
    return todo_crud.get_todos(db)

@router.get("/{todo_id}", response_model=ToDoResponse)
def get_single_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

@router.post("/", response_model=ToDoResponse)
def create(todo: ToDoCreate, db: Session = Depends(get_db)):
    return todo_crud.create_todo(db, todo)

@router.put("/{todo_id}", response_model=ToDoResponse)
def update(todo_id: int, todo_data: ToDoUpdate, db: Session = Depends(get_db)):
    updated = todo_crud.update_todo(db, todo_id, todo_data)
    if not updated:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return updated

@router.delete("/{todo_id}", response_model=ToDoResponse)
def delete(todo_id: int, db: Session = Depends(get_db)):
    deleted = todo_crud.delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return deleted
