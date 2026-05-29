from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from flask_login import (
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash
)

from app.extensions import db

from app.models.user import User

from app.models.department import (
    Department
)

from app.models.department_officer import (
    DepartmentOfficer
)

from app.models.voter_application import (
    VoterApplication
)

from app.models.workflow_log import (
    WorkflowLog
)

from app.security_service import (
    create_security_log
)


department_bp = Blueprint(
    "department",
    __name__,
    url_prefix="/department"
)


# =========================================
# DEPARTMENT HEAD ACCESS CONTROL
# =========================================

def department_head_required():

    officer = DepartmentOfficer.query.filter_by(
        user_id=current_user.id,
        role="department_head"
    ).first()

    if not officer:

        flash(
            "Unauthorized access.",
            "danger"
        )

        return None

    return officer


# =========================================
# OFFICER ACCESS CONTROL
# =========================================

def officer_required():

    officer = DepartmentOfficer.query.filter_by(
        user_id=current_user.id
    ).first()

    if not officer:

        flash(
            "Unauthorized access.",
            "danger"
        )

        return None

    return officer


# =========================================
# DEPARTMENT DASHBOARD
# =========================================

@department_bp.route("/dashboard")
@login_required
def dashboard():

    officer = department_head_required()

    if not officer:

        return redirect(
            url_for("auth.login")
        )

    department_id = officer.department_id

    department = Department.query.get(
        department_id
    )

    total_officers = (
        DepartmentOfficer.query.filter_by(
            department_id=department_id
        ).count()
    )

    total_applications = (
        VoterApplication.query.filter_by(
            department_id=department_id
        ).count()
    )

    pending_applications = (
        VoterApplication.query.filter_by(
            department_id=department_id,
            status="Pending"
        ).count()
    )

    assigned_applications = (
        VoterApplication.query.filter(
            VoterApplication.department_id
            == department_id,

            VoterApplication.assigned_officer_id
            != None
        ).count()
    )

    return render_template(

        "department/dashboard.html",

        department=department,

        total_officers=total_officers,

        total_applications=total_applications,

        pending_applications=pending_applications,

        assigned_applications=assigned_applications
    )


# =========================================
# OFFICER DASHBOARD
# =========================================

@department_bp.route("/officer/dashboard")
@login_required
def officer_dashboard():

    officer = officer_required()

    if not officer:

        return redirect(
            url_for("auth.login")
        )

    assigned_applications = (
        VoterApplication.query.filter_by(
            assigned_officer_id=current_user.id
        ).all()
    )

    pending_count = (
        VoterApplication.query.filter_by(
            assigned_officer_id=current_user.id,
            status="Pending"
        ).count()
    )

    approved_count = (
        VoterApplication.query.filter_by(
            assigned_officer_id=current_user.id,
            status="Approved"
        ).count()
    )

    rejected_count = (
        VoterApplication.query.filter_by(
            assigned_officer_id=current_user.id,
            status="Rejected"
        ).count()
    )

    return render_template(

        "department/officer_dashboard.html",

        assigned_applications=assigned_applications,

        pending_count=pending_count,

        approved_count=approved_count,

        rejected_count=rejected_count
    )


# =========================================
# DEPARTMENT OFFICERS
# =========================================

@department_bp.route("/officers")
@login_required
def officers():

    officer = department_head_required()

    if not officer:

        return redirect(
            url_for("auth.login")
        )

    department_officers = (
        DepartmentOfficer.query.filter_by(
            department_id=officer.department_id
        ).all()
    )

    return render_template(

        "department/officers.html",

        officers=department_officers
    )


# =========================================
# ADD OFFICER
# =========================================

@department_bp.route(
    "/officers/add",
    methods=["GET", "POST"]
)
@login_required
def add_officer():

    officer = department_head_required()

    if not officer:

        return redirect(
            url_for("auth.login")
        )

    if request.method == "POST":

        full_name = request.form[
            "full_name"
        ]

        email = request.form["email"]

        password = request.form[
            "password"
        ]

        role = request.form["role"]

        designation = request.form[
            "designation"
        ]

        user = User(

            voter_application_id=None,

            full_name=full_name,

            email=email,

            voter_id=f"OFFICER-{email}",

            password_hash=generate_password_hash(
                password
            ),

            role="officer"
        )

        db.session.add(user)

        db.session.commit()

        department_officer = (
            DepartmentOfficer(

                department_id=officer.department_id,

                user_id=user.id,

                role=role,

                designation=designation,

                assigned_by=current_user.id
            )
        )

        db.session.add(
            department_officer
        )

        db.session.commit()

        flash(
            "Officer added successfully.",
            "success"
        )

        return redirect(
            url_for(
                "department.officers"
            )
        )

    return render_template(
        "department/add_officer.html"
    )


