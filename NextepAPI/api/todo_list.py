#!/usr/bin/python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas
from schema.hash import Hash


# Create todolist
def create(request: schemas.TodoList, db: Session):
    new_todolist = models.TodoList(
        title=request.title,
        creator_id=request.creator_id,
        team_id=request.team_id,
        count=request.count,
        state=request.state,
    )
    db.add(new_todolist)
    db.commit()
    db.refresh(new_todolist)
    return new_todolist

# Get all todolist
def get_all(db: Session):
    return db.query(models.TodoList).all()

# Get all todolist by user_id
def get_all_by_user_id(user_id: int, db: Session):
    return db.query(models.TodoList).filter(models.TodoList.user_id == user_id).all()

# Get all todolist by team_id
def get_all_by_team_id(team_id: int, db: Session):
    return db.query(models.TodoList).filter(models.TodoList.team_id == team_id).all()

# 获取清单通过用户id并且是团队
def get_all_by_user_id_and_team(user_id: int, db: Session):
    return db.query(models.TodoList).filter(models.TodoList.user_id == user_id, models.TodoList.team_id != 0).all()

# 获取清单通过用户id并且是个人
def get_all_by_user_id_and_personal(user_id: int, db: Session):
    return db.query(models.TodoList).filter(models.TodoList.creator_id == user_id, models.TodoList.team_id == 0).all()


# Get todolist by id
def show(id: int, db: Session):
    todolist = db.query(models.TodoList).filter(models.TodoList.id == id).first()
    if not todolist:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"TodoList with id {id} not found"
        )
    return todolist

# Update todolist
def update(id: int, request: schemas.TodoListUpdate, db: Session):
    todolist = db.query(models.TodoList).filter(models.TodoList.id == id)
    if not todolist.first():
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"TodoList with id {id} not found"
        )
    todolist.update(request.dict())
    db.commit()
    return "updated successfully"

# Delete todolist
def delete(id: int, db: Session):
    todolist = db.query(models.TodoList).filter(models.TodoList.id == id)
    if not todolist.first():
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"TodoList with id {id} not found"
        )
    todolist.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"






