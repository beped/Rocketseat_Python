from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

class Events(Base):
    __tablename__ = 'events'

    id = Column(String, primary_key=True)
    title = Column(String,nullable=False)
    detais = Column(String)
    slug = Column(String,nullable=False)
    maximum_attendees = Column(Integer)

class attendees(Base):
    __tablename__ = 'attendees'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, nullable=False)
    created_at = Column()