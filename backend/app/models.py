from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Build(Base):
    __tablename__ = "builds"
    id = Column(Integer, primary_key=True, index=True)
    pipeline = Column(String, index=True)
    status = Column(String)
    build_time = Column(Float)
    timestamp = Column(DateTime)
    logs = Column(String)
    success = Column(Boolean)
