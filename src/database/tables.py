from sqlalchemy import Column, String, Integer
from datetime import datetime
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
    date = Column(datetime(), default = datetime.now())
