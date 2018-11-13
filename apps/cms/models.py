# !usr/bin/env python3
# coding: utf-8

from exts import db
from datetime import datetime
# 使用flask的生成密码工具
from werkzeug.security import generate_password_hash
# 使用flask的校验密码工具
from werkzeug.security import check_password_hash


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
