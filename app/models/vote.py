from datetime import datetime

from app.extensions import db


class Vote(db.Model):

    __tablename__ = "votes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    voter_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    candidate_id = db.Column(
        db.Integer,
        db.ForeignKey("candidates.id"),
        nullable=False
    )

    election_id = db.Column(
        db.Integer,
        db.ForeignKey("elections.id"),
        nullable=False
    )

    voted_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )