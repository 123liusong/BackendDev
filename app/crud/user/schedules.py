#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@文件        :schedules.py
@说明        :用户操作日程
@时间        :2023/02/11 16:00:58
@作者        :seanliu
"""

from sqlalchemy.orm import Session
from db import models, schemas


# 用户通过用户id获取用户的日程数量
def get_user_schedules_count_by_id(db: Session, user_id: int):
    return (
        db.query(models.Schedule)
        .filter(models.Schedule.user_id == user_id)
        .count()
    )


# 用户通过用户id分页获取用户的日程
def get_user_schedules_by_id_and_page(
    db: Session, user_id: int, page: int, page_size: int
):
    return (
        db.query(models.Schedule)
        .filter(models.Schedule.user_id == user_id)
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )


# 用户通过用户id获取用户的日程
def get_user_schedules_by_id(db: Session, user_id: int):
    return (
        db.query(models.Schedule)
        .filter(models.Schedule.user_id == user_id)
        .all()
    )


# 用户修改日程
def update_user_schedules(
    db: Session, user_id: int, schedules: schemas.CreateSchedule
):
    db.query(models.Schedule).filter(
        models.Schedule.user_id == user_id
    ).update(schedules.dict())
    db.commit()


# 用户创建日程
def create_user_schedules(db: Session, schedules: schemas.CreateSchedule):
    db_schedules = models.Schedule(**schedules.dict())
    db.add(db_schedules)
    db.commit()
    db.refresh(db_schedules)
    return db_schedules


# 用户删除日程
def delete_user_schedules(db: Session, user_id: int):
    db.query(models.Schedule).filter(
        models.Schedule.user_id == user_id
    ).delete()
    db.commit()

# Path: app\crud\user\schedules.py