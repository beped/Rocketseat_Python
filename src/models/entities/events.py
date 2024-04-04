from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

class Events(Base):
    __tablename__ = 'events'

    id = Column(String, primary_key=True)
    title = Column(String,nullable=False)
    details = Column(String)
    slug = Column(String,nullable=False)
    maximum_attendees = Column(Integer)

    def __repr__(self):
        return f"Events [title={self.title}, slug={self.slug}, maximum_attendees={self.maximum_attendees}]"
    
# class Attendees(Base):
#     __tablename__ = 'attendees'

#     id = Column(String, primary_key=True)
#     name = Column(String, nullable=False)
#     email = Column(String, nullable=False)
#     event_id = Column(String, nullable=False)
#     created_at = Column()