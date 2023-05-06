#!/usr/bin/python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas


# 获取所有团队 for admin
def get_all(db: Session):
    return db.query(models.Team).all()


# 根据id获取团队
def get_by_id(id: int, db: Session):
    return db.query(models.Team).filter(models.Team.id == id).first()


# 根据队长id获取团队
def get_by_leader_id(leader_id: int, db: Session):
    return db.query(
        models.Team).filter(models.Team.leader_id == leader_id).all()


# 跟新团队信息
def update(id: int, request: schemas.Team, db: Session):
    team = db.query(models.Team).filter(models.Team.id == id)
    if not team.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Team with the id {id} is not available")
    team.update(request)
    db.commit()
    return 'done'


# 删除团队
def delete(id: int, db: Session):
    team = db.query(models.Team).filter(models.Team.id == id)
    if not team.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Team with the id {id} is not available")
    team.delete(synchronize_session=False)
    db.commit()
    return 'done'


# 创建团队
def create(request: schemas.Team, db: Session):
    new_team = models.Team(
        title=request.title,
        body=request.body,
        leader_id=request.leader_id,
    )
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team
