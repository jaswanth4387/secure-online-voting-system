from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from app.extensions import db

from app.models.election import (
    Election
)


election_bp = Blueprint(
    "election",
    __name__,
    url_prefix="/admin/elections"
)


# =========================================
# ELECTION LIST
# =========================================

@election_bp.route("/")
@login_required
def elections():

    elections = (
        Election.query.order_by(
            Election.created_at.desc()
        ).all()
    )

    return render_template(

        "admin/elections.html",

        elections=elections
    )


# =========================================
# CREATE ELECTION
# =========================================

@election_bp.route(
    "/create",
    methods=["GET", "POST"]
)
@login_required
def create_election():

    if request.method == "POST":

        election = Election(

            title=request.form["title"],

            description=request.form[
                "description"
            ],

            election_type=request.form[
                "election_type"
            ],

            start_date=request.form[
                "start_date"
            ],

            end_date=request.form[
                "end_date"
            ],

            created_by=current_user.id
        )

        db.session.add(election)

        db.session.commit()

        flash(
            "Election created successfully.",
            "success"
        )

        return redirect(
            url_for("election.elections")
        )

    return render_template(
        "admin/create_election.html"
    )