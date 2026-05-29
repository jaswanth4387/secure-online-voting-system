from datetime import datetime


# =========================================
# FORMAT DATETIME
# =========================================

def format_datetime(date):

    if not date:

        return "N/A"

    return date.strftime(
        "%d-%m-%Y %I:%M %p"
    )


# =========================================
# FORMAT DATE
# =========================================

def format_date(date):

    if not date:

        return "N/A"

    return date.strftime(
        "%d-%m-%Y"
    )


# =========================================
# CALCULATE PERCENTAGE
# =========================================

def calculate_percentage(
    part,
    total
):

    if total == 0:

        return 0

    return round(
        (part / total) * 100,
        2
    )


# =========================================
# GENERATE STATUS BADGE
# =========================================

def generate_status_badge(status):

    status = status.lower()

    if status == "approved":

        return "success"

    elif status == "rejected":

        return "danger"

    elif status == "pending":

        return "warning"

    elif status == "active":

        return "primary"

    elif status == "completed":

        return "info"

    return "secondary"


# =========================================
# RISK LEVEL BADGE
# =========================================

def get_risk_badge(risk_level):

    risk_level = risk_level.lower()

    if risk_level == "low":

        return "success"

    elif risk_level == "medium":

        return "warning"

    elif risk_level == "high":

        return "danger"

    elif risk_level == "critical":

        return "dark"

    return "secondary"


# =========================================
# SHORTEN TEXT
# =========================================

def shorten_text(
    text,
    length=100
):

    if not text:

        return ""

    if len(text) <= length:

        return text

    return text[:length] + "..."


# =========================================
# FORMAT LARGE NUMBERS
# =========================================

def format_number(number):

    if number >= 1000000:

        return (
            f"{round(number / 1000000, 1)}M"
        )

    elif number >= 1000:

        return (
            f"{round(number / 1000, 1)}K"
        )

    return str(number)


# =========================================
# GET CURRENT TIMESTAMP
# =========================================

def current_timestamp():

    return datetime.utcnow()


# =========================================
# APPLICATION WORKFLOW LABEL
# =========================================

def workflow_label(status):

    mapping = {

        "Pending":
            "Application Pending",

        "Approved":
            "Application Approved",

        "Rejected":
            "Application Rejected",

        "Assigned to Officer":
            "Assigned to Officer",

        "Forwarded":
            "Forwarded to Department"
    }

    return mapping.get(
        status,
        status
    )


# =========================================
# SECURITY EVENT LABEL
# =========================================

def security_event_label(event):

    labels = {

        "LOGIN_SUCCESS":
            "Successful Login",

        "LOGIN_FAILED":
            "Failed Login Attempt",

        "LOGOUT":
            "User Logout",

        "APPLICATION_ACTION":
            "Application Activity",

        "APPLICATION_FORWARDED":
            "Application Forwarded"
    }

    return labels.get(
        event,
        event
    )


# =========================================
# GET DASHBOARD COLOR
# =========================================

def dashboard_card_color(card_type):

    colors = {

        "primary":
            "bg-primary",

        "success":
            "bg-success",

        "danger":
            "bg-danger",

        "warning":
            "bg-warning",

        "info":
            "bg-info",

        "dark":
            "bg-dark"
    }

    return colors.get(
        card_type,
        "bg-secondary"
    )


# =========================================
# VALIDATE ELECTION STATUS
# =========================================

def validate_election_status(status):

    valid_status = [

        "Upcoming",

        "Active",

        "Completed",

        "Cancelled"
    ]

    return status in valid_status


# =========================================
# GENERATE OFFICER CODE
# =========================================

def generate_officer_code(

    department_name,

    officer_id
):

    prefix = (
        department_name[:3]
        .upper()
    )

    return (
        f"{prefix}-{officer_id}"
    )


# =========================================
# FORMAT ROLE NAME
# =========================================

def format_role_name(role):

    return (
        role
        .replace("_", " ")
        .title()
    )


# =========================================
# GET APPLICATION PROGRESS
# =========================================

def get_application_progress(status):

    progress_map = {

        "Pending": 20,

        "Assigned to Officer": 40,

        "Forwarded": 60,

        "Approved": 100,

        "Rejected": 100
    }

    return progress_map.get(
        status,
        0
    )


# =========================================
# MASK EMAIL
# =========================================

def mask_email(email):

    if not email:

        return ""

    parts = email.split("@")

    username = parts[0]

    domain = parts[1]

    if len(username) <= 2:

        masked = "*" * len(username)

    else:

        masked = (

            username[:2]

            +

            "*" * (
                len(username) - 2
            )
        )

    return f"{masked}@{domain}"


# =========================================
# MASK MOBILE NUMBER
# =========================================

def mask_mobile(mobile):

    if not mobile:

        return ""

    if len(mobile) < 4:

        return "*" * len(mobile)

    return (

        "*" * (len(mobile) - 4)

        +

        mobile[-4:]
    )


# =========================================
# GENERATE SYSTEM MESSAGE
# =========================================

def system_message(
    message,
    level="info"
):

    return {

        "message": message,

        "level": level,

        "timestamp":
            current_timestamp()
    }