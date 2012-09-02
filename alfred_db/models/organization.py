from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Organization(Base):

    id = Column(Integer, primary_key=True)
    github_id = Column(Integer, nullable=False, unique=True)
    login = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)

    users = relationship('User', secondary='memberships',
                         backref='organizations')

    __tablename__ = 'organizations'

    def __repr__(self):
        return '<Organization({!r})>'.format(self.login)


class Membership(Base):

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    __tablename__ = 'memberships'

    def __repr__(self):
        return '<Membership(<User({!r})>-<Organization({!r})>)'.format(
            self.organization_id, self.user_id
        )