# =========================================
# DEPARTMENT APPLICATIONS
# =========================================

@department_bp.route("/applications")
@login_required
def applications():

    officer = department_head_required()

    if not officer:

        return redirect(
            url_for("auth.login")
        )

    applications = (
        VoterApplication.query.filter_by(
            department_id=officer.department_id
        ).order_by(
            VoterApplication.submitted_at.desc()
        ).all()
    )

    return render_template(

        "department/applications.html",

        applications=applications
    )


# =========================================
# ASSIGN APPLICATION
# =========================================

@department_bp.route(
    "/applications/<int:application_id>/assign",
    methods=["GET", "POST"]
)
@login_required
def assign_application(application_id):

    officer = department_head_required()

    if not officer:

        return redirect(
            url_for("auth.login")
        )

    application = (
        VoterApplication.query.get_or_404(
            application_id
        )
    )

    officers = (
        DepartmentOfficer.query.filter(
            DepartmentOfficer.department_id
            == officer.department_id,

            DepartmentOfficer.role
            != "department_head"
        ).all()
    )

    if request.method == "POST":

        assigned_officer_id = request.form[
            "officer_id"
        ]

        application.assigned_officer_id = (
            assigned_officer_id
        )

        application.workflow_status = (
            "Assigned to Officer"
        )

        log = WorkflowLog(

            application_id=application.id,

            from_department="Department Head",

            to_department="Officer Queue",

            action="Application Assigned",

            remarks="Assigned to officer",

            performed_by=current_user.id
        )

        db.session.add(log)

        db.session.commit()

        flash(
            "Application assigned successfully.",
            "success"
        )

        return redirect(
            url_for(
                "department.applications"
            )
        )

    return render_template(

        "department/assign_application.html",

        application=application,

        officers=officers
    )


# =========================================
# REVIEW APPLICATION
# =========================================

@department_bp.route(
    "/applications/<int:application_id>/review",
    methods=["GET", "POST"]
)
@login_required
def review_application(application_id):

    officer = officer_required()

    if not officer:

        return redirect(
            url_for("auth.login")
        )

    application = (
        VoterApplication.query.get_or_404(
            application_id
        )
    )

    departments = Department.query.all()

    if request.method == "POST":

        action = request.form["action"]

        remarks = request.form["remarks"]

        risk_level = request.form[
            "risk_level"
        ]

        application.remarks = remarks

        application.risk_level = risk_level

        # =====================================
        # APPROVE
        # =====================================

        if action == "approve":

            application.status = "Approved"

            application.workflow_status = (
                "Approved"
            )

            create_security_log(

                current_user.id,

                "APPLICATION_ACTION",

                (
                    f"{current_user.email} "
                    f"approved "
                    f"application "
                    f"{application.id}"
                ),

                risk_level
            )

        # =====================================
        # REJECT
        # =====================================

        elif action == "reject":

            application.status = "Rejected"

            application.workflow_status = (
                "Rejected"
            )

            create_security_log(

                current_user.id,

                "APPLICATION_ACTION",

                (
                    f"{current_user.email} "
                    f"rejected "
                    f"application "
                    f"{application.id}"
                ),

                risk_level
            )

        # =====================================
        # FORWARD
        # =====================================

        elif action == "forward":

            department_id = request.form[
                "department_id"
            ]

            next_department = (
                Department.query.get(
                    department_id
                )
            )

            current_department = (
                Department.query.get(
                    application.department_id
                )
            )

            application.department_id = (
                department_id
            )

            application.assigned_officer_id = (
                None
            )

            application.workflow_status = (
                f"Forwarded to "
                f"{next_department.name}"
            )

            log = WorkflowLog(

                application_id=application.id,

                from_department=(
                    current_department.name
                ),

                to_department=(
                    next_department.name
                ),

                action="Forwarded",

                remarks=remarks,

                performed_by=current_user.id
            )

            db.session.add(log)

            create_security_log(

                current_user.id,

                "APPLICATION_FORWARDED",

                (
                    f"{current_user.email} "
                    f"forwarded "
                    f"application "
                    f"{application.id} "
                    f"to "
                    f"{next_department.name}"
                ),

                risk_level
            )

        db.session.commit()

        flash(
            "Application updated successfully.",
            "success"
        )

        return redirect(
            url_for(
                "department.officer_dashboard"
            )
        )

    return render_template(

        "department/review_application.html",

        application=application,

        departments=departments
    )