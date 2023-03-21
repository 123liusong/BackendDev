#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :todolist.py
@说明        :用户操作清单
@时间        :2023/02/11 15:59:05
@作者        :seanliu
'''

from sqlalchemy.orm import Session
from db import models,schemas

#用户通过用户id获取用户的清单数量
def get_user_todolist_count_by_id(db: Session, user_id: int):
    return db.query(models.TodoList).filter(models.TodoList.user_id == user_id).count()

#用户通过用户id分页获取用户的清单
def get_user_todolist_by_id_and_page(db: Session, user_id: int, page: int, page_size: int):
    return db.query(models.TodoList).filter(models.TodoList.user_id == user_id).offset((page - 1) * page_size).limit(page_size).all()
    

#用户通过用户id获取用户的清单
def get_user_todolist_by_id(db: Session, user_id: int):
    return db.query(models.TodoList).filter(models.TodoList.user_id == user_id).all()

#用户修改清单
def update_user_todolist(db: Session, user_id: int, todolist: schemas.CreateTodoList):
    db.query(models.TodoList).filter(models.TodoList.user_id == user_id).update(todolist.dict())
    db.commit()

#用户创建清单
def create_user_todolist(db: Session, todolist: schemas.CreateTodoList):
    db_todolist = models.TodoList(**todolist.dict())
    db.add(db_todolist)
    db.commit()
    db.refresh(db_todolist)
    return db_todolist

#用户删除清单
def delete_user_todolist(db: Session, user_id: int):
    db.query(models.TodoList).filter(models.TodoList.user_id == user_id).delete()
    db.commit()


# Path: app\crud\user\todolist.py