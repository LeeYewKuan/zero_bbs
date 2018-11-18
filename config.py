#!/usr/bin/env python3
# coding: UTF-8

import os

SECRET_KEY = os.urandom(24)

# 调试模式配置
DEBUG = True

# 数据库配置
DB_USERNAME = 'root'
DB_PASSWORD = ''
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'zero_bbs'

# 数据库全路径
DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

# 设置orm映射数据库的URI
SQLALCHEMY_DATABASE_URI = DB_URI

# 设置模型改变通知为关闭状态
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 配置用户ID表示
CMS_USER_ID = "cms_user_id"

# 配置邮件
# 发送者邮箱服务器地址
MAIL_SERVER = "smtp.qq.com"
# 端口号：非加密：25
# MAIL_USE_TLS: 端口号：587
# MAIL_USE_SSL: 端口好：465
# QQ邮箱不支持非加密方式发送邮件
MAIL_PORT = '587'
MAIL_USE_TLS = True
MAIL_USERNAME = "2308074270@qq.com"
# 开启TLS服务的授权码
MAIL_PASSWORD = ""
# 默认发送者
MAIL_DEFAULT_SENDER = "2308074270@qq.com"

