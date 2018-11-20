from wtforms import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from ..forms import BaseForm
from utils import zerocache
from wtforms import ValidationError
from flask import g


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6, 20, message='请输入正确的密码')])
    remember = IntegerField()


class ResetPwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6, 20, message="请输入正确格式的旧密码")])
    newpwd = StringField(validators=[Length(6, 20, message="请输入正确格式的新密码")])
    newpwd2 = StringField(validators=[EqualTo('newpwd', message="两次输入的密码不一致")])


class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message="请输入正确的预想格式"), InputRequired(message='请输入邮箱')])
    captcha = StringField(validators=[Length(6, 6, message="请输入六位的验证码")])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        cache_captcha = zerocache.get(email)

        if not captcha or cache_captcha != cache_captcha:
            raise ValidationError(message="验证码不匹配")

    def validate_email(self, field):
        email = field.data
        old_email = g.cms_user.email
        if email == old_email:
            raise ValidationError(message="不能更改为相同的邮箱")




