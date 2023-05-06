#!/usr/bin/python3

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, Table
from sqlalchemy.orm import relationship
from database.configuration import Base


class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)  # 日程标题
    body = Column(String)  # 日程内容
    creator_id = Column(Integer, ForeignKey("users.id"))  # 外键 user_id
    creator = relationship("User", back_populates="schedules")  # 反向引用

    team_id = Column(Integer, ForeignKey("teams.id"))  # 外键 team_id
    team = relationship("Team", back_populates="schedules")  # 反向引用
    todo_lists = relationship("TodoList",
                              back_populates="schedules",
                              secondary='schedule_todo_list')  # 反向引用
    attachments = relationship("Attachment",
                               back_populates="schedules",
                               secondary='schedule_attachment')  # 反向引用
    start_time = Column(DateTime)  # 开始时间
    end_time = Column(DateTime)  # 结束时间
    state = Column(Integer)  # 状态 0 未完成 1 已完成
    level = Column(Integer)  # 优先级 0 低 1 中 2 高
    create_at = Column(DateTime, default=func.now())  # 创建时间
    update_at = Column(DateTime, default=func.now(),
                       onupdate=func.now())  # 更新时间


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True)  # 用户id
    name = Column(String)  # 用户名
    email = Column(String, index=True)  # 邮箱
    password = Column(String)  # 密码
    lteams = relationship("Team", back_populates="leader")  # 反向引用
    schedules = relationship("Schedule", back_populates="creator")  # 反向引用
    logs = relationship("Log", back_populates="creator")  # 反向引用
    teams = relationship("Team",
                         back_populates="members",
                         secondary='team_member')  # 反向引用
    todo_lists = relationship("TodoList", back_populates="creator")  # 反向引用
    attachments = relationship("Attachment", back_populates="creator")  # 反向引用
    create_at = Column(DateTime, default=func.now())  # 创建时间
    update_at = Column(DateTime, default=func.now(),
                       onupdate=func.now())  # 更新时间


# 团队表
class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True)  # 团队id
    title = Column(String)  # 团队名
    body = Column(String)  # 团队描述
    leader_id = Column(Integer, ForeignKey("users.id"))  # 队长
    leader = relationship("User", back_populates="lteams")
    members = relationship("User",
                           back_populates="teams",
                           secondary='team_member')  # 反向引用
    todo_lists = relationship("TodoList", back_populates="team")  # 反向引用
    attachments = relationship("Attachment", back_populates="team")  # 反向引用
    schedules = relationship("Schedule", back_populates="team")  # 反向引用
    create_at = Column(DateTime, default=func.now())  # 创建时间
    update_at = Column(DateTime, default=func.now(),
                       onupdate=func.now())  # 更新时间


# # 团队成员表
# class TeamMember(Base):
#     __tablename__ = "team_members"
#     id = Column(Integer, primary_key=True, index=True ,autoincrement=True)  # 团队成员id
#     alias = Column(String)  #别名
#     team_id = Column(Integer, ForeignKey("teams.id"))  # 团队id
#     # team = relationship("Team", back_populates="members")
#     member_id = Column(Integer, ForeignKey("users.id"))  # 成员id
#     # member = relationship("User", back_populates="teams")
#     create_at = Column(DateTime, default=func.now())  # 创建时间
#     update_at = Column(DateTime,
#                        default=func.now(),
#                        onupdate=func.now())  # 更新时间

team_member = Table(
    "team_member", Base.metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("alias", String), Column("team_id", Integer,
                                    ForeignKey("teams.id")),
    Column("member_id", Integer, ForeignKey("users.id")),
    Column("create_at", DateTime, default=func.now()),
    Column("update_at", DateTime, default=func.now(), onupdate=func.now()))


