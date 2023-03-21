#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :team.py
@说明        :团队操作
@时间        :2023/02/11 16:06:56
@作者        :seanliu
'''

from sqlalchemy.orm import Session
from db import models,schemas

#通过团队id获取团队
def get_team_by_id(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

#修改团队
def update_team(db: Session, team_id: int, team: schemas.CreateTeam):
    db.query(models.Team).filter(models.Team.id == team_id).update(team.dict())
    db.commit()

#创建团队
def create_team(db: Session, team: schemas.CreateTeam):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

#删除团队
def delete_team(db: Session, team_id: int):
    db.query(models.Team).filter(models.Team.id == team_id).delete()
    db.commit()


# Path: app\crud\team\team.py