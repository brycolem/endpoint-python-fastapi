from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    employer = Column(String, index=True)
    title = Column(String, index=True)
    link = Column(String)
    companyId = Column('company_id', Integer)

    notes = relationship("Note", back_populates="application", cascade="all, delete-orphan", lazy="raise")
