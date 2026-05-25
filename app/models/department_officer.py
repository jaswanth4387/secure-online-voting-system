from app.extensions import db
from flask_login import UserMixin


class DepartmentOfficer(UserMixin, db.Model):

    __tablename__ = "department_officers"

    id = db.Column(db.Integer, primary_key=True)

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

    department_name = db.Column(
        db.String(100),
        nullable=False
    )

    role = db.Column(
        db.String(50),
        default="verification_officer"
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )