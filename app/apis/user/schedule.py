import time

from db import models, schemas
from crud.user import user as crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal, Base, engine

user_api = APIRouter()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 用户新增日程
@user_api.post("/user/schedule/create")
def user_schedule_create(schedule: schemas.CreateSchedule, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule_by_title(db, title=schedule.title)
    if db_schedule:
        return HTTPException(status_code=400, detail="Title already exists")
    return crud.create_schedule(db=db, schedule=schedule)

# 用户更新日程
@user_api.post("/user/schedule/update")
def user_schedule_update(schedule: schemas.UpdateSchedule, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule_by_title(db, title=schedule.title)
    if db_schedule is None:
        return HTTPException(status_code=400, detail="Title not exists")
    return crud.update_schedule(db=db, schedule=schedule)

# 用户删除日程
@user_api.post("/user/schedule/delete")
def user_schedule_delete(schedule: schemas.DeleteSchedule, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule_by_title(db, title=schedule.title)
    if db_schedule is None:
        return HTTPException(status_code=400, detail="Title not exists")
    return crud.delete_schedule(db=db, schedule=schedule)

# 用户根据id获取日程
@user_api.get("/user/schedule/get")
def user_schedule_get(schedule: schemas.GetSchedule, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule_by_id(db, id=schedule.id)
    if db_schedule is None:
        return HTTPException(status_code=400, detail="Schedule not exists")
    return db_schedule


