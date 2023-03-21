#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :team.py
@说明        :用户查看所属、领导的团队
@时间        :2023/02/11 15:58:21
@作者        :seanliu
'''



from sqlalchemy.orm import Session
from db import models,schemas


#用户通过用户id获取用户所属的团队
def get_user_team_by_id(db: Session, user_id: int):
    return db.query(models.TeamMember).filter(models.TeamMember.user_id == user_id).all()

#用户通过用户id获取用户领导的团队
def get_user_team_by_leader_id(db: Session, user_id: int):
    return db.query(models.TeamMember).filter(models.TeamMember.leader_id == user_id).all()

#用户通过团队id和用户id获取记录
def get_user_team_by_user_id_and_team_id(db: Session, user_id: int, team_id: int):
    return db.query(models.TeamMember).filter(models.TeamMember.user_id == user_id, models.TeamMember.team_id == team_id).first()

#用户通过团队id添加团队
def create_user_team(db: Session, user_team: schemas.CreateTeamMember):
    db_user_team = models.TeamMember(**user_team.dict())
    db.add(db_user_team)
    db.commit()
    db.refresh(db_user_team)
    return db_user_team



    
# Path: app\crud\user\team.py
    
    