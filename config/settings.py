# -*- coding: UTF-8 -*-
import os

# 项目根路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 端口号
PORT = 8888

# API 网关
URLS = { 
    # 飞书自建应用中事件订阅的路由
    'events': '/event/',

    # 飞书自建应用中交互机器人的路由
    'larkbot': '/card/',

    # 语雀第三方消息推送的路由
    'yuque': '/hook/'
}

# 飞书开放平台 | 企业自建应用 | 凭证与基础信息
APP_ID = "cli_xxxxx"
APP_SECRET = "xxxxxxxxxxxxx" 

# 飞书开放平台 | 企业自建应用 | 事件订阅 | 开启Encrypt Key
ENCRYPT_KEY = "xxxxxxxxxxxxxx"

# 定义机器人昵称 | 群组中唤醒机器人（不使用@Bot）
NICK_NAME = "小雀同学"


