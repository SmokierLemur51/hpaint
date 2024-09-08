from flask_sqlalchemy import SQLAlchemy

from .models import Role


def load_role(db: SQLAlchemy, r: str) -> Role|None:
	return db.session.scalar(db.select(Role).where(Role.name == r))
