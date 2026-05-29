from flask_login import UserMixin

from datetime import datetime

from app.extensions import (
    db,
    login_manager
)


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    voter_application_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "voter_applications.id"
        ),
        nullable=True
    )

    full_name = db.Column(
        db.String(150),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    voter_id = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(50),
        default="voter"
    )

    status = db.Column(
        db.String(50),
        default="active"
    )

    last_login = db.Column(
        db.DateTime
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(
        int(user_id)
    )