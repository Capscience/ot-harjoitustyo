from datetime import datetime

from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


# Create SqlAlchemy connection to database projecttimer.db
engine = create_engine('sqlite:///projecttimer.db', echo=True)

# Init Base class for tables to use
Base = declarative_base()

# Create Object Relational Mapper (ORM) session
Session = Session(bind=engine)
print(Session)


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
