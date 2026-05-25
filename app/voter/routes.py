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
            "You have already voted in this election.",
            "warning"
        )

        return redirect(
            url_for(
                "voter.view_election",
                election_id=election.id
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

    vote = Vote(

        voter_id=current_user.id,

        candidate_id=candidate.id,

        election_id=election.id
    )

    db.session.add(vote)

    candidate.vote_count += 1

    db.session.commit()

    flash(
        "Vote cast successfully!",
        "success"
    )

    return redirect(
        url_for(
            "voter.dashboard"
        )
    )