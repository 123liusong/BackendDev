#!/usr/bin/python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas
from schema.hash import Hash


# Create attachment
def create(request: schemas.Attachment, db: Session):
    new_attachment = models.Attachment(
        name=request.name,
        path=request.path,
        creator_id=request.creator_id,
        team_id=request.team_id,
        type=request.type,
        size=request.size,
    )
    db.add(new_attachment)
    db.commit()
    db.refresh(new_attachment)
    return new_attachment


# Get all attachment for admin
def get_all(db: Session):
    attachment = db.query(models.Attachment).all()
    return attachment


# Get attachment by id
def get_by_id(id: int, db: Session):
    attachment = db.query(
        models.Attachment).filter(models.Attachment.id == id).first()
    if not attachment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attachment with the id {id} is not available")
    return attachment

# Get attachment by team id
def get_by_team_id(team_id: int, db: Session):
    attachment = db.query(
        models.Attachment).filter(models.Attachment.team_id == team_id).all()
    if not attachment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attachment with the team id {team_id} is not available")
    return attachment

# Get attachment by creator id
def get_by_creator_id(creator_id: int, db: Session):
    attachment = db.query(
        models.Attachment).filter(models.Attachment.creator_id == creator_id).all()
    if not attachment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attachment with the creator id {creator_id} is not available")
    return attachment

# 获取附件通过创建者id并且不是团队附件
def get_by_creator_id_and_personal(creator_id: int, db: Session):
    attachment = db.query(
        models.Attachment).filter(models.Attachment.creator_id == creator_id).filter(models.Attachment.team_id == 1).all()
    if not attachment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attachment with the creator id {creator_id} is not available")
    return attachment

# 获取附件通过创建者id并且是团队附件
def get_by_creator_id_and_team(creator_id: int, db: Session):
    attachment = db.query(
        models.Attachment).filter(models.Attachment.creator_id == creator_id).filter(models.Attachment.team_id != 1).all()
    if not attachment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attachment with the creator id {creator_id} is not available")
    return attachment



# Delete attachment by id
def delete(id: int, db: Session):
    attachment = db.query(models.Attachment).filter(models.Attachment.id == id)
    if not attachment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attachment with the id {id} is not available")
    attachment.delete(synchronize_session=False)
    db.commit()
    return 'done delete attachment'


# Update attachment by id
def update(id: int, request: schemas.Attachment, db: Session):
    attachment = db.query(models.Attachment).filter(models.Attachment.id == id)
    if not attachment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attachment with the id {id} is not available")
    attachment.update(request)
    db.commit()
    return 'updated attachment successfully' 
