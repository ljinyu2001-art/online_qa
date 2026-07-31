# 在线问答系统（Online QA System）

## 项目简介

在线问答系统是一个基于前后端分离架构开发的 Web 应用系统。

用户可以在系统中创建问题、浏览问题列表、查看问题详情，并针对问题提交回答。

系统后端采用 FastAPI 开发，使用 MySQL 进行业务数据持久化存储，同时结合 Redis 实现缓存机制，提高系统访问效率。

本项目主要用于学习和实践：

- 前后端分离开发
- RESTful API 接口设计
- FastAPI 后端开发
- Vue3 前端开发
- MySQL 数据库设计
- SQLAlchemy ORM 数据操作
- Redis 缓存应用


---

# 技术栈

## 后端

| 技术 | 说明 |
| --- | --- |
| Python | 后端开发语言 |
| FastAPI | Web 后端框架 |
| SQLAlchemy | ORM 框架 |
| MySQL | 数据库存储 |
| Redis | 缓存服务 |
| Pydantic | 数据验证 |
| Uvicorn | Web服务器 |


## 前端

| 技术 | 说明 |
| --- | --- |
| Vue3 | 前端框架 |
| Vite | 构建工具 |
| Axios | HTTP请求库 |
| Element Plus | UI组件库 |


---

# 系统功能

## 问题管理

系统支持：

- 创建问题
- 查看问题列表
- 查看问题详情
- 修改问题
- 删除问题


## 回答管理

系统支持：

- 提交回答
- 查看问题回答
- 自动统计回答数量


## Redis缓存

使用 Redis 缓存问题列表数据：

缓存内容：
问题：列表


缓存时间：
300秒


当问题发生以下操作时：

- 新增问题
- 修改问题
- 删除问题
- 添加回答

会清理 Redis 缓存，保证数据一致性。


---

# 系统架构
            用户

             |
             |

          Vue前端

             |
             |

         FastAPI接口

      -----------------

      |               |

      |               |

   MySQL           Redis

业务数据保存     数据缓存


---

# 项目目录结构
在线问答系统

├── backend # 后端项目
│
├── core
│ ├── database.py # MySQL数据库连接
│ └── redis.py # Redis连接配置
│
├── models # 数据模型
│ ├── question.py
│ └── answer.py
│
├── schemas # 请求数据模型
│ ├── question.py
│ └── answer.py
│
├── routers # 接口路由
│ ├── question.py
│ └── answer.py
│
├── services # 业务逻辑
│ └── qa_service.py
│
└── main.py # 后端入口

├── frontend # Vue前端

│── src
│ ├── api # 接口请求
│ ├── views # 页面
│ ├── router # 路由
│ └── App.vue

├── sql
│ └── online_qa.sql # 数据库初始化文件

└── README.md



---

# 数据库设计

数据库名称：
在线问答



系统主要包含两个数据表。


## question 问题表

用于保存用户发布的问题。


字段：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 主键 |
| title | varchar | 问题标题 |
| description | text | 问题描述 |
| answer_count | int | 回答数量 |


---

## answer 回答表

用于保存用户提交的回答。


字段：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 主键 |
| content | text | 回答内容 |
| question_id | int | 所属问题ID |


数据关系：
问题 1 -------- 答案



一个问题可以拥有多个回答。


---

# Redis设计

Redis主要用于缓存问题列表。


缓存Key：
问题：列表



缓存数据示例：

```json
[
    {
        "id":1,
        "title":"如何学习Python",
        "description":"Python学习问题",
        "answer_count":3
    }
]
缓存有效时间：

300秒
数据更新时：

新增问题
修改问题
删除问题
添加回答

        ↓

删除 question:list 缓存

        ↓

重新查询数据库
后端运行
1. 创建虚拟环境
python -m venv .venv
视窗：

.venv\Scripts\activate
2. 安装依赖
pip install -r requirements.txt
3. 创建数据库
进入 MySQL：

CREATE DATABASE online_qa;
执行初始化 SQL：

source online_qa.sql;
4. 启动 Redis
视窗：

redis-server
Linux：

systemctl start redis
5. 启动后端
进入 backend：

cd backend
启动：

uvicorn main:app --reload
接口文档：

http://127.0.0.1:8000/docs
前端运行
进入 frontend：

cd frontend
安装依赖：

npm install
启动：

npm run dev
访问：

http://localhost:5173
API接口
问题接口
获取问题列表
GET /questions
创建问题
POST /questions
请求：

{
    "title":"测试问题",
    "description":"问题描述"
}
修改问题
PUT /questions/{id}
删除问题
DELETE /questions/{id}
回答接口
添加回答
POST /answers/{question_id}
请求：

{
    "content":"这是一个回答"
}
项目总结
本项目完成了一个基础在线问答系统的设计与开发。

通过该项目实践了：

Vue3 前端页面开发

FastAPI 后端接口设计

SQLAlchemy ORM数据库操作

MySQL数据存储

Redis缓存优化

前后端数据交互

项目实现了从数据库设计、后端开发到前端展示的完整 Web 应用开发流程。
