from flask import Flask

from app.config import Config

from app.extensions import (
    db,
    login_manager,
    migrate,
    mail
)

# =========================================
# IMPORT MODELS
# IMPORTANT FOR FLASK-MIGRATE
# =========================================

import app.models


# =========================================
# CREATE APPLICATION
# =========================================

def create_app():

    flask_app = Flask(__name__)

    flask_app.config.from_object(Config)

    # =====================================
    # INITIALIZE EXTENSIONS
    # =====================================

    db.init_app(flask_app)

    login_manager.init_app(flask_app)

    migrate.init_app(flask_app, db)

    mail.init_app(flask_app)

    # =====================================
    # LOGIN CONFIGURATION
    # =====================================

    login_manager.login_view = (
        "auth.login"
    )

    login_manager.login_message_category = (
        "warning"
    )

    # =====================================
    # REGISTER BLUEPRINTS
    # =====================================

    from app.public.routes import public_bp

    from app.auth.routes import auth_bp

    from app.department.routes import (
        department_bp
    )

    from app.admin.routes import admin_bp

    from app.voter.routes import voter_bp

    flask_app.register_blueprint(
        public_bp
    )

    flask_app.register_blueprint(
        auth_bp
    )

    flask_app.register_blueprint(
        department_bp
    )

    flask_app.register_blueprint(
        admin_bp
    )

    flask_app.register_blueprint(
        voter_bp
    )

    return flask_app