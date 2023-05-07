from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api import message
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user
from fastapi.responses import StreamingResponse

#消息API
router = APIRouter(tags=["Messages"], prefix="/message")
get_db = configuration.get_db

from api import user

# 消息创建
@router.post("/add", status_code=status.HTTP_201_CREATED)
def create(
        request: schemas.MessageCreate,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return message.create(request, db)


# 获取所有消息 用于测试
@router.get("/get_all", response_model=List[schemas.ShowMessage])
def get_all_messages(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return message.get_all(db)

# 删除消息
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
        id,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    return message.destroy(id, db)

# 修改消息状态
@router.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
        id,
        request: schemas.MessageCreate,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    return message.update_state(id, request, db)

# 消息查询接收者id
@router.get("/show_by_to_user_id/{to_user_id}", response_model=List[schemas.ShowMessage])
def show_by_to_user_id(
        to_user_id,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    return message.show_by_to_user_id(to_user_id, db)

# 消息查询创建者id
@router.get("/show_by_creator_id/{creator_id}", response_model=List[schemas.ShowMessage])
def show_by_creator_id(
        creator_id,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    return message.show_by_creator_id(creator_id, db)

# 消息查询接收者id和消息状态
@router.get("/show_by_to_user_id_and_state/{to_user_id}/{state}", response_model=List[schemas.ShowMessage]) 
def show_by_to_user_id_and_state(
        to_user_id,
        state,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    return message.show_by_to_user_id_and_state(to_user_id, state, db)

# 消息查询创建者id和消息状态
@router.get("/show_by_creator_id_and_state/{creator_id}/{state}", response_model=List[schemas.ShowMessage])
def show_by_creator_id_and_state(
        creator_id,
        state,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    return message.show_by_creator_id_and_state(creator_id, state, db)

