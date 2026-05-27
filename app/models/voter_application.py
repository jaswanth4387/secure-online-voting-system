from datetime import datetime

from app.extensions import db


class VoterApplication(db.Model):

    __tablename__ = "voter_applications"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    full_name = db.Column(
        db.String(150),
        nullable=False
    )

    dob = db.Column(
        db.Date,
        nullable=False
    )

    gender = db.Column(
        db.String(20),
        nullable=False
    )

    mobile = db.Column(
        db.String(15),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    address = db.Column(
        db.Text,
        nullable=False
    )

    state = db.Column(
        db.String(100),
        nullable=False
    )

    district = db.Column(
        db.String(100),
        nullable=False
    )

    constituency = db.Column(
        db.String(100),
        nullable=False
    )

    identity_proof = db.Column(
        db.String(255),
        nullable=False
    )

    photo = db.Column(
        db.String(255),
        nullable=False
    )

    # =========================
    # WORKFLOW MANAGEMENT
    # =========================

    status = db.Column(
        db.String(50),
        default="Submitted"
    )

    workflow_stage = db.Column(
        db.String(100),
        default="Submitted"
    )

    current_department = db.Column(
        db.String(100),
        default="Administration"
    )

    remarks = db.Column(
        db.Text
    )

    # =========================
    # VOTER ID MANAGEMENT
    # =========================

    voter_id = db.Column(
        db.String(50),
        unique=True
    )

    # =========================
    # TIMESTAMPS
    # =========================

    submitted_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    forwarded_at = db.Column(
        db.DateTime
    )

    verified_at = db.Column(
        db.DateTime
    )

    # =========================
    # OFFICER TRACKING
    # =========================

    admin_reviewed_by = db.Column(
        db.Integer
    )

    verified_by = db.Column(
        db.Integer
    )