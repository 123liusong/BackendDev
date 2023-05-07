#!/usr/bin/python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from models import models
from schema import schemas
from datetime import datetime


# 获取所有日程
def get_all(db: Session):

    return db.query(models.Schedule).all()


# 根据创建者id获取日程
def get_all_by_creator_id(creator_id: int, db: Session):

    return db.query(models.Schedule).filter(
        models.Schedule.creator_id == creator_id).all()


# 当前用户所有的个人日程
def get_all_by_creator_id_and_personal(creator_id: int, db: Session):

    return db.query(models.Schedule).filter(
        models.Schedule.creator_id == creator_id).filter(
            models.Schedule.team_id == 0).all()


# 当前用户所有的团队日程 不用
# def get_all_by_creator_id_and_team(creator_id: int, db: Session):

#     return db.query(models.Schedule).filter(
#         models.Schedule.creator_id == creator_id).filter(
#             models.Schedule.team_id != None).all()


# 根据team_id获取日程
def get_all_by_team_id(team_id: int, db: Session):
    return db.query(
        models.Schedule).filter(models.Schedule.team_id == team_id).all()


# 根据id获取日程
def get_by_id(id: int, db: Session):

    return db.query(models.Schedule).filter(models.Schedule.id == id).first()


# 起止时间在某个时间段内的日程
def get_by_start_end(start: datetime, end: datetime, db: Session):
    return db.query(
        models.Schedule).filter(models.Schedule.start_time >= start).filter(
            models.Schedule.end_time <= end).all()
        
# 根据个人id、起止时间在某个时间段内、包含某些等级的日程
def get_by_user_start_end_level(start:datetime,end:datetime,level_c:int,db:Session,user_id:int):
    level =[0]
    if level_c == 1:
        level = [0]
    elif level_c == 2:
        level = [1]
    elif level_c == 3:
        level = [0,1]
    elif level_c == 4:
        level = [2]
    elif level_c == 5:
        level = [0,2]
    elif level_c == 6:
        level = [1,2]
    elif level_c == 7:
        level = [0,1,2]
    return db.query(models.Schedule).filter(models.Schedule.creator_id == user_id).filter(models.Schedule.start_time  <= end).filter(
            models.Schedule.end_time  >= start).filter(models.Schedule.level.in_(level)).all()


# 搜索创建者id并且开始时间小于结束时间结束时间大于开始时间的日程
def get_by_start_or_end(start_time: datetime, end_time: datetime, db: Session,
                        creator_id: int):
    return db.query(
        models.Schedule).filter(models.Schedule.creator_id == creator_id).filter(
            models.Schedule.start_time <= end_time).filter(
                models.Schedule.end_time >= start_time).all()

#删除creator_id为user_id的日程并且team_id为0的日程
def delete_by_creator_id_and_personal(user_id:int,db:Session):
    db.query(models.Schedule).filter(models.Schedule.creator_id == user_id).filter(models.Schedule.team_id == 0).delete(synchronize_session=False)
    db.commit()
    return "done delete schedule"


# create
def create(request: schemas.Schedule, db: Session):

    new_schedule = models.Schedule(**request.dict(), )
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    return new_schedule


def delete(id: int, db: Session):

    schedule_to_delete = db.query(
        models.Schedule).filter(models.Schedule.id == id)

    if not schedule_to_delete.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Schedule with id {id} not found.",
        )
    schedule_to_delete.delete(synchronize_session=False)
    db.commit()
    return "done delete schedule"


def update(id: int, request: schemas.ScheduleUpdate, db: Session):

    schedule = db.query(models.Schedule).filter(models.Schedule.id == id)
    if not schedule.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Schedule with id {id} not found")
    schedule.update(request.__dict__)
    db.commit()
    return "updated schedule"


def show(id: int, db: Session):

    schedule = db.query(
        models.Schedule).filter(models.Schedule.id == id).first()
    if schedule:
        return schedule
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Schedule with the id {id} is not available",
        )

# 根据返回的数组生成文件，返回文件流
def create_file(schedules: list):
    # 生成文件
    file_name = '日程表.csv'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('日程名称,开始时间,结束时间,日程等级,创建者,团队\n')
        for schedule in schedules:
            f.write(schedule.title + ',')
            f.write(schedule.start_time.strftime('%Y-%m-%d %H:%M:%S') + ',')
            f.write(schedule.end_time.strftime('%Y-%m-%d %H:%M:%S') + ',')
            f.write(str(schedule.level) + ',')
            f.write(str(schedule.creator_id) + ',')
            f.write(str(schedule.team_id )+ '\n')
    # 返回文件流
    with open(file_name, 'rb') as f:
        data = f.read()
    return data
