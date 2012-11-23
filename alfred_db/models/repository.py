from sqlalchemy import Column, Integer, String, UniqueConstraint, Enum
from .base import Base


class Repository(Base):

    id = Column(Integer, primary_key=True)
    github_id = Column(Integer, nullable=False, unique=True)
    url = Column(String, nullable=False)
    name = Column(String, nullable=False)
    token = Column(String, nullable=False)
    hook_id = Column(String, nullable=True)
    owner_name = Column(String, nullable=False)
    owner_type = Column(Enum('organization', 'user'), nullable=False)
    owner_id = Column(Integer, nullable=False)

    __tablename__ = 'repositories'

    def __repr__(self):
        return '<Repository({!r}, {!r})>'.format(self.owner_name, self.name)
