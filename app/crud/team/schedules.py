#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :schedules.py
@说明        :团队操作日程
@时间        :2023/02/11 16:21:59
@作者        :seanliu
'''

from sqlalchemy.orm import Session
from db import models, schemas

# 团队通过团队id获取团队的日程数量
def get_team_schedules_count_by_id(db: Session, team_id: int):
    return (
        db.query(models.Schedule)
        .filter(models.Schedule.team_id == team_id)
        .count()
    )

# 团队通过团队id获取团队的日程
def get_team_schedules_by_id(db: Session, team_id: int):
    return (
        db.query(models.Schedule)
        .filter(models.Schedule.team_id == team_id)
        .all()
    )

# 团队通过团队id分页获取团队的日程
def get_team_schedules_by_id_and_page(db: Session, team_id: int, page: int, page_size: int):
    return (
        db.query(models.Schedule)
        .filter(models.Schedule.team_id == team_id)
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

#添加团队日程
def create_team_schedules(db: Session, team_schedules: schemas.CreateSchedule):
    db_team_schedules = models.Schedule(**team_schedules.dict())
    db.add(db_team_schedules)
    db.commit()
    db.refresh(db_team_schedules)
    return db_team_schedules

#修改团队日程
def update_team_schedules(db: Session, team_id: int, schedule_id: int, team_schedules: schemas.CreateSchedule):
    db.query(models.Schedule).filter(models.Schedule.id == schedule_id, models.Schedule.team_id == team_id).update(team_schedules.dict())
    db.commit()

#删除团队日程
def delete_team_schedules(db: Session, team_id: int, schedule_id: int):
    db.query(models.Schedule).filter(models.Schedule.id == schedule_id, models.Schedule.team_id == team_id).delete()
    db.commit()

# Path: app\crud\team\schedules.py

