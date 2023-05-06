from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api import log
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["Logs"], prefix="/log")
get_db = configuration.get_db


# 获取所有日志 用于测试
@router.get("/get_all", response_model=List[schemas.ShowLog])
def get_all_logs(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return log.get_all(db)


# 创建日志
@router.post("/add", status_code=status.HTTP_201_CREATED)
def create(
        request: schemas.Log,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return log.create(request, db)


# 根据id获取日志
@router.get("/get/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowLog)
def get_log_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return log.get_by_id(id, db)


# 根据类型获取日志
@router.get("/get_by_type/{type}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowLog])
def get_log_by_type(
        type: str,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return log.get_by_type(type, db)


# 根据时间段获取日志
@router.get("/get_by_time/{start_time}/{end_time}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowLog])
def get_log_by_time(
        start_time: str,
        end_time: str,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return log.get_by_time(start_time, end_time, db)
