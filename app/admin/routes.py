from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
import os

from werkzeug.utils import secure_filename

from app.models.candidate import Candidate

from flask_login import login_required

from app.extensions import db

from app.models.election import Election
from app.models.vote import Vote
from app.models.candidate import Candidate


admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


@admin_bp.route("/dashboard")
@login_required
def dashboard():

    elections = Election.query.all()

    return render_template(
        "admin/dashboard.html",
        elections=elections
    )


@admin_bp.route(
    "/create-election",
    methods=["GET", "POST"]
)
@login_required
def create_election():

    if request.method == "POST":

        election = Election(

            title=request.form["title"],

            description=request.form["description"],

            election_type=request.form["election_type"],

            constituency=request.form["constituency"],

            start_datetime=request.form[
                "start_datetime"
            ],

            end_datetime=request.form[
                "end_datetime"
            ]
        )

        db.session.add(election)

        db.session.commit()

        flash(
            "Election created successfully!",
            "success"
        )

        return redirect(
            url_for("admin.dashboard")
        )

    return render_template(
        "admin/create_election.html"
    )
@admin_bp.route(
    "/add-candidate",
    methods=["GET", "POST"]
)
@login_required
def add_candidate():

    elections = Election.query.all()

    if request.method == "POST":

        symbol_file = request.files["symbol_image"]

        filename = secure_filename(
            symbol_file.filename
        )

        upload_path = os.path.join(
            "app/static/uploads",
            filename
        )

        symbol_file.save(upload_path)

        candidate = Candidate(

            full_name=request.form["full_name"],

            party_name=request.form["party_name"],

            bio=request.form["bio"],

            election_id=request.form[
                "election_id"
            ],

            constituency=request.form[
                "constituency"
            ],

            symbol_image=filename
        )

        db.session.add(candidate)

        db.session.commit()

        flash(
            "Candidate added successfully!",
            "success"
        )

        return redirect(
            url_for("admin.candidates")
        )

    return render_template(
        "admin/add_candidate.html",
        elections=elections
    )

@admin_bp.route("/candidates")
@login_required
def candidates():

    candidates = Candidate.query.all()

    return render_template(
        "admin/candidates.html",
        candidates=candidates
    )

@admin_bp.route("/results")
@login_required
def results():

    elections = Election.query.all()

    results_data = []

    for election in elections:

        candidates = Candidate.query.filter_by(
            election_id=election.id
        ).all()

        total_votes = sum(
            candidate.vote_count
            for candidate in candidates
        )

        winner = None

        if candidates:

            winner = max(
                candidates,
                key=lambda c: c.vote_count
            )

        candidate_results = []

        for candidate in candidates:

            percentage = 0

            if total_votes > 0:

                percentage = round(
                    (
                        candidate.vote_count
                        / total_votes
                    ) * 100,
                    2
                )

            candidate_results.append({

                "candidate": candidate,

                "percentage": percentage
            })

        results_data.append({

            "election": election,

            "total_votes": total_votes,

            "winner": winner,

            "candidate_results": candidate_results
        })

    return render_template(
        "admin/results.html",
        results_data=results_data
    )