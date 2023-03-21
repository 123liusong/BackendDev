#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@文件        :user_api.py
@说明        :用户登录、注册、查看、修改和注销  api
@时间        :2023/02/11 15:02:21
@作者        :seanliu
"""
import time

from db import models, schemas
from crud.user import user as crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal, Base, engine

user_api = APIRouter()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 用户注册
@user_api.post("/user/register")
def user_register(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        return HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# 创建用户token - 注册时
@user_api.post("/user/token/create")
def user_token(user_token: schemas.CreateToken, db: Session = Depends(get_db)):
    return crud.create_user_token(db=db, user=db_user)


# 用户登录
@user_api.post("/user/login")
def user_login(user: schemas.LoginUser, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user is None:
        return HTTPException(status_code=400, detail="Email not registered")
    if db_user.password != user.password:
        return HTTPException(status_code=400, detail="Password error")
    return True


# 更新用户token - 登录时
@user_api.post("/user/token/update")
def user_token(
    user_token: schemas.UpdateToken, user_id:int, db: Session = Depends(get_db)
):
    return crud.update_user_token(db, user_id, user_token)

# token过时和不匹配
def user_token_timeout(token: schemas.UpdateToken, db: Session = Depends(get_db)):
    db_user_token = crud.get_user_token_by_token(db, token=token.token)
    if db_user_token is None:
        return HTTPException(status_code=400, detail="Token error")
    if int(time.mktime(db_user_token.updated_at)) + 3600 < time.time():
        return HTTPException(status_code=400, detail="Token timeout")
    return True


# 用户查看
@user_api.get("/user/info")
def user_info(token: schemas.UpdateToken,token_local:str, db: Session = Depends(get_db)):
    #对比本地和服务器token
    if user_token_timeout(token_local, db):
        return crud.get_user_by_token(db, token=token.token)
# todo 本地token过时，重新获取token

# 用户修改
@user_api.put("/user/update")
def user_update(user: schemas.UpdateUser, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user is None:
        return HTTPException(status_code=400, detail="Email not registered")
    return crud.update_user(db=db, user=user)


# 用户删除
@user_api.delete("/user/delete")
def user_delete(user: schemas.DeleteUser, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user is None:
        return HTTPException(status_code=400, detail="Email not registered")
    if db_user.password != user.password:
        return HTTPException(status_code=400, detail="Password error")
    return crud.delete_user(db=db, user=db_user)
