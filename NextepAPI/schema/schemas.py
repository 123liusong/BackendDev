#!/usr/bin/python3

from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime


# Schedule

class ScheduleBase(BaseModel):
    title: str
    body: str
    start_time: datetime
    end_time: datetime
    state: int
    level : int    


class Schedule(ScheduleBase):
    id: int
    creator_id: int
    team_id: int

    class Config:
        orm_mode = True
    
class ScheduleCreate(ScheduleBase):
    creator_id: int
    team_id: int


class ScheduleUpdate(ScheduleBase):
    pass

class ScheduleDelete(ScheduleBase):
    id : int



# Team
class TeamBase(BaseModel):
    title: str
    body: str


class Team(TeamBase):
    id: int
    leader_id: int

    class Config:
        orm_mode = True
    
class TeamCreate(TeamBase):
    leader_id: int

class TeamUpdate(TeamBase):
    leader_id: int

class TeamDelete(TeamBase):
    id : int

# Attachment
class AttachmentBase(BaseModel):
    title: str
    path: str
    type : str
    size : int


class Attachment(AttachmentBase):
    id: int
    team_id: int
    creator_id : int

    class Config:
        orm_mode = True

class AttachmentCreate(AttachmentBase):
    team_id: int

class AttachmentUpdate(AttachmentBase):
    team_id: int

class AttachmentDelete(AttachmentBase):
    id : int

class ShowAttachment(AttachmentBase):
    id: int
    team_id: int
    creator_id : int
    create_at: datetime

    class Config:
        orm_mode = True
# todo_list
class TodoListBase(BaseModel):
    title: str
    count : int
    state : int

class TodoList(TodoListBase):
    id: int
    team_id: int
    creator_id : int

    class Config:
        orm_mode = True
    
class TodoListCreate(TodoListBase):
    team_id: int
    creator_id : int



class TodoListUpdate(TodoListBase):
    pass

class TodoListDelete(TodoListBase):
    id : int

class ShowTodoList(TodoListBase):
    id: int
    team_id: int
    creator_id : int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True

class TeamMemberBase(BaseModel):

    alias: str


class TeamMember(TeamMemberBase):
    id: int
    team_id: int
    member_id: int

    class Config:
        orm_mode = True

class TeamMemberCreate(TeamMemberBase):
    team_id: int
    member_id: int

class TeamMemberUpdate(TeamMemberBase):
    pass


class TeamMemberDelete(TeamMemberBase):
    id : int



# schedule_todo_list
class ScheduleTodoListBase(BaseModel):
    schedule_id: int
    todo_list_id: int


class ScheduleTodoList(ScheduleTodoListBase):
    id: int


    class Config:
        orm_mode = True


class ScheduleTodoListCreate(ScheduleTodoListBase):
    pass

# 不用
class ScheduleTodoListUpdate(ScheduleTodoListBase):
    pass

class ScheduleTodoListDelete(ScheduleTodoListBase):
    id : int

# 不用
class ShowScheduleTodoList(ScheduleTodoListBase):
    id: int
    create_at: datetime

    class Config:
        orm_mode = True

# schedule_attachment
class ScheduleAttachmentBase(BaseModel):
    schedule_id: int
    attachment_id: int


class ScheduleAttachment(ScheduleAttachmentBase):
    id: int

    class Config:
        orm_mode = True


class ScheduleAttachmentCreate(ScheduleAttachmentBase):
    pass

# 不用
class ScheduleAttachmentUpdate(ScheduleAttachmentBase):
    pass

class ScheduleAttachmentDelete(ScheduleAttachmentBase):
    id : int

# 不用
class ShowScheduleAttachment(ScheduleAttachmentBase):
    id: int
    schedule_id: int
    attachment_id: int
    create_at: datetime

    class Config:
        orm_mode = True
    
# log
class LogBase(BaseModel):
    title: str
    body: str
    type: int

class Log(LogBase):
    id: int
    creator_id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


class LogCreate(LogBase):
    creator_id: int

class LogUpdate(LogBase):
    creator_id: int

class LogDelete(LogBase):

    id : int

class ShowLog(LogBase):
    id: int
    creator_id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True

# user
class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    schedules: List[Schedule] = []

    class Config:
        orm_mode = True


# class ShowSchedule(BaseModel):
#     title: str
#     body: str
#     creator: ShowUser

#     class Config:
#         orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None



class ShowTeam(TeamBase):
    id: int
    leader_id: int
    create_at: datetime
    update_at: datetime
    schedules : List[Schedule] = []
    attachments : List[Attachment] = []
    todo_lists : List[TodoList] = []

    class Config:
        orm_mode = True
class ShowSchedule(ScheduleBase):
    id: int
    creator_id: int
    creator : ShowUser
    team_id: int
    team : ShowTeam
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
class ShowTeamMember(TeamMemberBase):
    id: int
    team_id: int
    member_id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# # 消息表
# class Message(Base):
#     __tablename__ = "messages"
#     id = Column(Integer, primary_key=True, index=True,
#                 autoincrement=True)  # 消息id
#     title = Column(String)  # 消息标题
#     body = Column(String)  # 消息内容
#     type = Column(Integer)  # 消息类型 0 个人 1 团队
#     state = Column(Integer)  # 消息状态 0 未读 1 已读
#     creator_id = Column(Integer, ForeignKey("users.id"))  # 消息创建者id
    # to_user_id = Column(Integer, ForeignKey("users.id"))  # 消息接收者id
#     # 消息创建时间
#     create_at = Column(DateTime, default=func.now())  # 创建时间

class MessageBase(BaseModel):
    title: str
    body: str
    type: int
    state: int
    creator_id: int
    to_user_id: int

class Message(MessageBase):
    id: int
    create_at: datetime

    class Config:
        orm_mode = True

class MessageCreate(MessageBase):
    pass

class MessageUpdate(MessageBase):
    pass

class ShowMessage(MessageBase):
    id: int
    create_at: datetime

    class Config:
        orm_mode = True


