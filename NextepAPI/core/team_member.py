from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api import team_member
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["TeamMember"], prefix="/team_member")
get_db = configuration.get_db


# 获取所有团队成员
@router.get("/get_all", response_model=List[schemas.ShowTeamMember])
def get_all_team_member(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.get_all(db)


# 创建团队成员
@router.post("/add", status_code=status.HTTP_201_CREATED)
def create(
        request: schemas.TeamMember,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.create(request, db)


# 根据id获取团队成员
@router.get("/get/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowTeamMember)
def get_team_member_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.get_by_id(id, db)


# 根据team_id获取团队成员
@router.get("/get_by_team_id/{team_id}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowTeamMember])
def get_team_member_by_team_id(
        team_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.get_by_team_id(team_id, db)


# 根据user_id获取团队
@router.get("/get_by_user_id/{user_id}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowTeamMember])
def get_team_member_by_user_id(
        user_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.get_by_member_id(user_id, db)


# 根据记录id删除团队成员
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_team_member_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.delete(id, db)


# 根据team_id删除所有团队成员
@router.delete("/delete_by_team_id/{team_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_team_member_by_team_id(
        team_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.delete_by_team_id(team_id, db)


# 根据user_id删除所有团队
@router.delete("/delete_by_user_id/{user_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_team_member_by_user_id(
        user_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.delete_by_member_id(user_id, db)


# 根据team_id和user_id删除团队成员
@router.delete("/delete_by_team_id_and_user_id/{team_id}/{user_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_team_member_by_team_id_and_user_id(
        team_id: int,
        user_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.delete_by_member_id_and_team_id(team_id, user_id, db)


# 根据id更新团队成员
@router.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_team_member_by_id(
        id: int,
        request: schemas.TeamMemberUpdate,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return team_member.update(id, request, db)
