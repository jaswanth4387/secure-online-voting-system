from flask_login import current_user

from app.models.department_officer import (
    DepartmentOfficer
)

from app.models.department import (
    Department
)


# =========================================
# ADMIN ACCESS
# =========================================

def admin_required():

    return (

        current_user.is_authenticated

        and

        current_user.role == "admin"
    )


# =========================================
# DEPARTMENT HEAD ACCESS
# =========================================

def department_head_required():

    if not current_user.is_authenticated:

        return False

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id,

        role="department_head"

    ).first()

    return officer is not None


# =========================================
# OFFICER ACCESS
# =========================================

def officer_required():

    if not current_user.is_authenticated:

        return False

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id

    ).first()

    return officer is not None


# =========================================
# CHECK DEPARTMENT ACCESS
# =========================================

def has_department_access(
    department_id
):

    if not current_user.is_authenticated:

        return False

    # =====================================
    # ADMIN HAS FULL ACCESS
    # =====================================

    if current_user.role == "admin":

        return True

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id,

        department_id=department_id

    ).first()

    return officer is not None


# =========================================
# CHECK IF USER IS
# DEPARTMENT HEAD
# =========================================

def is_department_head():

    if not current_user.is_authenticated:

        return False

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id,

        role="department_head"

    ).first()

    return officer is not None


# =========================================
# CHECK IF USER IS OFFICER
# =========================================

def is_officer():

    if not current_user.is_authenticated:

        return False

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id

    ).first()

    return officer is not None


# =========================================
# CHECK ELECTION PERMISSION
# =========================================

def can_manage_elections():

    if not current_user.is_authenticated:

        return False

    # =====================================
    # ADMIN CAN MANAGE
    # =====================================

    if current_user.role == "admin":

        return True

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id

    ).first()

    if not officer:

        return False

    department = Department.query.get(
        officer.department_id
    )

    if not department:

        return False

    return department.name.lower() == (
        "election"
    )


# =========================================
# CHECK SECURITY PERMISSION
# =========================================

def can_view_security_logs():

    if not current_user.is_authenticated:

        return False

    # =====================================
    # ADMIN CAN VIEW
    # =====================================

    if current_user.role == "admin":

        return True

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id

    ).first()

    if not officer:

        return False

    department = Department.query.get(
        officer.department_id
    )

    if not department:

        return False

    return department.name.lower() in [

        "security",

        "security & monitoring"
    ]


# =========================================
# CHECK INVESTIGATION ACCESS
# =========================================

def can_investigate():

    if not current_user.is_authenticated:

        return False

    if current_user.role == "admin":

        return True

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id

    ).first()

    if not officer:

        return False

    department = Department.query.get(
        officer.department_id
    )

    if not department:

        return False

    return department.name.lower() in [

        "investigation",

        "investigation department"
    ]


# =========================================
# CHECK RESULTS ACCESS
# =========================================

def can_publish_results():

    if not current_user.is_authenticated:

        return False

    if current_user.role == "admin":

        return True

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id

    ).first()

    if not officer:

        return False

    department = Department.query.get(
        officer.department_id
    )

    if not department:

        return False

    return department.name.lower() in [

        "results",

        "results & counting"
    ]


# =========================================
# CHECK COMPLAINT ACCESS
# =========================================

def can_manage_complaints():

    if not current_user.is_authenticated:

        return False

    if current_user.role == "admin":

        return True

    officer = DepartmentOfficer.query.filter_by(

        user_id=current_user.id

    ).first()

    if not officer:

        return False

    department = Department.query.get(
        officer.department_id
    )

    if not department:

        return False

    return department.name.lower() in [

        "complaint",

        "complaint & grievance"
    ]