#!/usr/bin/env python3
# coding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from exts import db

# 导入模型，纳入数据库迁移版本管理
from apps.cms import models

CMSUser = models.CMSUser
CMSRole = models.CMSRole
CMSPermission = models.CMSPermission

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


# 定义默认用户的访问权限
@manager.command
def create_role():
    # 访问者
    visitor = CMSRole(name='访客', desc='只能查看，不能修改')
    visitor.permissions = CMSPermission.VISITOR

    # 运营
    operator = CMSRole(name='运营', desc='管理帖子，评论和前台用户')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER \
                           | CMSPermission.CMSUSER | CMSPermission.COMMENTER \
                           | CMSPermission.FRONTUSER

    # 管理员
    admin = CMSRole(name='管理员', desc='拥有本系统所有权限')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.POSTER \
                        | CMSPermission.CMSUSER | CMSPermission.COMMENTER \
                        | CMSPermission.FRONTUSER | CMSPermission.BOARDER

    # 开发者
    developer = CMSRole(name='开发者', desc='开发人员专用')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


@manager.option('-e', '--email', dest="email")
@manager.option('-n', '--name', dest='name')
def add_user_role(email, name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加到角色成功')
        else:
            print('没有这个角色%s' % role)
    else:
        print('邮箱没有这个用户%s = ' % email)


@manager.command
def test_permission():
    user = CMSUser.query.first()
    if user.is_developer:
        print('这个用户有访问权限')
    else:
        print('这个用户没有访问权限')


if __name__ == '__main__':
    manager.run()
