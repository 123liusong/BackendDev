#!/usr/bin/python3

from typing import List
import re
from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from schema.oa2 import get_current_user

from api import user
from database import configuration
from schema import schemas

router = APIRouter(tags=["Users"], prefix="/users")
get_db = configuration.get_db


@router.post("/",
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # 密码格式判断字母加数字
    if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                    request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Password must be at least 8 characters and contain at least one letter and one number")
    # 邮箱格式判断
    if not re.match(r"[^@]+@[^@]+\.[^@]+", request.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid email")
    return user.create(request, db)


@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(get_db)):

    return user.get_all(db)


@router.get("/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):

    return user.show(id, db)


# update user
@router.put("/{id}",
            status_code=status.HTTP_202_ACCEPTED,
            response_model=schemas.ShowUser)
def update_user(id: int, request: schemas.User, db: Session = Depends(get_db)):

    return user.update(id, request, db)