from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from .base import Base


class Permission(Base):

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )
    user = relationship(
        'User',
        backref=backref(
            name='permissions',
            lazy='dynamic',
            cascade='all, delete-orphan',
            passive_deletes=True,
        ),
    )

    repository_id = Column(
        Integer,
        ForeignKey('repositories.id', ondelete='CASCADE'),
        nullable=False,
    )
    repository = relationship(
        'Repository',
        backref=backref(
            name='permissions',
            lazy='dynamic',
            cascade='all, delete-orphan',
            passive_deletes=True,
        ),
    )

    admin = Column(Boolean, default=False, nullable=False)
    push = Column(Boolean, default=False, nullable=False)
    pull = Column(Boolean, default=False, nullable=False)

    __tablename__ = 'permissions'

    def __repr__(self):
        return '<Permission({!r}-{!r})>'.format(
            self.user_id, self.repository_id
        )
