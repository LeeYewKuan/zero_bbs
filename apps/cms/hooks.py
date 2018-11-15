import config
from flask import session,g
from .models import CMSUser
from .views import bp


@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.filter_by(id=user_id).first()
        if user:
            g.cms_user = user
