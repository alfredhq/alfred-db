from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from .base import Base


class Fix(Base):

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    description_html = Column(Text, nullable=False)
    path = Column(String, nullable=False)
    line = Column(Integer, nullable=False)
    source = Column(Text, nullable=False)
    solution = Column(Text, nullable=False)

    report_id = Column(
        Integer,
        ForeignKey('reports.id', ondelete='CASCADE'),
        nullable=False,
    )
    report = relationship(
        'Report',
        backref=backref(
            name='fixes',
            lazy='dynamic',
            cascade='all, delete-orphan',
            passive_deletes=True,
        ),
    )

    __tablename__ = 'fixes'

    def __repr__(self):
        return '<Fix({!r}, {!r})>'.format(self.path, self.line)
