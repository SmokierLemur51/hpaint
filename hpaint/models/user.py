from datetime import datetime

from ..extensions import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(120), nullable=False)
    street_2 = db.Column(db.String(120))
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    zip = db.Column(db.String(5), nullable=False)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    hash = db.Column(db.String(60), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('clean_group.id'))
    bookings = db.relationship('Booking', backref='client', lazy=True)
    clean_group = db.relationship('CleanGroup', backref='member', lazy=True, foreign_keys=[group_id])

    