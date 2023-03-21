
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@文件        :database.py
@说明        :数据库连接
@时间        :2023/02/11 11:55:06
@作者        :seanliu
"""

# sqlalchemy 连接postgresql数据库
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

DATABASE_URI = "sqlite:///test_db_sqlite.db"
# DATABASE_URI = "postgresql://postgres:admin123@localhost:5432/cms"
engine = create_engine(DATABASE_URI, echo=True)

# 创建会话
SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=True
)

# 创建基类
Base = declarative_base()
