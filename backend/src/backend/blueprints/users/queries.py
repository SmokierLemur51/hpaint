from typing import List
from flask_sqlalchemy import SQLAlchemy

from ...models.models import (
    User
)

def get_user(db: SQLAlchemy, u: str) -> User|None:
    """Loading user for flask_login
    :param db: flask_sqlalchemy object.
    :param u: username
    """
    try:
        u = db.session.scalar(db.select(User).where(User.username == u))
        if u is None:
            print("No user found...")
            return None
        else:
            return u
    except Exception as e:
        print("Excetption: ", e)
        return None



# Might be best to rename to something like unique_usernames
def check_unique_usernames(db: SQLAlchemy, username: str) -> bool:
    """ 
    """
    try:
        u = db.session.scalar(db.select(User).where(User.username == priv))
        # Check all are None
        if u is None:
            print("Usernamesprovided is unique.")
            return True
        else:
            print("Username is not unique.")
            return False
    except AttributeError as e: 
        print("Error: " + e)
        return False 
    