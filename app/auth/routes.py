from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

import random
from flask import session
from flask_mail import Message
from app.extensions import mail

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_login import (
    login_user,
    logout_user,
    login_required
)

from app.extensions import db

from app.models.user import User

from app.models.voter_application import (
    VoterApplication
)


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route(
    "/register",
    methods=["GET", "POST"]
)

def register():

    if request.method == "POST":

        voter_id = request.form["voter_id"]

        email = request.form["email"]

        password = request.form["password"]

        application = (
            VoterApplication.query.filter_by(
                voter_id=voter_id,
                status="Approved"
            ).first()
        )

        if not application:

            flash(
                "Invalid or unapproved voter ID",
                "danger"
            )

            return redirect(
                url_for("auth.register")
            )

        existing_user = User.query.filter_by(
            voter_id=voter_id
        ).first()

        if existing_user:

            flash(
                "Account already exists",
                "warning"
            )

            return redirect(
                url_for("auth.login")
            )

        # -----------------------------
        # ADD OTP CODE HERE
        # -----------------------------

        otp = generate_otp()

        session["registration_otp"] = otp

        session["registration_data"] = {

            "voter_application_id": application.id,

            "voter_id": application.voter_id,

            "full_name": application.full_name,

            "email": email,

            "password": password
        }

        send_otp_email(email, otp)

        flash(
            "OTP sent to your email.",
            "info"
        )

        return redirect(
            url_for("auth.verify_otp")
        )

    return render_template(
        "auth/register.html"
    )

@auth_bp.route(
    "/verify-otp",
    methods=["GET", "POST"]
)
def verify_otp():

    if request.method == "POST":

        entered_otp = request.form["otp"]

        stored_otp = session.get(
            "registration_otp"
        )

        registration_data = session.get(
            "registration_data"
        )

        if entered_otp == stored_otp:

            new_user = User(

                voter_application_id=registration_data[
                    "voter_application_id"
                ],

                voter_id=registration_data[
                    "voter_id"
                ],

                full_name=registration_data[
                    "full_name"
                ],

                email=registration_data[
                    "email"
                ],

                password_hash=generate_password_hash(
                    registration_data["password"]
                )
            )

            db.session.add(new_user)

            db.session.commit()

            session.pop(
                "registration_otp",
                None
            )

            session.pop(
                "registration_data",
                None
            )

            flash(
                "Registration successful!",
                "success"
            )

            return redirect(
                url_for("auth.login")
            )

        flash(
            "Invalid OTP",
            "danger"
        )

    return render_template(
        "auth/verify_otp.html"
    )


@auth_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
            user.password_hash,
            password
        ):

            login_user(user)

            flash(
                "Login successful!",
                "success"
            )

            return redirect(
                url_for("voter.dashboard")
            )

        flash(
            "Invalid credentials",
            "danger"
        )

    return render_template(
        "auth/login.html"
    )

def generate_otp():

    return str(
        random.randint(100000, 999999)
    )

def send_otp_email(email, otp):

    msg = Message(

        subject="JanVote OTP Verification",

        sender="your_email@gmail.com",

        recipients=[email]
    )

    msg.body = f"""

Your OTP for JanVote registration is:

{otp}

Do not share this OTP with anyone.

"""

    mail.send(msg)

