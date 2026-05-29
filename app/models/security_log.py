from datetime import datetime

from app.extensions import db


class SecurityLog(db.Model):

    __tablename__ = "security_logs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    event_type = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    ip_address = db.Column(
        db.String(100)
    )

    user_agent = db.Column(
        db.Text
    )

    risk_level = db.Column(
        db.String(50),
        default="Low"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )