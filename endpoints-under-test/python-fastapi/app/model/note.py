from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    noteText = Column('note_text', String)
    applicationId = Column('application_id', Integer, ForeignKey('applications.id'))

    application = relationship("Application", back_populates="notes")
