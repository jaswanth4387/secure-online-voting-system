from app.extensions import db


class Candidate(db.Model):

    __tablename__ = "candidates"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    full_name = db.Column(
        db.String(150),
        nullable=False
    )

    party_name = db.Column(
        db.String(150),
        nullable=False
    )

    symbol_image = db.Column(
        db.String(255)
    )

    bio = db.Column(
        db.Text
    )

    election_id = db.Column(
        db.Integer,
        db.ForeignKey("elections.id"),
        nullable=False
    )

    constituency = db.Column(
        db.String(100),
        nullable=False
    )

    vote_count = db.Column(
        db.Integer,
        default=0
    )