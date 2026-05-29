from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash
)

from app.extensions import db

from app.models.department import (
    Department
)

from app.models.department_officer import (
    DepartmentOfficer
)
from app.models.officer import Officer


from app.models.user import User

from app.models.voter_application import (
    VoterApplication
)

from app.models.security_log import (
    SecurityLog
)

from app.admin.permissions import (
    admin_required
)

from app.admin.services import (
    get_dashboard_statistics
)

from app.admin.analytics import (
    get_department_analytics
)

from app.admin.security import (
    get_recent_security_logs,
    get_high_risk_alerts
)


admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


# =========================================
# ADMIN DASHBOARD
# =========================================

@admin_bp.route("/dashboard")
@login_required
def dashboard():

    if not admin_required():

        flash(
            "Unauthorized access.",
            "danger"
        )

        return redirect(
            url_for("auth.login")
        )

    statistics = (
        get_dashboard_statistics()
    )

    return render_template(

        "admin/dashboard.html",

        statistics=statistics
    )


# =========================================
# DEPARTMENTS
# =========================================

@admin_bp.route("/departments")
@login_required
def departments():

    if not admin_required():

        return redirect(
            url_for("auth.login")
        )

    departments = Department.query.order_by(
        Department.created_at.desc()
    ).all()

    return render_template(

        "admin/departments.html",

        departments=departments
    )


# =========================================
# CREATE DEPARTMENT
# =========================================

@admin_bp.route(
    "/departments/create",
    methods=["GET", "POST"]
)
@login_required
def create_department():

    if not admin_required():

        return redirect(
            url_for("auth.login")
        )

    if request.method == "POST":

        # =====================================
        # CREATE DEPARTMENT
        # =====================================

        department = Department(

            name=request.form[
                "department_name"
            ],

            description=request.form[
                "description"
            ],

            status="active"
        )

        db.session.add(department)

        db.session.commit()

        # =====================================
        # CREATE DEPARTMENT HEAD USER
        # =====================================

        user = User(

            voter_application_id=None,

            full_name=request.form[
                "full_name"
            ],

            email=request.form[
                "email"
            ],

            voter_id=(
                f"HEAD-{department.id}"
            ),

            password_hash=(
                generate_password_hash(
                    request.form["password"]
                )
            ),

            role="department_head"
        )

        db.session.add(user)

        db.session.commit()

        # =====================================
        # CREATE DEPARTMENT OFFICER
        # =====================================

        officer = DepartmentOfficer(

            department_id=department.id,

            user_id=user.id,

            role="department_head",

            designation=request.form[
                "designation"
            ],

            status="active",

            assigned_by=current_user.id
        )

        db.session.add(officer)

        db.session.commit()

        flash(
            "Department created successfully.",
            "success"
        )

        return redirect(
            url_for("admin.departments")
        )

    return render_template(
        "admin/create_department.html"
    )


# =========================================
# OFFICERS
# =========================================

@admin_bp.route("/officers")
@login_required
def officers():

    if not admin_required():

        return redirect(
            url_for("auth.login")
        )

    officers = (
        DepartmentOfficer.query.order_by(
            DepartmentOfficer.id.desc()
        ).all()
    )

    return render_template(

        "admin/officers.html",

        officers=officers
    )


# =========================================
# APPLICATIONS
# =========================================

@admin_bp.route("/applications")
@login_required
def applications():

    if not admin_required():

        return redirect(
            url_for("auth.login")
        )

    applications = (
        VoterApplication.query.order_by(
            VoterApplication.submitted_at.desc()
        ).all()
    )

    return render_template(

        "admin/applications.html",

        applications=applications
    )


# =========================================
# SECURITY DASHBOARD
# =========================================

@admin_bp.route("/security")
@login_required
def security_dashboard():

    if not admin_required():

        return redirect(
            url_for("auth.login")
        )

    logs = (
        get_recent_security_logs()
    )

    alerts = (
        get_high_risk_alerts()
    )

    high_risk_count = (
        SecurityLog.query.filter_by(
            risk_level="High"
        ).count()
    )

    critical_risk_count = (
        SecurityLog.query.filter_by(
            risk_level="Critical"
        ).count()
    )

    return render_template(

        "admin/security_dashboard.html",

        logs=logs,

        alerts=alerts,

        high_risk_count=high_risk_count,

        critical_risk_count=critical_risk_count
    )


# =========================================
# ANALYTICS DASHBOARD
# =========================================

@admin_bp.route("/analytics")
@login_required
def analytics_dashboard():

    if not admin_required():

        return redirect(
            url_for("auth.login")
        )

    analytics = (
        get_department_analytics()
    )

    return render_template(

        "admin/analytics_dashboard.html",

        analytics=analytics
    )


# =========================================
# WORKFLOW MONITOR
# =========================================

@admin_bp.route("/workflow-monitor")
@login_required
def workflow_monitor():

    if not admin_required():

        return redirect(
            url_for("auth.login")
        )

    applications = (
        VoterApplication.query.order_by(
            VoterApplication.submitted_at.desc()
        ).all()
    )

    return render_template(

        "admin/workflow_monitor.html",

        applications=applications
    )


# =========================================
# FRAUD ALERTS
# =========================================

@admin_bp.route("/fraud-alerts")
@login_required
def fraud_alerts():

    if not admin_required():

        return redirect(
            url_for("auth.login")
        )

    alerts = (
        SecurityLog.query.filter(
            SecurityLog.risk_level.in_([
                "High",
                "Critical"
            ])
        ).order_by(
            SecurityLog.created_at.desc()
        ).all()
    )

    return render_template(

        "admin/fraud_alerts.html",

        alerts=alerts
    )


# =========================================
# SYSTEM LOGS
# =========================================

@admin_bp.route("/system-logs")
@login_required
def system_logs():

    if not admin_required():

        return redirect(
            url_for("auth.login")
        )

    logs = (
        SecurityLog.query.order_by(
            SecurityLog.created_at.desc()
        ).all()
    )

    return render_template(

        "admin/system_logs.html",

        logs=logs
    )

# =========================================
# OFFICER MONITORING
# =========================================

@admin_bp.route("/officer-monitoring")
@login_required
def officer_monitoring():

    # Admin Protection
    if current_user.role != "admin":

        flash(
            "Unauthorized access",
            "danger"
        )

        return redirect(
            url_for("auth.login")
        )

    officers = Officer.query.all()

    departments_count = Department.query.count()

    return render_template(
        "admin/officer_monitoring.html",
        officers=officers,
        departments_count=departments_count
    )