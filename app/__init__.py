from flask import Flask

from app.config import Config


from app.extensions import (
    db,
    login_manager,
    migrate,
    mail
)

from app.auth.routes import auth_bp
from app.public.routes import public_bp
from app.voter.routes import voter_bp
from app.models.user import User
from app.department.routes import department_bp
from app.admin.routes import admin_bp

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(voter_bp)
    app.register_blueprint(admin_bp)


    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))


    return app