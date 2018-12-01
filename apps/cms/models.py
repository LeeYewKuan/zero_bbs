# !usr/bin/env python3
# coding: utf-8

from exts import db
from datetime import datetime
# 使用flask的生成密码工具
from werkzeug.security import generate_password_hash
# 使用flask的校验密码工具
from werkzeug.security import check_password_hash


class CMSPermission(object):
    """
    权限表
    255的二进制来表示
    """
    ALL_PERMISSION = 0b11111111
    # 访问者
    VISITOR = 0b00000001
    # 管理帖子权限
    POSTER = 0b00000010
    # 管理评论的权限
    COMMENTER = 0b00000100
    # 板块权限
    BOARDER = 0b00001000
    # 前台用户
    FRONTUSER = 0b00010000
    # 后台用户
    CMSUSER = 0b00100000
    # 管理后台管理员权限
    ADMINER = 0b0100000

cms_role_user = db.Table(
    'cms_role_user',
    db.Column('cms_role_id', db.Integer, db.ForeignKey('cms_role.id'), primary_key=True),
    db.Column('cms_user_id', db.Integer, db.ForeignKey('cms_user.id'), primary_key=True)
)


class CMSRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    permissions = db.Column(db.Integer, default=CMSPermission.VISITOR)

    users = db.relationship('CMSUser', secondary=cms_role_user, backref='roles')


# 构建cms用户
class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

    # 通过构造方法将获取到的密码加密
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    # 通过注解将一个方法变成一个属性
    @property
    def password(self):
        return self._password

    # 给注解的方法属性设置(加密保存)
    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result

    @property
    def permissions(self):
        if not self.roles:
            return 0
        all_permissions = 0
        for role in self.roles:
            permissions = role.permissions
            all_permissions |= permissions
        return all_permissions

    def has_permission(self, permission):
        return self.permissions & permission == permission

    @property
    def is_developer(self):
        return self.has_permission(CMSPermission.ALL_PERMISSION)
