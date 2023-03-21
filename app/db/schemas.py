#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@文件        :schemas.py
@说明        :pydantic模型
@时间        :2023/02/11 12:57:15
@作者        :seanliu
"""

# pydantic模型
from pydantic import BaseModel
from datetime import datetime

"""    
    id = Column(Integer, primary_key=True, index=True)  # 主键
    name = Column(String(20), nullable=False)  # 用户名
    email = Column(String(50), nullable=False)  # 邮箱
    password = Column(String(100), nullable=False)  # 密码
    gender = Column(Integer, nullable=False)  # 性别 0:男 1:女
    is_active = Column(Boolean, default=True)  # 是否激活
    is_superuser = Column(Boolean, default=False)  # 是否超级管理员
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:禁用
"""


# 定义模型 用于创建用户
class CreateUser(BaseModel):
    name: str
    email: str
    password: str
    gender: int
    is_active: bool
    is_superuser: bool
    state: int


# 定义模型 用于读取用户
class ReadUser(BaseModel):
    name: str
    email: str


# 定义模型 用于更新用户
class UpdateUser(BaseModel):
    name: str
    password: str

# 定义模型 用于登录、登出后激活用户
class ActiveUser(BaseModel):
    id: int
    is_active: bool

# 定义模型 用于登录用户
class LoginUser(BaseModel):
    email: str
    password: str


# 定义模型 用于删除用户
class DeleteUser(BaseModel):
    id: int


""" 
    id = Column(Integer, primary_key=True, index=True)  # 主键
    name = Column(String(100), nullable=False)  # 团队名称
    description = Column(Text, nullable=False)  # 团队描述
    leader_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:禁用
"""


# 定义模型 用于创建团队
class CreateTeam(BaseModel):
    name: str
    description: str
    leader_id: int
    state: int


# 定义模型 用于删除团队
class DeleteTeam(BaseModel):
    id: int


""" 
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
"""


# 定义模型 用于创建文件
class CreateFile(BaseModel):
    name: str
    path: str
    size: float
    state: int
    is_user: bool
    user_id: int
    is_team: bool
    team_id: int
    is_public: bool


# 定义模型 用于删除文件
class DeleteFile(BaseModel):
    id: int


# 定义模型 用于查看文件
class ReadFile(BaseModel):
    name: str
    path: str
    size: float
    state: int
    is_user: bool
    user_id: int
    is_team: bool
    team_id: int
    is_public: bool
    created_at: datetime
    updated_at: datetime


# 定义模型 用于更新文件
class UpdateFile(BaseModel):
    name: str
    state: int
    is_public: bool


"""    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键
    token = Column(String(100), nullable=False)  # token
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
"""


# 定义模型 用于创建token - 注册用户时创建token
class CreateToken(BaseModel):
    user_id: int
    token: str


# 定义模型 用于删除token - 删除用户时删除token
class DeleteToken(BaseModel):
    id: int

# 定义模型 用于修改token - 登陆一次修改一次token
class UpdateToken(BaseModel):
    token: str


"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键
    ip = Column(String(20), nullable=False)  # ip地址
    method = Column(String(10), nullable=False)  # 请求方法
    path = Column(String(100), nullable=False)  # 请求路径
    status_code = Column(Integer, nullable=False)  # 状态码
    created_at = Column(DateTime, default=func.now())
"""


# 定义模型 用于创建日志
class CreateLog(BaseModel):
    user_id: int
    ip: str
    method: str
    path: str
    status_code: int


# 定义模型 用于查看日志
class ReadLog(BaseModel):
    user_id: int
    ip: str
    method: str
    path: str
    status_code: int
    created_at: datetime


""" 
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
"""


# 定义模型 用于创建md文件
class CreateMd(BaseModel):
    name: str
    path: str
    state: int
    is_user: bool
    user_id: int
    is_team: bool
    team_id: int


# 定义模型 用于删除md文件
class DeleteMd(BaseModel):
    id: int


# 定义模型 用于查看md文件
class ReadMd(BaseModel):
    name: str
    path: str
    state: int
    is_user: bool
    user_id: int
    is_team: bool
    team_id: int
    created_at: datetime
    updated_at: datetime


# 定义模型 用于更新md文件
class UpdateMd(BaseModel):
    name: str
    state: int


