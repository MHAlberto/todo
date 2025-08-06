from sqlalchemy.orm import Session
from app.models.todo_model import ToDo
from app.schemas.todo_schema import ToDoCreate, ToDoUpdate

def get_todos(db: Session):
    return db.query(ToDo).all()

def get_todo(db: Session, todo_id: int):
    return db.query(ToDo).filter(ToDo.id == todo_id).first()

def create_todo(db: Session, todo: ToDoCreate):
    db_todo = ToDo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo_data: ToDoUpdate):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
        return None
    for key, value in todo_data.dict().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
        return None
    db.delete(todo)
    db.commit()
    return todo
