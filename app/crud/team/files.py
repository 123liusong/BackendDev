#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :files.py
@说明        :团队文件
@时间        :2023/02/11 16:29:12
@作者        :seanliu
'''

from sqlalchemy.orm import Session
from db import models,schemas

#通过团队id获取团队文件
def get_team_files_by_team_id(db: Session, team_id: int):
    return db.query(models.File).filter(models.File.team_id == team_id).all()

#通过团队id获取团队文件数量
def get_team_files_count_by_team_id(db: Session, team_id: int):
    return db.query(models.File).filter(models.File.team_id == team_id).count()

#通过团队id分页获取团队文件
def get_team_files_by_team_id_and_page(db: Session, team_id: int, page: int, page_size: int):
    return db.query(models.File).filter(models.File.team_id == team_id).offset((page - 1) * page_size).limit(page_size).all()

#创建团队文件
def create_team_files(db: Session, files: schemas.CreateFile):
    db_files = models.File(**files.dict())
    db.add(db_files)
    db.commit()
    db.refresh(db_files)
    return db_files

#修改团队文件
def update_team_files(db: Session, team_id: int, files: schemas.CreateFile):
    db.query(models.File).filter(models.File.team_id == team_id).update(files.dict())
    db.commit()

#删除团队文件
def delete_team_files(db: Session, team_id: int):
    db.query(models.File).filter(models.File.team_id == team_id).delete()
    db.commit()

# Path: app\crud\team\files.py