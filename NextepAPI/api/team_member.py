#!/usr/bin/python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas


# 创建团队成员
def create(request: schemas.TeamMember, db: Session):
    new_team_member = models.TeamMember(
        team_id=request.team_id,
        member_id=request.member_id,
        alias=request.alias,
    )
    db.add(new_team_member)
    db.commit()
    db.refresh(new_team_member)
    return new_team_member


# 获取所有团队成员 for admin
def get_all(db: Session):
    return db.query(models.TeamMember).all()

# 根据id获取团队成员
def get_by_id(id: int, db: Session):
    return db.query(models.TeamMember).filter(
        models.TeamMember.id == id).first()

# 根据团队id获取成员
def get_by_team_id(team_id: int, db: Session):
    return db.query(models.TeamMember).filter(
        models.TeamMember.team_id == team_id).all()

# 根据成员id获取团队
def get_by_member_id(member_id: int, db: Session):
    return db.query(models.TeamMember).filter(
        models.TeamMember.member_id == member_id).all()

# 删除团队成员
def delete(id: int, db: Session):
    team_member = db.query(models.TeamMember).filter(
        models.TeamMember.id == id)
    if not team_member.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TeamMember with the id {id} is not available")
    team_member.delete(synchronize_session=False)
    db.commit()
    return 'done delete team_member'

# 跟新团队成员信息
def update(id: int, request: schemas.TeamMember, db: Session):
    team_member = db.query(models.TeamMember).filter(
        models.TeamMember.id == id)
    if not team_member.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TeamMember with the id {id} is not available")
    team_member.update(request)
    db.commit()
    return 'done update team_member'