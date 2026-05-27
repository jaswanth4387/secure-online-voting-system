from datetime import datetime

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from app.extensions import db

from app.models.election import Election

from app.models.candidate import Candidate

from app.models.vote import Vote
import random
from flask import session
from flask_mail import Message
from app.extensions import mail


def generate_vote_otp():

    return str(
        random.randint(100000, 999999)
    )

voter_bp = Blueprint(
    "voter",
    __name__,
    url_prefix="/voter"
)


@voter_bp.route("/dashboard")
@login_required
def dashboard():

    active_elections = Election.query.filter_by(
        status="Active"
    ).all()

    return render_template(
        "voter/dashboard.html",
        elections=active_elections
    )


@voter_bp.route(
    "/election/<int:election_id>"
)
@login_required
def view_election(election_id):

    election = Election.query.get_or_404(
        election_id
    )

    candidates = Candidate.query.filter_by(
        election_id=election.id
    ).all()

    existing_vote = Vote.query.filter_by(
        voter_id=current_user.id,
        election_id=election.id
    ).first()

    return render_template(
        "voter/view_election.html",
        election=election,
        candidates=candidates,
        existing_vote=existing_vote
    )


@voter_bp.route(
    "/vote/<int:candidate_id>"
)
@login_required
def cast_vote(candidate_id):

    candidate = Candidate.query.get_or_404(
        candidate_id
    )

    election = Election.query.get_or_404(
        candidate.election_id
    )

    existing_vote = Vote.query.filter_by(
        voter_id=current_user.id,
        election_id=election.id
    ).first()

    if existing_vote:

        flash(
            "You have already voted.",
            "warning"
        )

        return redirect(
            url_for(
                "voter.dashboard"
            )
        )

    current_time = datetime.utcnow()

    if (
        current_time < election.start_datetime
        or
        current_time > election.end_datetime
    ):

        flash(
            "Voting is not active.",
            "danger"
        )

        return redirect(
            url_for(
                "voter.dashboard"
            )
        )

    otp = generate_vote_otp()

    session["vote_otp"] = otp

    session["pending_vote"] = {

        "candidate_id": candidate.id,

        "election_id": election.id
    }

    send_vote_otp(
        current_user.email,
        otp
    )

    flash(
        "OTP sent to your email.",
        "info"
    )

    return redirect(
        url_for(
            "voter.verify_vote_otp"
        )
    )

@voter_bp.route(
    "/verify-vote-otp",
    methods=["GET", "POST"]
)
@login_required
def verify_vote_otp():

    if request.method == "POST":

        entered_otp = request.form["otp"]

        stored_otp = session.get(
            "vote_otp"
        )

        pending_vote = session.get(
            "pending_vote"
        )

        if entered_otp == stored_otp:

            vote = Vote(

                voter_id=current_user.id,

                candidate_id=pending_vote[
                    "candidate_id"
                ],

                election_id=pending_vote[
                    "election_id"
                ]
            )

            db.session.add(vote)

            candidate = Candidate.query.get(
                pending_vote["candidate_id"]
            )

            candidate.vote_count += 1

            db.session.commit()

            session.pop(
                "vote_otp",
                None
            )

            session.pop(
                "pending_vote",
                None
            )

            flash(
                "Vote cast successfully!",
                "success"
            )

            return redirect(
                url_for(
                    "voter.dashboard"
                )
            )

        flash(
            "Invalid OTP",
            "danger"
        )

    return render_template(
        "voter/verify_vote_otp.html"
    )

def send_vote_otp(email, otp):

    msg = Message(

        subject="JanVote Vote Verification OTP",

        sender="your_email@gmail.com",

        recipients=[email]
    )

    msg.body = f"""

Your OTP for vote confirmation is:

{otp}

Do not share this OTP with anyone.

"""

    mail.send(msg)