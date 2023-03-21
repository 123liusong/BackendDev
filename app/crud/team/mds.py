#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :mds.py
@说明        :团队md文件
@时间        :2023/02/11 16:25:57
@作者        :seanliu
'''

from sqlalchemy.orm import Session
from db import models,schemas

#通过团队id获取团队md
def get_team_mds_by_team_id(db: Session, team_id: int):
    return db.query(models.MarkdownFile).filter(models.MarkdownFile.team_id == team_id).all()
    
#通过团队id获取团队md数量
def get_team_mds_count_by_team_id(db: Session, team_id: int):
    return db.query(models.MarkdownFile).filter(models.MarkdownFile.team_id == team_id).count()

#通过团队id分页获取团队md
def get_team_mds_by_team_id_and_page(db: Session, team_id: int, page: int, page_size: int):
    return db.query(models.MarkdownFile).filter(models.MarkdownFile.team_id == team_id).offset((page - 1) * page_size).limit(page_size).all()

#添加团队md
def create_team_md(db: Session, team_md: schemas.CreateMarkdownFile):
    db_team_md = models.MarkdownFile(**team_md.dict())
    db.add(db_team_md)
    db.commit()
    db.refresh(db_team_md)
    return db_team_md

#修改团队md
def update_team_md(db: Session, team_md_id: int, team_md: schemas.CreateMarkdownFile):
    db.query(models.MarkdownFile).filter(models.MarkdownFile.id == team_md_id).update(team_md.dict())
    db.commit()

#删除团队md
def delete_team_md(db: Session, team_md_id: int):
    db.query(models.MarkdownFile).filter(models.MarkdownFile.id == team_md_id).delete()
    db.commit()

# Path: app\crud\team\mds.py