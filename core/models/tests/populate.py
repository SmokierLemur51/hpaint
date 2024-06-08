""" File: models/tests/populate.py
    
    Test data for working with in development.
"""
from flask_sqlalchemy import SQLAlchemy
from flask import current_app

from sqlalchemy.exc import IntegrityError

from ..models import StatusCode

def populate_stat_codes(db: SQLAlchemy) -> None:
    stat_codes = [
        StatusCode(code="open", info="Not yet contacted."),
    ]
    with current_app.app_context():
        try:
            db.session.add_all(stat_codes)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print(e)
        