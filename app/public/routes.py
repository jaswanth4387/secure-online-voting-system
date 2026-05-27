import os

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from werkzeug.utils import secure_filename

from app.extensions import db

from app.models.voter_application import (
    VoterApplication
)


public_bp = Blueprint(
    "public",
    __name__
)


# =========================================
# HOME PAGE
# =========================================

@public_bp.route("/")
def home():

    return render_template(
        "public/index.html"
    )


# =========================================
# ABOUT PAGE
# =========================================

@public_bp.route("/about")
def about():

    return render_template(
        "public/about.html"
    )


# =========================================
# NOTICES
# =========================================

@public_bp.route("/notices")
@public_bp.route("/notices/page/1")
def notices_1():

    return render_template(
        "public/notices_1.html"
    )


@public_bp.route("/notices/page/2")
def notices_2():

    return render_template(
        "public/notices_2.html"
    )


# =========================================
# FORMS PAGE
# =========================================

@public_bp.route("/forms")
def forms():

    return render_template(
        "public/forms.html"
    )


# =========================================
# RESULTS PAGE
# =========================================

@public_bp.route("/results")
def results():

    return render_template(
        "public/results.html"
    )


# =========================================
# FAQ PAGE
# =========================================

@public_bp.route("/faq")
def faq():

    return render_template(
        "public/faq.html"
    )


# =========================================
# CONTACT PAGE
# =========================================

@public_bp.route("/contact")
def contact():

    return render_template(
        "public/contact.html"
    )


# =========================================
# NEW VOTER REGISTRATION FORM
# =========================================

@public_bp.route(
    "/apply-voter-id",
    methods=["GET", "POST"]
)
def apply_voter_id():

    if request.method == "POST":

        # =========================
        # FILES
        # =========================

        identity_file = request.files[
            "identity_proof"
        ]

        photo_file = request.files[
            "photo"
        ]

        identity_filename = secure_filename(
            identity_file.filename
        )

        photo_filename = secure_filename(
            photo_file.filename
        )

        identity_path = os.path.join(
            "app/static/uploads",
            identity_filename
        )

        photo_path = os.path.join(
            "app/static/uploads",
            photo_filename
        )

        identity_file.save(identity_path)

        photo_file.save(photo_path)

        # =========================
        # CREATE APPLICATION
        # =========================

        application = VoterApplication(

            full_name=request.form[
                "full_name"
            ],

            dob=request.form[
                "dob"
            ],

            gender=request.form[
                "gender"
            ],

            mobile=request.form[
                "mobile"
            ],

            email=request.form[
                "email"
            ],

            address=request.form[
                "address"
            ],

            state=request.form[
                "state"
            ],

            district=request.form[
                "district"
            ],

            constituency=request.form[
                "constituency"
            ],

            identity_proof=identity_filename,

            photo=photo_filename,

            # =====================
            # WORKFLOW MANAGEMENT
            # =====================

            status="Submitted",

            workflow_stage="Submitted",

            current_department="Administration"
        )

        db.session.add(application)

        db.session.commit()

        flash(
            "Application submitted successfully and forwarded to Administration Department.",
            "success"
        )

        return redirect(
            url_for("public.home")
        )

    return render_template(
        "public/apply_voter_id.html"
    )


# =========================================
# NEW VOTER FORM PAGE
# =========================================

@public_bp.route("/new_voter_form")
def new_voter_form():

    return render_template(
        "public/new_voter_form.html"
    )