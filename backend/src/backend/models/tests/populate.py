""" File: models/tests/populate.py
    
    Test data for working with in development.
"""
from flask_sqlalchemy import SQLAlchemy
from flask import current_app

from sqlalchemy.exc import IntegrityError

from ..models import (
    ContactRequest,
    EstimateRequest,
    StatusCode,
) 

def populate_stat_codes(db: SQLAlchemy) -> None:
    stat_codes = [
        StatusCode(code="New", info="A newly received lead contact request that has not been reviewed yet."),
        StatusCode(code="Reviewed", info="The lead contact request has been reviewed but no further action has been taken yet."),
        StatusCode(code="Contacted", info="The lead has been contacted."),
        StatusCode(code="Follow-Up Scheduled", info="A follow-up call or meeting has been scheduled with the lead."),
        StatusCode(code="In Progress", info="Discussions or negotiations are actively ongoing with the lead."),
        StatusCode(code="Awaiting Response", info="Waiting for a response from the lead after contacting or sending a proposal."),
        StatusCode(code="Proposal Sent", info="A formal proposal has been sent to the lead."),
        StatusCode(code="Negotiation", info="The lead is negotiating terms or pricing with us."),
        StatusCode(code="Closed Won", info="The lead has agreed to proceed with our services and the deal is closed."),
        StatusCode(code="Closed Lost", info="The lead has decided not to proceed with our services and the deal is closed."),
        StatusCode(code="Deferred", info="The lead has expressed interest but wants to delay the project to a later date."),
        StatusCode(code="Invalid", info="The lead contact request is invalid (e.g., spam, incorrect contact details)."),
        StatusCode(code="Duplicate", info="The lead contact request is a duplicate of a previously received request."),
        StatusCode(code="Archived", info="The lead request is archived for future reference but is not currently active.")
    ]
    with current_app.app_context():
        try:
            db.session.add_all(stat_codes)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print(e)
        

def populate_contact_requests(db: SQLAlchemy) -> None:
    reqs = [
        ContactRequest(
            name="Logan",
            phone="0129991234",
            email="trainwreck@gmail.com",
            message="I need help urgent!! I shit on the wall and my mom is gonna be so mad! HELP!",
        ),
        ContactRequest(
            name="Javier Garcia",
            phone="1234567891",
            email="javiergarcia@nomail.com",
            message="You guys come paint house. Tuesday please.",
        ),
        ContactRequest(
            name="Juan Torres",
            phone="7894561234",
            email="juantorres@gmail.com",
            message="I was wondering if you guys do charity work? My mom has dementia.",
        ),
        ContactRequest(
            name="Harry Potter",
            phone="4561386795",
            email="harrypotter@fakeemail.com",
            message="I am a builder, looking to sub contract painting gigs out to someone. Are you interested?",
        ),
        ContactRequest(
            name="Taylor Swift",
            phone="5050551000",
            email="realtaylor@notemail.com",
            message="I would like to perform at your next painting job please. Hit my line.",
        ),
    ]
    with current_app.app_context():
        try:
            db.session.add_all(reqs)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(IntegrityError)



def populate_estimate_requests(db: SQLAlchemy) -> None:
    reqs = [
        EstimateRequest(
            name="Logan",
            phone="0129991234",
            email="trainwreck@gmail.com",
            message="I need help urgent!! I shit on the wall and my mom is gonna be so mad! HELP!",
        ),
        EstimateRequest(
            name="Pablo",
            phone="1099876543",
            email="pabloescobar@colombian.com",
            message="How much to paint my trap house?",
        ),
        EstimateRequest(name="Callie", phone="8764561234", email="cgdilamarter@gmail.com", 
                        message="Six bedroom house, can you come and give me an estimate?"),
        EstimateRequest(name="Julio", phone="7564869234", email="juliorojas@fake.com",
                        message="Moving in July, do you think you can come quote the premove paintjob."),

    ]
    with current_app.app_context():
        try:
            db.session.add_all(reqs)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(IntegrityError)
