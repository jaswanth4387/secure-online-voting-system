from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import (
    check_password_hash
)

from app.models.user import User

from app.models.department_officer import (
    DepartmentOfficer
)

from app.security_service import (
    create_security_log
)


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


# =========================================
# LOGIN
# =========================================

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

        # =====================================
        # INVALID LOGIN
        # =====================================

        if not user or not check_password_hash(
            user.password_hash,
            password
        ):

            create_security_log(

                None,

                "LOGIN_FAILED",

                (
                    f"Failed login "
                    f"attempt for {email}"
                ),

                "Medium"
            )

            flash(
                "Invalid email or password.",
                "danger"
            )

            return redirect(
                url_for("auth.login")
            )

        # =====================================
        # SUCCESS LOGIN
        # =====================================

        login_user(user)

        create_security_log(

            user.id,

            "LOGIN_SUCCESS",

            f"{user.email} logged in",

            "Low"
        )

        flash(
            "Login successful.",
            "success"
        )

        # =====================================
        # ADMIN LOGIN
        # =====================================

        if user.role == "admin":

            return redirect(
                url_for("admin.dashboard")
            )

        # =====================================
        # DEPARTMENT HEAD LOGIN
        # =====================================

        department_head = (
            DepartmentOfficer.query.filter_by(
                user_id=user.id,
                role="department_head"
            ).first()
        )

        if department_head:

            return redirect(
                url_for(
                    "department.dashboard"
                )
            )

        # =====================================
        # OFFICER LOGIN
        # =====================================

        officer = (
            DepartmentOfficer.query.filter(
                DepartmentOfficer.user_id
                == user.id,

                DepartmentOfficer.role
                != "department_head"
            ).first()
        )

        if officer:

            return redirect(
                url_for(
                    "department.officer_dashboard"
                )
            )

        # =====================================
        # NORMAL VOTER
        # =====================================

        return redirect(
            url_for("public.home")
        )

    return render_template(
        "auth/login.html"
    )


# =========================================
# LOGOUT
# =========================================

@auth_bp.route("/logout")
@login_required
def logout():

    create_security_log(

        current_user.id,

        "LOGOUT",

        f"{current_user.email} logged out",

        "Low"
    )

    logout_user()

    flash(
        "Logged out successfully.",
        "success"
    )

    return redirect(
        url_for("public.home")
    )



@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    return render_template("auth/register.html")