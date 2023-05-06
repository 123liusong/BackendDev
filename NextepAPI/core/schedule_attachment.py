from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api import schedule_attachment
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["ScheduleAttachment"], prefix="/schedule_attachment")
get_db = configuration.get_db


# 获取所有日程附件
@router.get("/get_all", response_model=List[schemas.ShowScheduleAttachment])
def get_all_schedule_attachment(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_attachment.get_all(db)


# 创建日程附件
@router.post("/add", status_code=status.HTTP_201_CREATED)
def create(
        request: schemas.ScheduleAttachmentCreate,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_attachment.create(request, db)



# 根据id获取日程附件
@router.get("/get/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowScheduleAttachment)
def get_schedule_attachment_by_id(

        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_attachment.get_by_id(id, db)

# 根据schedule_id获取日程附件
@router.get("/get_by_schedule_id/{schedule_id}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowScheduleAttachment])
def get_schedule_attachment_by_schedule_id(
        schedule_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_attachment.get_by_schedule_id(schedule_id, db)

# 根据id删除日程附件
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_schedule_attachment_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_attachment.delete(id, db)


# 根据schedule_id删除日程附件
@router.delete("/delete_by_schedule_id/{schedule_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_schedule_attachment_by_schedule_id(
        schedule_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_attachment.delete_by_schedule_id(schedule_id, db)