from datetime import datetime
from sqlalchemy import Column,String,Integer,DateTime
from database.database import Base


class Projects(Base):
    """Database management class for projects."""

    __tablename__ = 'projects'
    id = Column(Integer(), primary_key = True)
    name = Column(String())


class ProjectData(Base):
    """Database management class for timer entries."""

    __tablename__ = 'entries'
    id = Column(Integer(), primary_key = True)
    project_id = Column(Integer())
    time = Column(Integer())
    date = Column(DateTime(), default = datetime.now())
