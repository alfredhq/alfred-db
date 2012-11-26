from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref

from .base import Base


class Push(Base):

    id = Column(Integer, primary_key=True)
    ref = Column(String, nullable=False)
    compare_url = Column(String, nullable=False)
    commit_hash = Column(String, nullable=False)
    commit_message = Column(Text, nullable=False)
    committer_name = Column(String, nullable=False)
    committer_email = Column(String)

    repository_id = Column(
        Integer,
        ForeignKey('repositories.id', ondelete='CASCADE'),
        nullable=False,
    )
    repository = relationship(
        'Repository',
        backref=backref(
            name='pushes',
            lazy='dynamic',
            cascade='all, delete-orphan',
            passive_deletes=True,
        ),
    )

    __tablename__ = 'pushes'

    def __repr__(self):
        return '<Push({!r}, {!r})>'.format(self.ref, self.commit_hash)