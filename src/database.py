from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


# Create SQLAlchemy engine
engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
Base = declarative_base()

class Projects(Base):
    """Database management class for projects."""

    __tablename__ = 'projects'
    id = Column(Integer(), primary_key = True)
    name = Column(String())

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class ProjectData(Base):
    """Database management class for timer entries."""

    __tablename__ = 'entries'
    id = Column(Integer(), primary_key = True)
    project_id = Column(Integer())
    time = Column(Integer())
    date = Column(datetime(), default = datetime.now())


    def __init__(self, id: int, project_id: int, time: int, date: datetime) -> None:
        self.id = id
        self.project_id = project_id
        self.time = time
        self.date = datetime.now()
