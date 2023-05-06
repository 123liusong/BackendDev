from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas

# 创建日志
def create(request: schemas.Log, db: Session):
    new_log = models.Log(
        user_id=request.user_id,
        schedule_id=request.schedule_id,
        content=request.content,
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

# 获取所有日志 for admin
def get_all(db: Session):
    return db.query(models.Log).all()

# 根据id获取日志
def get_by_id(id: int, db: Session):
    return db.query(models.Log).filter(models.Log.id == id).first()

# 根据创建者id获取日志
def get_by_user_id(user_id: int, db: Session):
    return db.query(models.Log).filter(models.Log.user_id == user_id).all()

# 根据类型获取日志
def get_by_type(type: str, db: Session):
    return db.query(models.Log).filter(models.Log.type == type).all()

# 根据时间段
def get_by_time(start_time: str, end_time: str, db: Session):
    return db.query(models.Log).filter(
        models.Log.create_time.between(start_time, end_time)).all()
        