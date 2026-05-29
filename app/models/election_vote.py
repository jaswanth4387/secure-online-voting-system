from datetime import datetime

from app.extensions import db


class ElectionVote(db.Model):

    __tablename__ = "election_votes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    election_id = db.Column(
        db.Integer,
        db.ForeignKey("elections.id"),
        nullable=False
    )

    candidate_id = db.Column(
        db.Integer,
        db.ForeignKey("candidates.id"),
        nullable=False
    )

    voter_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    voted_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )