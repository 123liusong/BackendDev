#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :todolist.py
@说明        :团队操作清单
@时间        :2023/02/11 16:16:12
@作者        :seanliu
'''

from sqlalchemy.orm import Session
from db import models,schemas

#通过团队id获取团队清单
def get_team_todolist_by_team_id(db: Session, team_id: int):
    return db.query(models.TodoList).filter(models.TodoList.team_id == team_id).all()

#通过团队id获取团队清单数量
def get_team_todolist_count_by_team_id(db: Session, team_id: int):
    return db.query(models.TodoList).filter(models.TodoList.team_id == team_id).count()

#通过团队id分页获取团队清单
def get_team_todolist_by_team_id_and_page(db: Session, team_id: int, page: int, page_size: int):
    return db.query(models.TodoList).filter(models.TodoList.team_id == team_id).offset((page - 1) * page_size).limit(page_size).all()

#添加团队清单
def create_team_todolist(db: Session, team_todolist: schemas.CreateTodoList):
    db_team_todolist = models.TodoList(**team_todolist.dict())
    db.add(db_team_todolist)
    db.commit()
    db.refresh(db_team_todolist)
    return db_team_todolist

#修改团队清单
def update_team_todolist(db: Session, team_todolist_id: int, team_todolist: schemas.CreateTodoList):
    db.query(models.TodoList).filter(models.TodoList.id == team_todolist_id).update(team_todolist.dict())
    db.commit()

#删除团队清单
def delete_team_todolist(db: Session, team_todolist_id: int):
    db.query(models.TodoList).filter(models.TodoList.id == team_todolist_id).delete()
    db.commit()

# Path: app\crud\team\todolist.py

