from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from ..helpers import now
from .base import Base


class Report(Base):

    id = Column(Integer, primary_key=True)
    error = Column(Text)
    created_on = Column(DateTime(timezone=True), nullable=False,  default=now)
    finished_on = Column(DateTime(timezone=True))

    commit_id = Column(
        Integer,
        ForeignKey('commits.id', ondelete='CASCADE'),
        nullable=False,
    )
    commit = relationship(
        'Commit',
        backref=backref(
            name='report',
            uselist=False,
            cascade='all, delete-orphan',
            passive_deletes=True,
        ),
    )

    __tablename__ = 'reports'

    def __repr__(self):
        return '<Report({!r}, {!r})>'.format(self.id, self.finished_on)
