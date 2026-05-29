from app.models.department import (
    Department
)

from app.models.department_officer import (
    DepartmentOfficer
)

from app.models.voter_application import (
    VoterApplication
)

from app.models.election import (
    Election
)

from app.models.candidate import (
    Candidate
)

from app.models.election_vote import (
    ElectionVote
)

from app.models.security_log import (
    SecurityLog
)


# =========================================
# DEPARTMENT ANALYTICS
# =========================================

def get_department_analytics():

    departments = Department.query.all()

    analytics = []

    for department in departments:

        total_officers = (
            DepartmentOfficer.query.filter_by(
                department_id=department.id
            ).count()
        )

        total_applications = (
            VoterApplication.query.filter_by(
                department_id=department.id
            ).count()
        )

        approved_applications = (
            VoterApplication.query.filter_by(
                department_id=department.id,
                status="Approved"
            ).count()
        )

        rejected_applications = (
            VoterApplication.query.filter_by(
                department_id=department.id,
                status="Rejected"
            ).count()
        )

        pending_applications = (
            VoterApplication.query.filter_by(
                department_id=department.id,
                status="Pending"
            ).count()
        )

        analytics.append({

            "department":
                department.name,

            "officers":
                total_officers,

            "applications":
                total_applications,

            "approved":
                approved_applications,

            "rejected":
                rejected_applications,

            "pending":
                pending_applications
        })

    return analytics


# =========================================
# APPLICATION ANALYTICS
# =========================================

def get_application_analytics():

    total = (
        VoterApplication.query.count()
    )

    approved = (
        VoterApplication.query.filter_by(
            status="Approved"
        ).count()
    )

    rejected = (
        VoterApplication.query.filter_by(
            status="Rejected"
        ).count()
    )

    pending = (
        VoterApplication.query.filter_by(
            status="Pending"
        ).count()
    )

    return {

        "total":
            total,

        "approved":
            approved,

        "rejected":
            rejected,

        "pending":
            pending
    }


# =========================================
# OFFICER ANALYTICS
# =========================================

def get_officer_analytics():

    officers = (
        DepartmentOfficer.query.all()
    )

    analytics = []

    for officer in officers:

        assigned_applications = (
            VoterApplication.query.filter_by(
                assigned_officer_id=
                officer.user_id
            ).count()
        )

        analytics.append({

            "officer_id":
                officer.user_id,

            "designation":
                officer.designation,

            "role":
                officer.role,

            "status":
                officer.status,

            "assigned_applications":
                assigned_applications
        })

    return analytics


# =========================================
# ELECTION ANALYTICS
# =========================================

def get_election_analytics():

    elections = Election.query.all()

    analytics = []

    for election in elections:

        total_candidates = (
            Candidate.query.filter_by(
                election_id=election.id
            ).count()
        )

        approved_candidates = (
            Candidate.query.filter_by(
                election_id=election.id,
                status="Approved"
            ).count()
        )

        total_votes = (
            ElectionVote.query.filter_by(
                election_id=election.id
            ).count()
        )

        analytics.append({

            "election":
                election.title,

            "status":
                election.status,

            "candidates":
                total_candidates,

            "approved_candidates":
                approved_candidates,

            "votes":
                total_votes
        })

    return analytics


# =========================================
# SECURITY ANALYTICS
# =========================================

def get_security_analytics():

    total_logs = (
        SecurityLog.query.count()
    )

    low_risk = (
        SecurityLog.query.filter_by(
            risk_level="Low"
        ).count()
    )

    medium_risk = (
        SecurityLog.query.filter_by(
            risk_level="Medium"
        ).count()
    )

    high_risk = (
        SecurityLog.query.filter_by(
            risk_level="High"
        ).count()
    )

    critical_risk = (
        SecurityLog.query.filter_by(
            risk_level="Critical"
        ).count()
    )

    failed_logins = (
        SecurityLog.query.filter_by(
            event_type="LOGIN_FAILED"
        ).count()
    )

    return {

        "total_logs":
            total_logs,

        "low_risk":
            low_risk,

        "medium_risk":
            medium_risk,

        "high_risk":
            high_risk,

        "critical_risk":
            critical_risk,

        "failed_logins":
            failed_logins
    }


# =========================================
# WORKFLOW ANALYTICS
# =========================================

def get_workflow_analytics():

    forwarded = (
        VoterApplication.query.filter(
            VoterApplication.workflow_status.like(
                "%Forwarded%"
            )
        ).count()
    )

    assigned = (
        VoterApplication.query.filter_by(
            workflow_status=
            "Assigned to Officer"
        ).count()
    )

    approved = (
        VoterApplication.query.filter_by(
            workflow_status="Approved"
        ).count()
    )

    rejected = (
        VoterApplication.query.filter_by(
            workflow_status="Rejected"
        ).count()
    )

    return {

        "forwarded":
            forwarded,

        "assigned":
            assigned,

        "approved":
            approved,

        "rejected":
            rejected
    }