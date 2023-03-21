#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@文件        :user.py
@说明        :模型
@时间        :2023/02/11 12:04:38
@作者        :seanliu
"""

from sqlalchemy import (
    Column,
    Float,
    Text,
    Integer,
    String,
    DateTime,
    Boolean,
    BigInteger,
    Date,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship

from db.database import Base


# 用户模型
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    name = Column(String(20), nullable=False)  # 用户名
    email = Column(String(50), nullable=False)  # 邮箱
    password = Column(String(100), nullable=False)  # 密码
    gender = Column(Integer, nullable=False)  # 性别 0:男 1:女
    is_active = Column(Boolean, default=True)  # 是否激活
    is_superuser = Column(Boolean, default=False)  # 是否超级管理员
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:禁用
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
# 包含的字段有 id,name,e

# 用户token模型
class UserToken(Base):
    __tablename__ = "user_token"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键
    token = Column(String(100), nullable=False)  # token
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"UserToken(id={self.id}, user_id={self.user_id}, token={self.token})"


# 团队模型
class Team(Base):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    name = Column(String(100), nullable=False)  # 团队名称
    description = Column(Text, nullable=False)  # 团队描述
    leader_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:禁用
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Team(id={self.id}, name={self.name}, leader_id={self.leader_id})"


# 文件模型
class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    name = Column(String(100), nullable=False)  # 文件名
    path = Column(String(100), nullable=False)  # 文件路径
    size = Column(Float, nullable=False)  # 文件大小
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:禁用
    is_user = Column(Boolean, default=False)  # 是否用户文件
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    is_team = Column(Boolean, default=False)  # 是否团队文件
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    is_public = Column(Boolean, default=False)  # 是否公开
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"File(id={self.id}, name={self.name}, path={self.path}, size={self.size}, state={self.state}, is_user={self.is_user}, user_id={self.user_id}, is_team={self.is_team}, team_id={self.team_id})"


# 日志模型
class Log(Base):
    __tablename__ = "log"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键
    ip = Column(String(20), nullable=False)  # ip地址
    method = Column(String(10), nullable=False)  # 请求方法
    path = Column(String(100), nullable=False)  # 请求路径
    status_code = Column(Integer, nullable=False)  # 状态码
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"Log(id={self.id}, user_id={self.user_id}, ip={self.ip}, method={self.method}, path={self.path}, status_code={self.status_code})"


# MarkdownFile模型
class MarkdownFile(Base):
    __tablename__ = "markdown_file"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    name = Column(String(100), nullable=False)  # 文件名
    path = Column(String(100), nullable=False)  # 文件路径
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:禁用
    is_user = Column(Boolean, default=False)  # 是否用户文件
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    is_team = Column(Boolean, default=False)  # 是否团队文件
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"MarkdownFile(id={self.id}, name={self.name}, path={self.path}, state={self.state}, is_user={self.is_user}, user_id={self.user_id}, is_team={self.is_team}, team_id={self.team_id})"


# 日程模型 1-n
class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    is_user = Column(Boolean, default=False)  # 是否用户日程
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    is_team = Column(Boolean, default=False)  # 是否团队日程
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    title = Column(String(100), nullable=False)  # 标题
    content = Column(String(100), nullable=False)  # 内容
    start_time = Column(DateTime, nullable=False)  # 开始时间
    end_time = Column(DateTime, nullable=False)  # 结束时间
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:禁用
    level = Column(Integer, nullable=False)  # 级别  0:普通 1:重要 2:紧急
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Schedule(id={self.id}, user_id={self.user_id}, title={self.title}, content={self.content}, start_time={self.start_time}, end_time={self.end_time}, annpexes={self.annpexes}, level={self.level})"


# 日程附件模型 n-n
class ScheduleAnnex(Base):
    __tablename__ = "schedule_annex"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    schedule_id = Column(Integer, ForeignKey("schedule.id"))  # 外键 关联schedule表
    markdown_file_id = Column(
        Integer, ForeignKey("markdown_file.id")
    )  # 外键 关联markdown_file表
    file_id = Column(Integer, ForeignKey("file.id"))  # 外键 关联file表
    todo_list_id = Column(Integer, ForeignKey("todo_list.id"))  # 外键 关联todo_list表
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"ScheduleAnnex(id={self.id}, schedule_id={self.schedule_id}, file_id={self.file_id})"


# 团队成员模型 n-n
class TeamMember(Base):
    __tablename__ = "team_member"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return (
            f"TeamMember(id={self.id}, team_id={self.team_id}, user_id={self.user_id})"
        )


# 团队文件模型 1-n
# class TeamFile(Base):
#     __tablename__ = "team_file"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
#     team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
#     file_id = Column(Integer, ForeignKey("file.id"))  # 外键 关联file表
#     created_at = Column(DateTime, default=func.now())

#     def __repr__(self):
#         return f"TeamFile(id={self.id}, team_id={self.team_id}, file_id={self.file_id})"


# 消息模型 n-n
class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    type = Column(Integer, nullable=False)  # 类型 0:系统消息 1:团队消息 2:个人消息
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    receive_user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    send_user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    content = Column(String(100), nullable=False)  # 内容
    state = Column(Integer, nullable=False)  # 状态 0:未读 1:已读
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"Message(id={self.id}, user_id={self.user_id}, content={self.content}, state={self.state})"


# 清单模型 1-n
class TodoList(Base):
    __tablename__ = "todo_list"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    is_user = Column(Boolean, default=False)  # 是否用户清单
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    is_team = Column(Boolean, default=False)  # 是否团队清单
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    title = Column(String(100), nullable=False)  # 标题
    description = Column(String(100), nullable=False)  # 描述
    number = Column(Integer, nullable=False)  # 数量
    type = Column(Integer, nullable=False)  # 类型
    state = Column(Integer, nullable=False)  # 状态 0:未完成 1:已完成
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"TodoList(id={self.id}, user_id={self.user_id}, title={self.title}, description={self.description}, number={self.number}, type={self.type}, state={self.state})"


# 团队聊天模型 1-n
class TeamChat(Base):
    __tablename__ = "team_chat"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    content = Column(String(100), nullable=False)  # 内容
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:删除
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"TeamChat(id={self.id}, team_id={self.team_id}, user_id={self.user_id}, content={self.content})"
