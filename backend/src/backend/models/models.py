
from typing import List
import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, DateTime, Integer, Float, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from flask_login import UserMixin

from ..extensions import login_manager


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(Base, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    # user info
    username: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    # server info
    last_logged_in: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    last_ip: Mapped[str] = mapped_column(String(25), nullable=True)

    def __repr__(self):
        return self.username


@login_manager.user_loader
def load_user(user_id):
    return db.session.scalar(db.select(User).where(User.id == user_id))


class StatusCode(Base):
    __tablename__ = "status_codes"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    info: Mapped[str] = mapped_column(String(500), nullable=True)

    def __repr__(self) -> str:
        return self.code


class EstimateRequest(Base):
    __tablename__ = "estimate_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    contacted: Mapped[bool] = mapped_column(Boolean, default=False)
    converted: Mapped[bool] = mapped_column(Boolean, default=False)
    job_type: Mapped[str] = mapped_column(String(20), nullable=False, default="general")
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=True)
    message: Mapped[str] = mapped_column(String(500), nullable=True)

    def __repr__(self) -> str:
        return "{}'s estimate request.".format(self.name)



# Contact request forms
class ContactRequest(Base):
    __tablename__ = "contact_requests"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    contacted: Mapped[bool] = mapped_column(Boolean, default=False)
    converted: Mapped[bool] = mapped_column(Boolean, default=False)
    requested_on_page: Mapped[str] = mapped_column(String(60))
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=True)
    message: Mapped[str] = mapped_column(String(500), nullable=True)

    notes: Mapped[List["ContactRequestNote"]] = relationship(back_populates="contact_request")

    def __repr__(self) -> str:
        return "{}'s contact request.".format(self.name)




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
    contact_request_id: Mapped[int] = mapped_column(ForeignKey('contact_requests.id'), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    sent: Mapped[bool] = mapped_column(Boolean, default=False)
    approved: Mapped[bool] = mapped_column(Boolean, default=False)
    denied: Mapped[bool] = mapped_column(Boolean, default=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=True)
    total: Mapped[float] = mapped_column(Float, default=0.0)
    street: Mapped[str] = mapped_column(String(120))
    steet_2: Mapped[str] = mapped_column(String(120), nullable=True)
    city: Mapped[str] = mapped_column(String(60))
    state: Mapped[str] = mapped_column(String(2)) 
    zip_code: Mapped[str] = mapped_column(String(10))    

    def __repr__(self) -> str:
        return self.name
