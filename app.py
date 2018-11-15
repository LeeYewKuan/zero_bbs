from flask import Flask
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
import config
from exts import db
from flask_wtf import CSRFProtect


# 构建需要的app对象
def create_app():
    app = Flask(__name__)
    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)

    app.config.from_object(config)

    db.init_app(app)
    CSRFProtect(app)
    return app


if __name__ == '__main__':
    zero_app = create_app()
    zero_app.run()
