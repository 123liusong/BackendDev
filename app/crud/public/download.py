#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@文件        :download.py
@说明        :公用下载
@时间        :2023/02/11 16:35:55
@作者        :seanliu
"""

from fastapi import HTTPException, status
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db import models, schemas
from app.core import config
import os


# 获取文件列表
def get_files(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.File).offset(skip).limit(limit).all()


# 获取文件数量
def get_files_count(db: Session):
    return db.query(models.File).count()


# 下载文件
def download_file(db: Session, file_id: int):
    file = db.query(models.File).filter(models.File.id == file_id).first()
    if file:
        file_path = os.path.join(config.UPLOAD_PATH, file.file_name)
        if os.path.exists(file_path):
            return FileResponse(
                file_path, filename=file.file_name, media_type=file.file_type
            )
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="文件不存在")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="文件不存在")


# Path: app\crud\public\download.py
