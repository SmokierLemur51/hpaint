
from typing import List
import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, DateTime, Integer, Float, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class StatusCode(Base):
    __tablename__ = "status_codes"

    id: Mapped[int] = mapped_column(primary_key=True)




class EstimateRequest(Base):
    __tablename__ = "estimate_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    contacted: Mapped[bool] = mapped_column(Boolean, default=False)
    converted: Mapped[bool] = mapped_column(Boolean, default=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=True)
    message: Mapped[str] = mapped_column(String(500), nullable=True)

    def __repr__(self) -> str:
        return "{}'s estimate request.".format(self.name)



# 
# Contact request forms
class ContactRequest(Base):
    __tablename__ = "contact_requests"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    contacted: Mapped[bool] = mapped_column(Boolean, default=False)
    converted: Mapped[bool] = mapped_column(Boolean, default=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=True)
    message: Mapped[str] = mapped_column(String(500), nullable=True)

    notes: Mapped[List["ContactRequestNote"]] = relationship(back_populates="contact_request")

    def __repr__(self) -> str:
        return "{}'s contact request.".format(self.name)


    def check_not_duplicate(self, db: SQLAlchemy) -> bool:
        return True

    def create_note(): # -> Note
        pass    


# Administrative notes for contact requests
class ContactRequestNote(Base): 
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    contact_form_id: Mapped[int] = mapped_column(ForeignKey('contact_requests.id'))
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(String(500), nullable=True)

    contact_request: Mapped["ContactRequest"] = relationship(back_populates="notes")

    def __repr__(self) -> str:
        return "{} <ContactRequest-{}>".format(self.title, self.contact_form_id)




class Estimate(Base):
    __tablename__ = "estimates"

    id: Mapped[int] = mapped_column(primary_key=True)



""" 
class Address(Base):

    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    street: Mapped[str] = mapped_column(String(120))
    steet_2: Mapped[str] = mapped_column(String(120), nullable=True)
    city: Mapped[str] = mapped_column(String(60))
    state: Mapped[str] = mapped_column(String(2)) # add options
    zip_code: Mapped[str] = mapped_column(String(10))


    def __repr__(self) -> str:
        return "{}".format(self.street)
        







class EstimateRequest(Base):

    __tablename__ = "estimate_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    contacted: Mapped[bool] = mapped_column(Boolean, default=False)
    converted: Mapped[bool] = mapped_column(Boolean, default=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=True)
    message: Mapped[str] = mapped_column(String(500), nullable=True)

    def __repr__(self) -> str:
        return "{}'s estimate request.".format(self.name)




class EstimateRequestNote(Base):
    

    __tablename__ = "estimate_request_notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    estimate_request_id: Mapped[int] = mapped_column(ForeignKey('estimate_requests.id'))
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return "{} <EstimateRequest-{}>".format(self.title, self.estimate_request_id)


"""
