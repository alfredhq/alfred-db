from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref

from .base import Base


class Commit(Base):

    id = Column(Integer, primary_key=True)
    hash = Column(String, nullable=False)
    ref = Column(String, nullable=False)
    compare_url = Column(String, nullable=False)
    committer_name = Column(String, nullable=False)
    committer_email = Column(String, nullable=False)
    message = Column(Text, nullable=False)

    repository_id = Column(
        Integer,
        ForeignKey('repositories.id', ondelete='CASCADE'),
        nullable=False,
    )
    repository = relationship(
        'Repository',
        backref=backref(
            name='commits',
            lazy='dynamic',
            cascade='all, delete-orphan',
            passive_deletes=True,
        ),
    )

    __tablename__ = 'commits'

    def __repr__(self):
        return '<Commit({!r}, {!r})>'.format(self.ref, self.hash)
