from sqlalchemy import Column, Integer, String, UniqueConstraint
from .base import Base


class Repository(Base):

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    name = Column(String, nullable=False)
    user = Column(String, nullable=False)

    __tablename__ = 'repositories'
    __table_args__ = (
        UniqueConstraint(user, name),
    )

    def __repr__(self):
        return '<Repository({!r}, {!r})>'.format(self.user, self.name)
