from app.models.department import (
    Department
)

from app.models.department_officer import (
    DepartmentOfficer
)

from app.models.voter_application import (
    VoterApplication
)

from app.models.security_log import (
    SecurityLog
)

from app.models.workflow_log import (
    WorkflowLog
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

from app.models.user import User

from app.extensions import db


# =========================================
# DASHBOARD STATISTICS
# =========================================

def get_dashboard_statistics():

    statistics = {

        # =================================
        # DEPARTMENTS
        # =================================

        "total_departments":
            Department.query.count(),

        # =================================
        # OFFICERS
        # =================================

        "active_officers":
            DepartmentOfficer.query.filter_by(
                status="active"
            ).count(),

        "officers_on_leave":
            DepartmentOfficer.query.filter_by(
                status="leave"
            ).count(),

        # =================================
        # APPLICATIONS
        # =================================

        "total_applications":
            VoterApplication.query.count(),

        "approved_applications":
            VoterApplication.query.filter_by(
                status="Approved"
            ).count(),

        "rejected_applications":
            VoterApplication.query.filter_by(
                status="Rejected"
            ).count(),

        "pending_applications":
            VoterApplication.query.filter_by(
                status="Pending"
            ).count(),

        # =================================
        # SECURITY
        # =================================

        "high_risk_alerts":
            SecurityLog.query.filter_by(
                risk_level="High"
            ).count(),

        "critical_risk_alerts":
            SecurityLog.query.filter_by(
                risk_level="Critical"
            ).count(),

        # =================================
        # ELECTIONS
        # =================================

        "total_elections":
            Election.query.count(),

        "active_elections":
            Election.query.filter_by(
                status="Active"
            ).count(),

        "completed_elections":
            Election.query.filter_by(
                status="Completed"
            ).count(),

        # =================================
        # CANDIDATES
        # =================================

        "total_candidates":
            Candidate.query.count(),

        "approved_candidates":
            Candidate.query.filter_by(
                status="Approved"
            ).count(),

        # =================================
        # VOTES
        # =================================

        "total_votes":
            ElectionVote.query.count()
    }

    return statistics


# =========================================
# CREATE DEPARTMENT SERVICE
# =========================================

def create_department_service(

    department_name,

    description,

    status="active"
):

    department = Department(

        name=department_name,

        description=description,

        status=status
    )

    db.session.add(department)

    db.session.commit()

    return department


# =========================================
# GET DEPARTMENT DETAILS
# =========================================

def get_department_details(
    department_id
):

    department = Department.query.get(
        department_id
    )

    if not department:

        return None

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

    approved = (
        VoterApplication.query.filter_by(
            department_id=department.id,
            status="Approved"
        ).count()
    )

    rejected = (
        VoterApplication.query.filter_by(
            department_id=department.id,
            status="Rejected"
        ).count()
    )

    pending = (
        VoterApplication.query.filter_by(
            department_id=department.id,
            status="Pending"
        ).count()
    )

    return {

        "department":
            department,

        "total_officers":
            total_officers,

        "total_applications":
            total_applications,

        "approved":
            approved,

        "rejected":
            rejected,

        "pending":
            pending
    }


# =========================================
# GET OFFICER WORKLOAD
# =========================================

def get_officer_workload():

    officers = (
        DepartmentOfficer.query.all()
    )

    workloads = []

    for officer in officers:

        assigned_applications = (
            VoterApplication.query.filter_by(
                assigned_officer_id=
                officer.user_id
            ).count()
        )

        approved_applications = (
            VoterApplication.query.filter_by(
                assigned_officer_id=
                officer.user_id,

                status="Approved"
            ).count()
        )

        rejected_applications = (
            VoterApplication.query.filter_by(
                assigned_officer_id=
                officer.user_id,

                status="Rejected"
            ).count()
        )

        workloads.append({

            "officer":
                officer,

            "assigned":
                assigned_applications,

            "approved":
                approved_applications,

            "rejected":
                rejected_applications
        })

    return workloads


# =========================================
# GET RECENT APPLICATIONS
# =========================================

def get_recent_applications():

    return (
        VoterApplication.query.order_by(
            VoterApplication.submitted_at.desc()
        ).limit(10).all()
    )


# =========================================
# GET RECENT SECURITY ALERTS
# =========================================

def get_recent_security_alerts():

    return (
        SecurityLog.query.order_by(
            SecurityLog.created_at.desc()
        ).limit(10).all()
    )


# =========================================
# GET RECENT WORKFLOW ACTIVITY
# =========================================

def get_recent_workflow_logs():

    return (
        WorkflowLog.query.order_by(
            WorkflowLog.created_at.desc()
        ).limit(20).all()
    )


# =========================================
# GET ELECTION OVERVIEW
# =========================================

def get_election_overview():

    elections = Election.query.all()

    overview = []

    for election in elections:

        candidates = (
            Candidate.query.filter_by(
                election_id=election.id
            ).count()
        )

        votes = (
            ElectionVote.query.filter_by(
                election_id=election.id
            ).count()
        )

        overview.append({

            "election":
                election,

            "candidates":
                candidates,

            "votes":
                votes
        })

    return overview


# =========================================
# GET FRAUD ALERTS
# =========================================

def get_fraud_alerts():

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
# GET SYSTEM HEALTH
# =========================================

def get_system_health():

    total_users = User.query.count()

    total_logs = SecurityLog.query.count()

    total_workflows = (
        WorkflowLog.query.count()
    )

    total_votes = (
        ElectionVote.query.count()
    )

    return {

        "users":
            total_users,

        "security_logs":
            total_logs,

        "workflow_logs":
            total_workflows,

        "votes":
            total_votes
    }


# =========================================
# GET APPLICATION STATUS REPORT
# =========================================

def get_application_status_report():

    report = {

        "approved":
            VoterApplication.query.filter_by(
                status="Approved"
            ).count(),

        "rejected":
            VoterApplication.query.filter_by(
                status="Rejected"
            ).count(),

        "pending":
            VoterApplication.query.filter_by(
                status="Pending"
            ).count()
    }

    return report


# =========================================
# GET ELECTION RESULTS REPORT
# =========================================

def get_election_results_report(
    election_id
):

    election = Election.query.get(
        election_id
    )

    if not election:

        return None

    candidates = (
        Candidate.query.filter_by(
            election_id=election.id,
            status="Approved"
        ).all()
    )

    results = []

    for candidate in candidates:

        total_votes = (
            ElectionVote.query.filter_by(
                election_id=election.id,
                candidate_id=candidate.id
            ).count()
        )

        results.append({

            "candidate":
                candidate.full_name,

            "party":
                candidate.party_name,

            "votes":
                total_votes
        })

    results = sorted(

        results,

        key=lambda x: x["votes"],

        reverse=True
    )

    return results