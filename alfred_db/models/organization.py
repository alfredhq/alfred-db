from sqlalchemy import Column, Integer, String

from .base import Base


class Organization(Base):

    id = Column(Integer, primary_key=True)
    github_id = Column(Integer, nullable=False, unique=True)
    login = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)

    __tablename__ = 'organizations'

    def __repr__(self):
        return '<Organization({!r})>'.format(self.login)
