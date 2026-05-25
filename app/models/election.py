from datetime import datetime

from app.extensions import db


class Election(db.Model):

    __tablename__ = "elections"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    election_type = db.Column(
        db.String(100),
        nullable=False
    )

    constituency = db.Column(
        db.String(100),
        nullable=False
    )

    start_datetime = db.Column(
        db.DateTime,
        nullable=False
    )

    end_datetime = db.Column(
        db.DateTime,
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="Draft"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )