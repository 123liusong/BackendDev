#!/usr/bin/python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas

# 创建日程清单
def create(request: schemas.ScheduleTodoList, db: Session): 
    new_schedule_todo_list = models.ScheduleTodoList(
        schedule_id=request.schedule_id,
        todo_list_id=request.todo_list_id,
        )
    db.add(new_schedule_todo_list)
    db.commit()
    db.refresh(new_schedule_todo_list)
    return new_schedule_todo_list

# 获取所有日程清单
def get_all(db: Session):

    return db.query(models.ScheduleTodoList).all()


# 根据id获取日程清单
def get_by_id(id: int, db: Session):

    return db.query(models.ScheduleTodoList).filter(
        models.ScheduleTodoList.id == id).first()


# 根据日程id获取日程清单
def get_by_schedule_id(schedule_id: int, db: Session):
    
        return db.query(models.ScheduleTodoList).filter(
            models.ScheduleTodoList.schedule_id == schedule_id).all()
        

# 删除日程清单
def delete(id: int, db: Session):
    schedule_todo_list = db.query(models.ScheduleTodoList).filter(
        models.ScheduleTodoList.id == id)
    if not schedule_todo_list.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ScheduleTodoList with the id {id} is not available")
    schedule_todo_list.delete(synchronize_session=False)
    db.commit()
    return 'done delete schedule_todo_list'

# 根据日程id删除日程清单
def delete_by_schedule_id(schedule_id: int, db: Session):
    schedule_todo_list = db.query(models.ScheduleTodoList).filter(
        models.ScheduleTodoList.schedule_id == schedule_id)
    if not schedule_todo_list.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=
            f"ScheduleTodoList with the schedule_id {schedule_id} is not available"
        )
    schedule_todo_list.delete(synchronize_session=False)
    db.commit()
    return 'done delete schedules schedule_todo_list'

