#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :user_dao.py
@说明        :用户操作
@时间        :2023/02/11 13:03:37
@作者        :seanliu
'''

# # 数据库操作
# from sqlalchemy.orm import Session

# from db.models import User, UserToken
# from db.schemas import CreateUser

# def get_user_by_id(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()

# def get_user_by_name(db: Session, name: str):
#     return db.query(User).filter(User.name == name).first()

# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()

# #创建用户
# def create_user(db: Session, user: CreateUser):
#     db_user = User(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


from sqlalchemy.orm import Session
from db import models,schemas

#用户通过id获取用户
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#用户通过email获取用户
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# #通过token获取用户
# def get_user_by_token(db: Session, token: str):
#     user_id = db.query(models.User).filter(models.User.token == token).first().user_id
#     return db.query(models.User).filter(models.User.id == user_id).first()

#用户创建用户
def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user  

#用户删除用户 
def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()

#用户更新用户
def update_user(db: Session, user_id: int, user: schemas.CreateUser):
    db.query(models.User).filter(models.User.id == user_id).update(user.dict())
    db.commit()
    
#创建用户token
def create_user_token(db: Session, user_token: schemas.CreateToken):
    db_user_token = models.UserToken(**user_token.dict())
    db.add(db_user_token)
    db.commit()
    db.refresh(db_user_token)
    return db_user_token

#通过用户id获取用户token
def get_user_token_by_user_id(db: Session, user_id: int):
    return db.query(models.UserToken).filter(models.UserToken.user_id == user_id).first()



#通过token获取用户token
def get_user_token_by_token(db: Session, token: str):
    return db.query(models.UserToken).filter(models.UserToken.token == token).first()

#修改用户token
def update_user_token(db: Session, user_id: int(), user_token: schemas.UpdateToken):
    db.query(models.UserToken).filter(models.UserToken.user_id == user_id).update(user_token.dict())
    db.commit()

#删除用户token
def delete_user_token(db: Session, user_id: int):
    db.query(models.UserToken).filter(models.UserToken.user_id == user_id).delete()
    db.commit()

# Path: app\crud\user\user.py