from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas


# 获取所有消息 用于测试
def get_all(db: Session):
    messages = db.query(models.Message).all()
    return messages
    

# 消息创建
def create(request: schemas.MessageCreate, db: Session):
    new_message = models.Message(**request.dict())
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


# 消息查询
def show(id: int, db: Session):
    message = db.query(models.Message).filter(models.Message.id == id).first()
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Message with id {id} is not available")
    return message

# 消息查询通过接收者id
def show_by_to_user_id(to_user_id: int, db: Session):
    message = db.query(models.Message).filter(models.Message.to_user_id == to_user_id).all()
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Message with to_user_id {to_user_id} is not available")
    return message

# 消息查询通过创建者id
def show_by_creator_id(creator_id: int, db: Session):
    message = db.query(models.Message).filter(models.Message.creator_id == creator_id).all()
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Message with creator_id {creator_id} is not available")
    return message

# 消息查询通过接收者id和消息状态
def show_by_to_user_id_and_state(to_user_id: int, state: int, db: Session):
    message = db.query(models.Message).filter(models.Message.to_user_id == to_user_id).filter(models.Message.state == state).all()
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Message with to_user_id {to_user_id} and state {state} is not available")
    return message

# 消息查询通过创建者id和消息状态
def show_by_creator_id_and_state(creator_id: int, state: int, db: Session):
    message = db.query(models.Message).filter(models.Message.creator_id == creator_id).filter(models.Message.state == state).all()
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Message with creator_id {creator_id} and state {state} is not available")
    return message

#跟新消息状态
def update_state(id: int, request: schemas.MessageUpdate, db: Session):
    message = db.query(models.Message).filter(models.Message.id == id)
    if not message.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Message with id {id} is not available")
    message.update(request.dict())
    db.commit()
    return 'update success'

# 删除消息
def destroy(id: int, db: Session):
    message = db.query(models.Message).filter(models.Message.id == id)
    if not message.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Message with id {id} is not available")
    message.delete(synchronize_session=False)
    db.commit()
    return 'delete success'
