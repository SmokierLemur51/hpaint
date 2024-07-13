from typing import List
from flask_sqlalchemy import SQLAlchemy

from ...models.models import (
    ContactRequest,
    EstimateRequest,
    Estimate,
)


def get_contact_requests(db: SQLAlchemy, contacted_filter: bool) -> List[ContactRequest]:
    """Provide bool to filter through ContactRequest.contacted"""
    return db.session.scalars(db.select(ContactRequest).where(ContactRequest.contacted == contacted_filter)).all()


def get_estimates(db: SQLAlchemy) -> List[Estimate]:
    return db.session.scalars(db.select(Estimate)).all()


def get_estimates_with_filter(db: SQLAlchemy, filter: str, status: bool) -> List[Estimate]:
    """
    Params:
    -filter: str -> 'sent', 'approved', 'denied'. For Estimate.sent, Estimate.approved, Estimate.denied 
    db values.
    -status: bool -> the boolean value of Estimate.sent/approved/denied
    Ex:
        estimates = filter_estimates(db, 'sent', False) -> List[*estimates not yet sent*]
    """
    if filter == 'sent':
        return db.session.query(db.select(Estimate).where(
            Estimate.sent == status, Estimate.approved == False, Estimate.denied == False)).all()
    elif filter == 'approved':
        return db.session.query(db.select(Estimate).where(Estimate.approved == status)).all()
    elif filter == 'denied':
        return db.session.query(db.select(Estimate).where(Estimate.denied == status)).all()
    else:
        return get_estimates(db)
