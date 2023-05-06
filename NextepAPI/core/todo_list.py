from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api import todo_list
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["TodoList"], prefix="/todo_list")
get_db = configuration.get_db


# 获取所有待办事项
@router.get("/get_all", response_model=List[schemas.ShowTodoList])
def get_all_todo_list(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return todo_list.get_all(db)


# 创建待办事项
@router.post("/add", status_code=status.HTTP_201_CREATED)
def create(
        request: schemas.TodoList,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return todo_list.create(request, db)


# 根据id获取待办事项
@router.get("/get/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowTodoList)
def get_todo_list_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return todo_list.show(id, db)


# 根据id删除待办事项
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_list_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return todo_list.delete(id, db)


# 根据id更新待办事项
@router.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_todo_list_by_id(
        id: int,
        request: schemas.TodoList,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return todo_list.update(id, request, db)


# 根据用户id获取待办事项
@router.get("/user/{id}/todolist",
            response_model=List[schemas.ShowTodoList],
            status_code=status.HTTP_200_OK)
def get_user_todo_list(
        id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    return todo_list.get_all_by_user_id_and_personal(id, db)



# 根据团队id获取待办事项
@router.get("/team/{id}/todolist",
            response_model=List[schemas.ShowTodoList],
            status_code=status.HTTP_200_OK)
def get_team_todo_list(
        id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    return todo_list.get_all_by_team_id(id, db)


