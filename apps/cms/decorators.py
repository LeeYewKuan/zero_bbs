#!usr/bin/evn python3
# encoding: utf8
from flask import session, redirect, url_for
from functools import wraps
from .models import CMSUser
import config


def login_required(fun):

    @wraps(fun)
    def inner(*args, ** kwargs):
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.filter_by(id=user_id).first()
        if user:
            return fun(*args, **kwargs)
        else:
            return redirect(url_for('cms.login'))
    return inner
