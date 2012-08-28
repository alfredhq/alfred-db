from sqlalchemy import Column, Integer, String, Index
from .base import Base


class User(Base):

    id = Column(Integer, primary_key=True)
    github_id = Column(Integer, nullable=False)
    github_access_token = Column(String, nullable=False)
    login = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    __tablename__ = 'users'
    __table_args__ = (
        Index('ix_users_github_id', 'github_id', unique=True),
        Index('ix_users_login', 'login', unique=True),
    )

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
