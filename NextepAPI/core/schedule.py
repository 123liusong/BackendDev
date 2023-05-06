#!/usr/bin/python3

from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api import schedule
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user
from fastapi.responses import StreamingResponse

from io import BytesIO
import xlsxwriter
import time

router = APIRouter(tags=["Schedules"], prefix="/schedule")
get_db = configuration.get_db

from api import user


# 获取所有日程 用于测试
@router.get("/get_all", response_model=List[schemas.ShowSchedule])
def get_all_schedules(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule.get_all(db)


# 创建日程
@router.post("/add", status_code=status.HTTP_201_CREATED)
def create(
        request: schemas.Schedule,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule.create(request, db)


#开始时间或结束时间在某个时间段内的日程
@router.get("/get_by_time/{start_time}/{end_time}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowSchedule])
def get_schedule_by_time(
        start_time: str,
        end_time: str,
        id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule.get_by_start_or_end(start_time, end_time, db, id)


# 根据id获取日程
@router.get("/get/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowSchedule)
def get_schedule_by_id(
        id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule.show(id, db)


@router.get("/user/{id}/personal/schedule",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowSchedule])
def get_schedule_by_user(
        id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule.get_all_by_creator_id_and_personal(id, db)


@router.get("/user/{id}/team/schedule",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowSchedule])
def get_schedule_by_team(
        id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    #获取用户信息
    user = user.show(id, db)
    #获取用户所在的团队
    teams = user.team
    #循环获取团队的日程
    team_schedule = []
    for i in teams:
        schedule = team.get_schedule_by_team(i.id, db)
        team_schedule.append(schedule)
    return team_schedule


# 导出日程,根据用户id、开始时间、结束时间、日程级别数组
@router.get("/export/{id}/{start_time}/{end_time}/{level}",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowSchedule])
def export_schedule(
        id: int,
        start_time: str,
        end_time: str,
        level: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule.get_by_user_start_end_level(start_time, end_time, level,
                                                db, id)


# 根据用户id、开始时间、结束时间、日程级别数组的数组生成文件并返回
@router.get("/export/file/{id}/{start_time}/{end_time}/{level}")
def export_schedule_file(
        id: int,
        start_time: str,
        end_time: str,
        level: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    schedules = schedule.get_by_user_start_end_level(start_time, end_time,
                                                     level, db, id)
    output =BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()    
    worksheet.write(0, 0, "日程名称")
    worksheet.write(0, 1, "开始时间")
    worksheet.write(0, 2, "结束时间")
    worksheet.write(0, 3, "日程级别")
    worksheet.write(0, 4, "创建者")
    worksheet.write(0, 5, "团队")    

    for i in range(len(schedules)):
        worksheet.write(i+1, 0, schedules[i].title)
        worksheet.write(i+1, 1, schedules[i].start_time)
        worksheet.write(i+1, 2, schedules[i].end_time)
        worksheet.write(i+1, 3, schedules[i].level)
        worksheet.write(i+1, 5, schedules[i].creator_id)
        worksheet.write(i+1, 6, schedules[i].team_id)
    #生成文件
    workbook.close()
    output.seek(0)

    headers ={
        'Content-Disposition': 'attachment; filename="schedule.xlsx"'
    }
    return StreamingResponse(output, headers=headers)


@router.get('/team/{id}/schedule',
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowSchedule])
def get_team_all_schrdule(
        id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    return schedule.get_all_by_team_id(id, db)


# 根据id删除日程
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_schedule(
        id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):

    return schedule.delete(id, db)


# 根据id更新日程
@router.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_schedule(
        id: int,
        request: schemas.ScheduleUpdate,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    """
    Update a schedule by id

    Args:
        id (int): Schedule id
        request (schemas.Schedule): Schedule to update
        db (Session, optional): Database session. Defaults to Depends(get_db).
        current_user (schemas.User, optional): Current user. Defaults to Depends(get_current_user).

    Returns:
        schemas.Schedule: Updated schedule
    """
    return schedule.update(id, request, db)
