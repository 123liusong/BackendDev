#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@文件        :admin.py
@说明        :管理员
@时间        :2023/02/11 17:00:28
@作者        :seanliu
"""

from sqlalchemy.orm import Session
from db import models, schemas

# 查询

"""总表-分页"""


# 用户列表
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# 团队列表
def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()


# 文件列表
def get_files(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.File).offset(skip).limit(limit).all()


# 日志列表
def get_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Log).offset(skip).limit(limit).all()


# md文件列表
def get_md_files(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.MarkdownFile).offset(skip).limit(limit).all()
        + db.query(models.MarkdownFile).offset(skip).limit(limit).all()
    )


# 清单列表
def get_lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TodoList).offset(skip).limit(limit).all()


"""总表计数"""


# 总用户数量
def get_users_count(db: Session):
    return db.query(models.User).count()


# 总文件数量
def get_files_count(db: Session):
    return db.query(models.File).count()


# 总团队数量
def get_teams_count(db: Session):
    return db.query(models.Team).count()


# 总日志数量
def get_logs_count(db: Session):
    return db.query(models.Log).count()


# 总md文件数量
def get_md_files_count(db: Session):
    return db.query(models.MarkdownFile).count() + db.query(models.MarkdownFile).count()


# 总清单数量
def get_lists_count(db: Session):
    return db.query(models.TodoList).count()


"""团队信息"""


# 某团队信息
def get_team_by_team_id(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()


# 某团队成员数量
def get_team_users_count_by_team_id(db: Session, team_id: int):
    return (
        db.query(models.TeamMember).filter(models.TeamMember.team_id == team_id).count()
    )


# 某团队文件数量
def get_team_files_count_by_team_id(db: Session, team_id: int):
    return db.query(models.File).filter(models.File.team_id == team_id).count()


# 某团队md文件数量
def get_team_md_files_count_by_team_id(db: Session, team_id: int):
    return (
        db.query(models.MarkdownFile)
        .filter(models.MarkdownFile.team_id == team_id)
        .count()
    )


# 某团队清单数量
def get_team_lists_count_by_team_id(db: Session, team_id: int):
    return db.query(models.TodoList).filter(models.TodoList.team_id == team_id).count()


"""用户信息"""


# 某用户信息
def get_user_by_user_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# 某用户团队数量
def get_user_teams_count_by_user_id(db: Session, user_id: int):
    return (
        db.query(models.TeamMember).filter(models.TeamMember.user_id == user_id).count()
    )


# 某用户文件数量
def get_user_files_count_by_user_id(db: Session, user_id: int):
    return db.query(models.File).filter(models.File.user_id == user_id).count()


# 某用户md文件数量
def get_user_md_files_count_by_user_id(db: Session, user_id: int):
    return (
        db.query(models.MarkdownFile)
        .filter(models.MarkdownFile.user_id == user_id)
        .count()
    )


# 某用户清单数量
def get_user_lists_count_by_user_id(db: Session, user_id: int):
    return db.query(models.TodoList).filter(models.TodoList.user_id == user_id).count()


# 某用户日志数量
def get_user_logs_count_by_user_id(db: Session, user_id: int):
    return db.query(models.Log).filter(models.Log.user_id == user_id).count()


# 增加 - 一般不用


# 添加团队
def create_team(db: Session, team: schemas.CreateTeam):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


# 添加文件
def create_file(db: Session, file: schemas.CreateFile):
    db_file = models.File(**file.dict())
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file


# 添加日志 - 不单独使用
def create_log(db: Session, log: schemas.CreateLog):
    db_log = models.Log(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


# 添加用户
def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 添加团队成员
def create_team_member(db: Session, team_member: schemas.CreateTeamMember):
    db_team_member = models.TeamMember(**team_member.dict())
    db.add(db_team_member)
    db.commit()
    db.refresh(db_team_member)
    return db_team_member


# 添加md文件
def create_md_file(db: Session, md_file: schemas.CreateMdFile):
    db_md_file = models.MarkdownFile(**md_file.dict())
    db.add(db_md_file)
    db.commit()
    db.refresh(db_md_file)
    return db_md_file


# 删除 - 仅限删除自己的文件，团队文件需要团队成员权限，admin权限可以删除任何文件


# 删除团队
def delete_team(db: Session, team_id: int):
    db.query(models.Team).filter(models.Team.id == team_id).delete()
    db.commit()


# 删除文件
def delete_file(db: Session, file_id: int):
    db.query(models.File).filter(models.File.id == file_id).delete()
    db.commit()


# 删除团队成员
def delete_team_member(db: Session, team_member_id: int):
    db.query(models.TeamMember).filter(models.TeamMember.id == team_member_id).delete()
    db.commit()


# 删除md文件
def delete_md_file(db: Session, md_file_id: int):
    db.query(models.MarkdownFile).filter(models.MarkdownFile.id == md_file_id).delete()
    db.commit()


# 删除用户
def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()


# 删除清单
def delete_list(db: Session, list_id: int):
    db.query(models.TodoList).filter(models.TodoList.id == list_id).delete()
    db.commit()


# 修改 - admin权限可以修改任何除日志外事务


# 修改团队
def update_team(db: Session, team: schemas.UpdateTeam):
    db.query(models.Team).filter(models.Team.id == team.id).update(team.dict())
    db.commit()


# 修改文件
def update_file(db: Session, file: schemas.UpdateFile):
    db.query(models.File).filter(models.File.id == file.id).update(file.dict())
    db.commit()


# 修改md文件
def update_md_file(db: Session, md_file: schemas.UpdateMdFile):
    db.query(models.MarkdownFile).filter(models.MarkdownFile.id == md_file.id).update(
        md_file.dict()
    )
    db.commit()


# 修改用户
def update_user(db: Session, user: schemas.UpdateUser):
    db.query(models.User).filter(models.User.id == user.id).update(user.dict())
    db.commit()


# 修改清单
def update_list(db: Session, list: schemas.UpdateList):
    db.query(models.TodoList).filter(models.TodoList.id == list.id).update(list.dict())
    db.commit()


# 修改用户
def update_user(db: Session, user: schemas.UpdateUser):
    db.query(models.User).filter(models.User.id == user.id).update(user.dict())
    db.commit()


# Path: app\crud\admin\admin.py
