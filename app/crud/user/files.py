#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :files.py
@说明        :用户操作文件
@时间        :2023/02/11 16:02:35
@作者        :seanliu
'''

from sqlalchemy.orm import Session
from db import models,schemas
#用户通过用户id获取用户的文件数量
def get_user_files_count_by_id(db: Session, user_id: int):
    return db.query(models.File).filter(models.File.user_id == user_id).count()

#用户通过用户id分页获取用户的文件
def get_user_files_by_id_page(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.File).filter(models.File.user_id == user_id).offset(skip).limit(limit).all()


#用户通过用户id获取用户的文件
def get_user_files_by_id(db: Session, user_id: int):
    return db.query(models.File).filter(models.File.user_id == user_id).all()

#用户修改文件
def update_user_files(db: Session, user_id: int, files: schemas.CreateFile):
    db.query(models.File).filter(models.File.user_id == user_id).update(files.dict())
    db.commit()

#用户创建文件
def create_user_files(db: Session, files: schemas.CreateFile):
    db_files = models.File(**files.dict())
    db.add(db_files)
    db.commit()
    db.refresh(db_files)
    return db_files

#用户删除文件
def delete_user_files(db: Session, user_id: int):
    db.query(models.File).filter(models.File.user_id == user_id).delete()
    db.commit()



# Path: app\crud\user\files.py