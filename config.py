#!/usr/bin/env python3
# coding: UTF-8

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
SQLALCHEMY_TRACK_MODIFICATION = False
