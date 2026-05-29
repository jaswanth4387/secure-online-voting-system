from datetime import datetime

from app.extensions import db


class WorkflowLog(db.Model):

    __tablename__ = "workflow_logs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    application_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "voter_applications.id"
        ),
        nullable=False
    )

    from_department = db.Column(
        db.String(150)
    )

    to_department = db.Column(
        db.String(150)
    )

    action = db.Column(
        db.String(255)
    )

    remarks = db.Column(
        db.Text
    )

    performed_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )