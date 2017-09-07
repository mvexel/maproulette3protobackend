"""The Challenge model."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class Challenge(Base):
    """The Challenge model."""

    __tablename__ = 'challenge'

    # Database identifier
    id = Column(Integer, primary_key=True)
    # Challenge owner
    user_id = Column(Integer, ForeignKey('user.id'))
    # The Challenge owner can assign their own identifier to
    # keep track of the feature across updates.
    assigned_id = Column(Integer)
    # Challenge Title
    title = Column(String)
    # Description
    description = Column(String)
    # Challenge level instruction
    instruction = Column(String)
    # Backref to tasks
    tasks = relationship("Task", backref='challenge')
