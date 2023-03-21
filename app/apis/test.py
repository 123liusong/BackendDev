#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :test.py
@说明        :
@时间        :2023/02/11 12:02:59
@作者        :seanliu
'''

# from db.models import User, UserToken
# from fastapi import FastAPI, Depends,APIRouter
# from sqlalchemy.orm import Session
# from db.schemas import CreateUser
# from crud.user import create_user, get_user_by_name, get_user_by_email

# 测试数据库连接
# from db.database import SessionLocal, Base, engine


# test_app = APIRouter()
# 测试创建表
# Base.metadata.create_all(engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# 测试插入数据


# @test_app.post("/test/create")
# def test_create(user:CreateUser,db: Session = Depends(get_db)):
#     db_user = get_user_by_email(db, email=user.email)
#     if db_user:
#         return HTTPException(status_code=400, detail="Email already registered")
#     return create_user(db=db, user=user)