# 附件表
class Attachment(Base):
    __tablename__ = "attachments"
    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True)  # 附件id
    title = Column(String)  # 附件名
    path = Column(String)  # 附件路径
    type = Column(String)  # 附件类型
    size = Column(Integer)  # 附件大小
    team_id = Column(Integer, ForeignKey("teams.id"))  # 团队id
    team = relationship("Team", back_populates="attachments")
    creator = relationship("User", back_populates="attachments")  # 反向引用
    schedules = relationship("Schedule",
                             back_populates="attachments",
                             secondary='schedule_attachment')  # 反向引用
    creator_id = Column(Integer, ForeignKey("users.id"))  # 附件创建者id
    create_at = Column(DateTime, default=func.now())  # 创建时间


# 清单表
class TodoList(Base):
    __tablename__ = "todo_lists"
    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True)  # 清单id
    title = Column(String)  # 清单名
    creator_id = Column(Integer, ForeignKey("users.id"))  # 清单创建者id
    creator = relationship("User", back_populates="todo_lists")
    count = Column(Integer)  # 数量
    state = Column(Integer)  # 状态 0 未完成 1 已完成
    team_id = Column(Integer, ForeignKey("teams.id"))  # 团队id
    team = relationship("Team", back_populates="todo_lists")

    schedules = relationship("Schedule",
                             back_populates="todo_lists",
                             secondary='schedule_todo_list')  # 反向引用
    create_at = Column(DateTime, default=func.now())  # 创建时间
    update_at = Column(DateTime, default=func.now(),
                       onupdate=func.now())  # 更新时间


# # 日程清单表
# class ScheduleTodoList(Base):
#     __tablename__ = "schedule_todo_lists"
#     id = Column(Integer, primary_key=True, index=True ,autoincrement=True)  # 日程清单id
#     schedule_id = Column(Integer, ForeignKey("schedules.id"))  # 日程id
#     schedule = relationship("Schedule", back_populates="todo_lists")
#     todo_list_id = Column(Integer, ForeignKey("todo_lists.id"))  # 清单id
#     todoList = relationship("TodoList", back_populates="schedules")
#     # todo_list = relationship("TodoList", back_populates="schedules")
#     create_at = Column(DateTime, default=func.now())  # 创建时间

schedule_todo_list = Table(
    "schedule_todo_list", Base.metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("schedule_id", Integer, ForeignKey("schedules.id")),
    Column("todo_list_id", Integer, ForeignKey("todo_lists.id")),
    Column("create_at", DateTime, default=func.now()))

# # 日程附件表
# class ScheduleAttachment(Base):
#     __tablename__ = "schedule_attachments"
#     id = Column(Integer, primary_key=True, index=True ,autoincrement=True)  # 日程附件id
#     schedule_id = Column(Integer, ForeignKey("schedules.id"))  # 日程id
#     schedule = relationship("Schedule", back_populates="attachments")
#     attachment_id = Column(Integer, ForeignKey("attachments.id"))  # 附件id
#     attachment = relationship("Attachment", back_populates="schedules")
#     create_at = Column(DateTime, default=func.now())  # 创建时间

schedule_attachment = Table(
    "schedule_attachment", Base.metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("schedule_id", Integer, ForeignKey("schedules.id")),
    Column("attachment_id", Integer, ForeignKey("attachments.id")),
    Column("create_at", DateTime, default=func.now()))


# 日志表
class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True)  # 日志id
    title = Column(String)  # 日志标题
    body = Column(String)  # 日志内容
    type = Column(Integer)  # 日志类型 0 个人 1 团队
    creator_id = Column(Integer, ForeignKey("users.id"))  # 日志创建者id
    creator = relationship("User", back_populates="logs")
    # 日志创建时间
    create_at = Column(DateTime, default=func.now())  # 创建时间


# # 消息表
# class Message(Base):
#     __tablename__ = "messages"
#     id = Column(Integer, primary_key=True, index=True,
#                 autoincrement=True)  # 消息id
#     title = Column(String)  # 消息标题
#     body = Column(String)  # 消息内容
#     type = Column(Integer)  # 消息类型 0 个人 1 团队
#     creator_id = Column(Integer, ForeignKey("users.id"))  # 消息创建者id
#     creator = relationship("User", back_populates="messages")
#     # 消息创建时间
#     create_at = Column(DateTime, default=func.now())  # 创建时间