from datetime import datetime

from app.extensions import db

from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    voter_application_id = db.Column(
        db.Integer,
        db.ForeignKey("voter_applications.id"),
        nullable=False
    )

    voter_id = db.Column(
        db.String(50),
        unique=True,
        nullable=False
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

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(50),
        default="voter"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )