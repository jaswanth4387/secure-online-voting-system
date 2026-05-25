from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
import random
from app.extensions import db

from werkzeug.security import (
    check_password_hash
)

from flask_login import (
    login_user,
    login_required,
    logout_user
)

from app.models.department_officer import (
    DepartmentOfficer
)

department_bp = Blueprint(
    "department",
    __name__,
    url_prefix="/department"
)


@department_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        officer = DepartmentOfficer.query.filter_by(
            email=email
        ).first()

        if officer and check_password_hash(
            officer.password_hash,
            password
        ):

            login_user(officer)

            flash(
                "Login successful!",
                "success"
            )

            return redirect(
                url_for(
                    "department.dashboard"
                )
            )

        flash(
            "Invalid credentials",
            "danger"
        )

    return render_template(
        "department/login.html"
    )

@department_bp.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "department/dashboard.html"
    )

from app.models.voter_application import (
    VoterApplication
)


@department_bp.route("/applications")
@login_required
def applications():

    pending_applications = (
        VoterApplication.query
        .order_by(
            VoterApplication.submitted_at.desc()
        )
        .all()
    )

    return render_template(
        "department/applications.html",
        applications=pending_applications
    )

@department_bp.route(
    "/application/<int:application_id>"
)
@login_required
def view_application(application_id):

    application = (
        VoterApplication.query.get_or_404(
            application_id
        )
    )

    return render_template(
        "department/view_application.html",
        application=application
    )

def generate_voter_id():

    random_number = random.randint(
        100000,
        999999
    )

    return f"JANVOTE{random_number}"

@department_bp.route(
    "/approve/<int:application_id>"
)
@login_required
def approve_application(application_id):

    application = (
        VoterApplication.query.get_or_404(
            application_id
        )
    )

    application.status = "Approved"

    application.voter_id = generate_voter_id()

    db.session.commit()

    flash(
        "Application approved successfully!",
        "success"
    )

    return redirect(
        url_for(
            "department.applications"
        )
    )

@department_bp.route(
    "/reject/<int:application_id>"
)
@login_required
def reject_application(application_id):

    application = (
        VoterApplication.query.get_or_404(
            application_id
        )
    )

    application.status = "Rejected"

    db.session.commit()

    flash(
        "Application rejected!",
        "danger"
    )

    return redirect(
        url_for(
            "department.applications"
        )
    )