"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    is_user = Column(Boolean, default=False)  # 是否用户文件
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    is_team = Column(Boolean, default=False)  # 是否团队文件
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    title = Column(String(100), nullable=False)  # 标题
    content = Column(String(100), nullable=False)  # 内容
    start_time = Column(DateTime, nullable=False)  # 开始时间
    end_time = Column(DateTime, nullable=False)  # 结束时间
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:禁用
    level = Column(Integer, nullable=False)  # 级别  0:普通 1:重要 2:紧急
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
"""


# 定义模型 用于创建日程
class CreateSchedule(BaseModel):
    is_user: bool
    user_id: int
    is_team: bool
    team_id: int
    title: str
    content: str
    start_time: datetime
    end_time: datetime
    state: int
    level: int


# 定义模型 用于删除日程
class DeleteSchedule(BaseModel):
    id: int


# 定义模型 用于查看日程
class ReadSchedule(BaseModel):
    is_user: bool
    user_id: int
    is_team: bool
    team_id: int
    title: str
    content: str
    start_time: datetime
    end_time: datetime
    state: int
    level: int
    created_at: datetime
    updated_at: datetime


# 定义模型 用于更新日程
class UpdateSchedule(BaseModel):
    title: str
    content: str
    start_time: datetime
    end_time: datetime
    state: int
    level: int


"""
 id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    schedule_id = Column(Integer, ForeignKey("schedule.id"))  # 外键 关联schedule表
    markdown_file_id = Column(
        Integer, ForeignKey("markdown_file.id")
    )  # 外键 关联markdown_file表
    file_id = Column(Integer, ForeignKey("file.id"))  # 外键 关联file表
    todo_list_id = Column(Integer, ForeignKey("todo_list.id"))  # 外键 关联todo_list表
    created_at = Column(DateTime, default=func.now())
"""


# 定义模型 用于创建日程关联
class CreateScheduleRelation(BaseModel):
    schedule_id: int
    markdown_file_id: int
    file_id: int
    todo_list_id: int


# 定义模型 用于删除日程关联
class DeleteScheduleRelation(BaseModel):
    id: int


"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键
    created_at = Column(DateTime, default=func.now())
"""


# 定义模型 用于创建团队成员关联
class CreateTeamMemberRelation(BaseModel):
    team_id: int
    user_id: int


# 定义模型 用于删除团队成员关联
class DeleteTeamMemberRelation(BaseModel):
    id: int

"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    type = Column(Integer, nullable=False)  # 类型 0:系统消息 1:团队消息 2:个人消息
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    receive_user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    send_user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    content = Column(String(100), nullable=False)  # 内容
    state = Column(Integer, nullable=False)  # 状态 0:未读 1:已读
    created_at = Column(DateTime, default=func.now())
"""

# 定义模型 用于创建消息
class CreateMessage(BaseModel):
    type: int
    team_id: int
    receive_user_id: int
    send_user_id: int
    content: str
    state: int

# 定义模型 用于删除消息
class DeleteMessage(BaseModel):
    id: int

# 定义模型 用于查看消息
class ReadMessage(BaseModel):
    type: int
    team_id: int
    receive_user_id: int
    send_user_id: int
    content: str
    state: int
    created_at: datetime

"""
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
"""

# 定义模型 用于创建清单
class CreateTodoList(BaseModel):
    is_user: bool
    user_id: int
    is_team: bool
    team_id: int
    title: str
    description: str
    number: int
    type: int
    state: int

# 定义模型 用于删除清单
class DeleteTodoList(BaseModel):
    id: int

# 定义模型 用于查看清单
class ReadTodoList(BaseModel):
    is_user: bool
    user_id: int
    is_team: bool
    team_id: int
    title: str
    description: str
    number: int
    type: int
    state: int
    created_at: datetime
    updated_at: datetime

# 定义模型 用于更新清单
class UpdateTodoList(BaseModel):
    title: str
    description: str
    number: int
    type: int
    state: int


"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # 主键
    team_id = Column(Integer, ForeignKey("team.id"))  # 外键 关联team表
    user_id = Column(Integer, ForeignKey("user.id"))  # 外键 关联user表
    content = Column(String(100), nullable=False)  # 内容
    state = Column(Integer, nullable=False)  # 状态 0:正常 1:删除
    created_at = Column(DateTime, default=func.now())
"""

# 定义模型 用于团队创建聊天
class CreateChat(BaseModel):
    team_id: int
    user_id: int
    content: str
    state: int

# 定义模型 用于团队删除聊天
class DeleteChat(BaseModel):
    id: int

# 定义模型 用于团队查看聊天
class ReadChat(BaseModel):
    team_id: int
    user_id: int
    content: str
    state: int
    created_at: datetime

