#!/usr/bin/env python3
# coding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from exts import db

# 导入模型，纳入数据库迁移版本管理
from apps.cms import models

CMSUser = models.CMSUser

# 构建app
app = create_app()

# 构建脚本管理工具管理，针对当前项目
manager = Manager(app)

# 构建迁移对象(对哪个应用，数据库是什么)
Migrate(app, db)
# 将迁移对象的命令导入到脚本命令中(执行迁移对象的脚本名称，具体的迁移脚本命令)
manager.add_command('db', MigrateCommand)


# 定义一个添加用户的脚本方法,使用注解给定传值参数
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('add', username, 'success')


if __name__ == '__main__':
    manager.run()
