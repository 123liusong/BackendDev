from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api import team
from database import configuration
from schema import schemas


router = APIRouter(tags=["Teams"], prefix="/teams")
get_db = configuration.get_db


# GET ALL TEAMS
@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowTeam])
def get_teams(db: Session = Depends(get_db)):
    return team.get_all(db)

# GET TEAM BY ID
@router.get("/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowTeam)
def get_team_by_id(id: int, db: Session = Depends(get_db)):
    return team.get_by_id(id, db)


# CREATE TEAM
@router.post("/",
                status_code=status.HTTP_201_CREATED,
                response_model=schemas.ShowTeam)
def create_team(request: schemas.Team, db: Session = Depends(get_db)):
    return team.create(request, db)

# update team
@router.put("/{id}",
            status_code=status.HTTP_202_ACCEPTED,
            response_model=schemas.ShowTeam)
def update_team(id: int, request: schemas.Team, db: Session = Depends(get_db)):
    return team.update(id, request, db)

# delete team
@router.delete("/{id}",
                status_code=status.HTTP_204_NO_CONTENT)
def delete_team(id: int, db: Session = Depends(get_db)):
    return team.delete(id, db)


# #!/usr/bin/python3
