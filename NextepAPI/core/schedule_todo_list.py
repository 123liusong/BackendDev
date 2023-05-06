from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api import schedule_todo_list

from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["ScheduleTodoList"], prefix="/schedule_todo_list")
get_db = configuration.get_db


# 获取所有日程子清单
@router.get("/get_all", response_model=List[schemas.ShowScheduleTodoList])
def get_all_schedule_todo_list(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_todo_list.get_all(db)


# 创建日程子清单
@router.post("/add", status_code=status.HTTP_201_CREATED)
def create(
        request: schemas.ScheduleTodoListCreate,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_todo_list.create(request, db)


# 根据id获取日程子清单
@router.get("/get/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowScheduleTodoList)
def get_schedule_todo_list_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_todo_list.get_by_id(id, db)


# 根据schedule_id获取日程子清单
@router.get("/get_by_schedule_id/{schedule_id}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowScheduleTodoList])
def get_schedule_todo_list_by_schedule_id(
        schedule_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_todo_list.get_by_schedule_id(schedule_id, db)


# 根据id删除日程子清单
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_schedule_todo_list_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_todo_list.delete(id, db)




# 根据schedule_id删除日程子清单
@router.delete("/delete_by_schedule_id/{schedule_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_schedule_todo_list_by_schedule_id(
        schedule_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule_todo_list.delete_by_schedule_id(schedule_id, db)
