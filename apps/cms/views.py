from flask import Blueprint
from flask import views
from flask import render_template, request, session, redirect, url_for
from .forms import LoginForm
from .models import CMSUser
from .decorators import login_required
import config

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
            message = form.errors.popitem()[1][0]
            print(message)
            return self.get(message=message)


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))


@bp.route('/')
@login_required
def index():
    return 'cms'

