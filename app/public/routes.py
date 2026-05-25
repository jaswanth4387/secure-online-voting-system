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
from app.models.voter_application import VoterApplication


public_bp = Blueprint(
    "public",
    __name__
)


@public_bp.route("/")
def home():
    return render_template("public/index.html")


@public_bp.route(
    "/apply-voter-id",
    methods=["GET", "POST"]
)
def apply_voter_id():

    if request.method == "POST":

        identity_file = request.files["identity_proof"]
        photo_file = request.files["photo"]

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

        application = VoterApplication(

            full_name=request.form["full_name"],

            dob=request.form["dob"],

            gender=request.form["gender"],

            mobile=request.form["mobile"],

            email=request.form["email"],

            address=request.form["address"],

            state=request.form["state"],

            district=request.form["district"],

            constituency=request.form["constituency"],

            identity_proof=identity_filename,

            photo=photo_filename
        )

        db.session.add(application)
        db.session.commit()

        flash(
            "Application submitted successfully!",
            "success"
        )

        return redirect(
            url_for("public.home")
        )

    return render_template(
        "public/apply_voter_id.html"
    )