from flask import Blueprint
from flask import views
from flask import render_template, request, session, redirect, url_for, g
from .forms import LoginForm, ResetPwdForm, ResetEmailForm
from .models import CMSUser
from .decorators import login_required
import config
from exts import db
# 邮件
from exts import mail
from flask_mail import Message
from utils import resultful

bp = Blueprint('cms', __name__, url_prefix='/cms')


# 登录的view
class LoginView(views.MethodView):

    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data

            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # 如果过期时间为记住我，时间就设置为31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message="用户名或者密码不正确")
        else:
            message = form.get_error()
            print(message)
            return self.get(message=message)


class RestPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetPwdForm(request.form)
        if form.validate():
            old_pwd = form.oldpwd.data
            new_pwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(old_pwd):
                user.password = new_pwd
                db.session.commit()
                return resultful.success()
            else:
                return resultful.unauth_error(message="旧密码验证失败")

        else:
            message = form.get_error()
            print(message)
            return resultful.params_error(message=message)


class ResetEmailView(views.MethodView):

    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            return resultful.success()
        else:
            return resultful.params_error(form.get_error())


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=RestPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))


@bp.route('/email/')
def send_email():
    message = Message("邮件发送", recipients=["514979156@qq.com"], body="您正在更改zerobbs登录的邮箱，验证码：541234")
    mail.send(message=message)
    return "邮件发送成功"


@bp.route('/logout/')
def logout():
    session.pop(config.CMS_USER_ID)
    return redirect(url_for('cms.login'))


@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')

