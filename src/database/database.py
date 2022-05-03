from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


# Create SqlAlchemy connection to database projecttimer.db
ENGINE = create_engine('sqlite:///projecttimer.db', echo = False)

# Init Base class for tables to use
Base = declarative_base()


class Projects(Base):
    """Database management class for projects."""

    __tablename__ = 'projects'
    id = Column(Integer, primary_key = True)
    name = Column(String)


class ProjectData(Base):
    """Database management class for timer entries."""

    __tablename__ = 'entries'
    id = Column(Integer(), primary_key = True)
    project_id = Column(Integer)
    time = Column(Integer)
    date = Column(DateTime)
