#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :user.py
@说明        :团员操作
@时间        :2023/02/11 16:12:13
@作者        :seanliu
'''

from sqlalchemy.orm import Session
from db import models,schemas

#在团队成员表通过团队id获取用户id   
def get_team_user_by_team_id(db: Session, team_id: int):
    return db.query(models.TeamMember).filter(models.TeamMember.team_id == team_id).all()

#在团队成员表通过团队id获取用户id数量
def get_team_user_count_by_team_id(db: Session, team_id: int):
    return db.query(models.TeamMember).filter(models.TeamMember.team_id == team_id).count()

#在团队成员表通过团队id分页获取用户id  
def get_team_user_by_team_id_and_page(db: Session, team_id: int, page: int, page_size: int):
    return db.query(models.TeamMember).filter(models.TeamMember.team_id == team_id).offset((page - 1) * page_size).limit(page_size).all()

#添加团队成员
def create_team_user(db: Session, team_user: schemas.CreateTeamMember):
    db_team_user = models.TeamMember(**team_user.dict())
    db.add(db_team_user)
    db.commit()
    db.refresh(db_team_user)
    return db_team_user

#删除团队成员
def delete_team_user(db: Session, team_id: int, user_id: int):
    db.query(models.TeamMember).filter(models.TeamMember.team_id == team_id).filter(models.TeamMember.user_id == user_id).delete()
    db.commit()

# Path: app\crud\team\user.py