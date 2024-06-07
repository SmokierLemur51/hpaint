
import datetime

from flask import SQLAlchemy
from sqlalchemy import Boolean, DateTime, Integer, Float, ForeignKey, String,
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class StatusCode(Base):
    pass


class EstimateRequest(Base):
    pass


class ContactRequest(Base):
    pass


class Estimate(Base):
    pass



