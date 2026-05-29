from app import db
from datetime import datetime


class Officer(db.Model):

    __tablename__ = "officers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id")
    )

    role = db.Column(
        db.String(100),
        default="officer"
    )

    status = db.Column(
        db.String(50),
        default="active"
    )

    assigned_applications = db.Column(
        db.Integer,
        default=0
    )

    completed_applications = db.Column(
        db.Integer,
        default=0
    )

    risk_activity = db.Column(
        db.String(50),
        default="Low"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user = db.relationship(
        "User",
        backref="officer_profile"
    )

    department = db.relationship(
        "Department",
        backref="officers"
    )