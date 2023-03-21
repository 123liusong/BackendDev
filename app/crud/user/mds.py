#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :mds.py
@说明        :用户操作md文件    
@时间        :2023/02/11 16:01:41
@作者        :seanliu
'''


from sqlalchemy.orm import Session
from db import models,schemas
#用户通过用户id获取用户的md文件数量
def get_user_mds_count_by_id(db: Session, user_id: int):
    return db.query(models.UserMds).filter(models.UserMds.user_id == user_id).count()

#用户通过用户id分页获取用户的md文件
def get_user_mds_by_id_page(db: Session, user_id: int, page: int, page_size: int):
    return db.query(models.UserMds).filter(models.UserMds.user_id == user_id).offset((page-1)*page_size).limit(page_size).all()


#用户通过用户id获取用户的md文件
def get_user_mds_by_id(db: Session, user_id: int):
    return db.query(models.UserMds).filter(models.UserMds.user_id == user_id).all()

#用户修改md文件
def update_user_mds(db: Session, user_id: int, mds: schemas.CreateUserMds):
    db.query(models.UserMds).filter(models.UserMds.user_id == user_id).update(mds.dict())
    db.commit()

#用户创建md文件
def create_user_mds(db: Session, mds: schemas.CreateUserMds):
    db_mds = models.UserMds(**mds.dict())
    db.add(db_mds)
    db.commit()
    db.refresh(db_mds)
    return db_mds

#用户删除md文件
def delete_user_mds(db: Session, user_id: int):
    db.query(models.UserMds).filter(models.UserMds.user_id == user_id).delete()
    db.commit()


# Path: app\crud\user\mds.py

