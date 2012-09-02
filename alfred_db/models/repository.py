from sqlalchemy import Column, Integer, String, UniqueConstraint, Enum
from .base import Base


class Repository(Base):

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    name = Column(String, nullable=False)
    owner_name = Column(String, nullable=False)
    owner_type = Column(Enum('organization', 'user', native_enum=False),
                        nullable=False)
    owner_id = Column(Integer, nullable=False)

    __tablename__ = 'repositories'
    __table_args__ = (
        UniqueConstraint(owner_id, owner_type),
    )

    def __repr__(self):
        return '<Repository({!r}, {!r})>'.format(self.owner_name, self.name)
