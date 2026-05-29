from flask import request

from app.extensions import db

from app.models.security_log import (
    SecurityLog
)


def create_security_log(

    user_id,

    event_type,

    description,

    risk_level="Low"
):

    log = SecurityLog(

        user_id=user_id,

        event_type=event_type,

        description=description,

        ip_address=request.remote_addr,

        user_agent=request.user_agent.string,

        risk_level=risk_level
    )

    db.session.add(log)

    db.session.commit()