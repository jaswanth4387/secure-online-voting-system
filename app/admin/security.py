from app.models.security_log import (
    SecurityLog
)

from app.models.user import User

from app.models.department_officer import (
    DepartmentOfficer
)

from app.models.voter_application import (
    VoterApplication
)

from app.models.workflow_log import (
    WorkflowLog
)

from app.models.election import (
    Election
)

from app.models.election_vote import (
    ElectionVote
)

from app.models.candidate import (
    Candidate
)


# =========================================
# RECENT SECURITY LOGS
# =========================================

def get_recent_security_logs():

    return (
        SecurityLog.query.order_by(
            SecurityLog.created_at.desc()
        ).limit(100).all()
    )


# =========================================
# HIGH RISK ALERTS
# =========================================

def get_high_risk_alerts():

    return (
        SecurityLog.query.filter(
            SecurityLog.risk_level.in_([
                "High",
                "Critical"
            ])
        ).order_by(
            SecurityLog.created_at.desc()
        ).all()
    )


# =========================================
# FAILED LOGIN ATTEMPTS
# =========================================

def get_failed_login_attempts():

    return (
        SecurityLog.query.filter_by(
            event_type="LOGIN_FAILED"
        ).order_by(
            SecurityLog.created_at.desc()
        ).all()
    )


# =========================================
# SUCCESSFUL LOGIN EVENTS
# =========================================

def get_successful_logins():

    return (
        SecurityLog.query.filter_by(
            event_type="LOGIN_SUCCESS"
        ).order_by(
            SecurityLog.created_at.desc()
        ).all()
    )


# =========================================
# LOGOUT EVENTS
# =========================================

def get_logout_events():

    return (
        SecurityLog.query.filter_by(
            event_type="LOGOUT"
        ).order_by(
            SecurityLog.created_at.desc()
        ).all()
    )


# =========================================
# APPLICATION SECURITY EVENTS
# =========================================

def get_application_security_events():

    return (
        SecurityLog.query.filter(
            SecurityLog.event_type.in_([
                "APPLICATION_ACTION",
                "APPLICATION_FORWARDED"
            ])
        ).order_by(
            SecurityLog.created_at.desc()
        ).all()
    )


# =========================================
# SECURITY DASHBOARD STATS
# =========================================

def get_security_dashboard_stats():

    stats = {

        "total_logs":
            SecurityLog.query.count(),

        "low_risk":
            SecurityLog.query.filter_by(
                risk_level="Low"
            ).count(),

        "medium_risk":
            SecurityLog.query.filter_by(
                risk_level="Medium"
            ).count(),

        "high_risk":
            SecurityLog.query.filter_by(
                risk_level="High"
            ).count(),

        "critical_risk":
            SecurityLog.query.filter_by(
                risk_level="Critical"
            ).count(),

        "failed_logins":
            SecurityLog.query.filter_by(
                event_type="LOGIN_FAILED"
            ).count(),

        "successful_logins":
            SecurityLog.query.filter_by(
                event_type="LOGIN_SUCCESS"
            ).count(),

        "application_events":
            SecurityLog.query.filter(
                SecurityLog.event_type.in_([
                    "APPLICATION_ACTION",
                    "APPLICATION_FORWARDED"
                ])
            ).count()
    }

    return stats


# =========================================
# GET USER SECURITY HISTORY
# =========================================

def get_user_security_history(
    user_id
):

    return (
        SecurityLog.query.filter_by(
            user_id=user_id
        ).order_by(
            SecurityLog.created_at.desc()
        ).all()
    )


# =========================================
# DETECT SUSPICIOUS USERS
# =========================================

def detect_suspicious_users():

    suspicious_users = []

    users = User.query.all()

    for user in users:

        failed_attempts = (
            SecurityLog.query.filter_by(
                user_id=user.id,
                event_type="LOGIN_FAILED"
            ).count()
        )

        if failed_attempts >= 5:

            suspicious_users.append({

                "user":
                    user,

                "failed_attempts":
                    failed_attempts
            })

    return suspicious_users


# =========================================
# DETECT HIGH RISK APPLICATIONS
# =========================================

def get_high_risk_applications():

    return (
        VoterApplication.query.filter(
            VoterApplication.risk_level.in_([
                "High",
                "Critical"
            ])
        ).all()
    )


# =========================================
# GET SECURITY EVENT COUNTS
# =========================================

def get_security_event_counts():

    events = [

        "LOGIN_SUCCESS",

        "LOGIN_FAILED",

        "LOGOUT",

        "APPLICATION_ACTION",

        "APPLICATION_FORWARDED"
    ]

    counts = {}

    for event in events:

        counts[event] = (
            SecurityLog.query.filter_by(
                event_type=event
            ).count()
        )

    return counts


# =========================================
# GET SYSTEM SECURITY OVERVIEW
# =========================================

def get_system_security_overview():

    overview = {

        "users":
            User.query.count(),

        "officers":
            DepartmentOfficer.query.count(),

        "applications":
            VoterApplication.query.count(),

        "workflow_logs":
            WorkflowLog.query.count(),

        "security_logs":
            SecurityLog.query.count(),

        "elections":
            Election.query.count(),

        "votes":
            ElectionVote.query.count(),

        "candidates":
            Candidate.query.count()
    }

    return overview


# =========================================
# DETECT ABNORMAL ACTIVITY
# =========================================

def detect_abnormal_activity():

    abnormal_logs = []

    logs = SecurityLog.query.all()

    for log in logs:

        if log.risk_level in [

            "High",

            "Critical"
        ]:

            abnormal_logs.append(log)

    return abnormal_logs


# =========================================
# GET LATEST FRAUD ALERTS
# =========================================

def get_latest_fraud_alerts():

    return (
        SecurityLog.query.filter(
            SecurityLog.risk_level.in_([
                "High",
                "Critical"
            ])
        ).order_by(
            SecurityLog.created_at.desc()
        ).limit(20).all()
    )


# =========================================
# GET OFFICER SECURITY ACTIVITY
# =========================================

def get_officer_security_activity():

    officers = (
        DepartmentOfficer.query.all()
    )

    activity = []

    for officer in officers:

        logs = (
            SecurityLog.query.filter_by(
                user_id=officer.user_id
            ).count()
        )

        activity.append({

            "officer":
                officer,

            "logs":
                logs
        })

    return activity