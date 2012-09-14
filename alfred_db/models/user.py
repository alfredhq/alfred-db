from sqlalchemy import Column, Integer, String, UniqueConstraint
from .base import Base


class User(Base):

    id = Column(Integer, primary_key=True)
    github_id = Column(Integer, nullable=False, unique=True)
    github_access_token = Column(String, nullable=False)
    login = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    apitoken = Column(String, unique=True, nullable=False)

    __tablename__ = 'users'

    def __repr__(self):
        return '<User({!r})>'.format(self.login)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
