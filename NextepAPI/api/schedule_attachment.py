#!/usr/bin/python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas


# 创建日程附件
def create(request: schemas.ScheduleAttachment, db: Session):
    new_schedule_attachment = models.ScheduleAttachment(
        schedule_id=request.schedule_id,
        attachment_id=request.attachment_id,
    )
    db.add(new_schedule_attachment)
    db.commit()
    db.refresh(new_schedule_attachment)
    return new_schedule_attachment


# 获取所有日程附件 for admin
def get_all(db: Session):
    return db.query(models.ScheduleAttachment).all()


# 根据id获取日程附件
def get_by_id(id: int, db: Session):
    return db.query(models.ScheduleAttachment).filter(
        models.ScheduleAttachment.id == id).first()


# 根据日程id获取日程附件
def get_by_schedule_id(schedule_id: int, db: Session):
    return db.query(models.ScheduleAttachment).filter(
        models.ScheduleAttachment.schedule_id == schedule_id).all()


# 删除日程附件
def delete(id: int, db: Session):
    schedule_attachment = db.query(
        models.ScheduleAttachment).filter(models.ScheduleAttachment.id == id)
    if not schedule_attachment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ScheduleAttachment with the id {id} is not available")
    schedule_attachment.delete(synchronize_session=False)
    db.commit()
    return 'done delete schedule_attachment'


# 根据日程id删除日程附件
def delete_by_schedule_id(schedule_id: int, db: Session):
    schedule_attachment = db.query(models.ScheduleAttachment).filter(
        models.ScheduleAttachment.schedule_id == schedule_id)
    if not schedule_attachment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=
            f"ScheduleAttachment with the schedule_id {schedule_id} is not available"
        )
    schedule_attachment.delete(synchronize_session=False)
    db.commit()
    return 'done delete  schedules    schedule_attachment   '