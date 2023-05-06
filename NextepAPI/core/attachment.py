from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api import attachment
from api import schedule
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["Attachments"], prefix="/attachment")
get_db = configuration.get_db


# 获取所有附件
@router.get("get_all/", response_model=List[schemas.ShowAttachment])
def get_all_attachments(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return attachment.get_all(db)


# 创建附件
@router.post("/add", status_code=status.HTTP_201_CREATED)
def create(
        request: schemas.Attachment,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return attachment.create(request, db)


# 根据id获取附件
@router.get("/get/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowAttachment)
def get_attachment_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return attachment.get_by_id(id, db)


# 根据id删除附件
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_attachment_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return attachment.delete(id, db)


# 根据id更新附件
@router.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_attachment_by_id(
        id: int,
        request: schemas.Attachment,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return attachment.update(id, request, db)


@router.get("/user/{id}/attachment",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowAttachment])
def get_attachment_by_user(
        id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return attachment.get_by_creator_id_and_personal(id, db)


# 团队附件
@router.get("/team/{id}/attachment",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowAttachment])
def get_attachment_by_team(
        id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return attachment.get_by_team_id(id, db)
    