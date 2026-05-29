from datetime import datetime

from app.extensions import db


class DepartmentOfficer(db.Model):

    __tablename__ = "department_officers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    role = db.Column(
        db.String(100),
        nullable=False
    )

    designation = db.Column(
        db.String(150)
    )

    status = db.Column(
        db.String(50),
        default="active"
    )

    assigned_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    joined_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )