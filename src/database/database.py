from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base


# Create SqlAlchemy connection to database projecttimer.db
ENGINE = create_engine('sqlite:///projecttimer.db', echo = True)

# Initialize Base class for ORM (Object Relational Mapper) tables to use
Base = declarative_base()


class Projects(Base):
    """Database management class for projects.

    Args:
        id: Unique id for every project.
        name: Name of project.
    """

    __tablename__ = 'projects'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    active = Column(Boolean)


class ProjectData(Base):
    """Database management class for timer entries.

    Args:
        id: Unique identifier for each saved entry.
        project_id: Connects entry to a specific project.
        time: Saved time in seconds.
        date: Date when entry was saved.
    """

    __tablename__ = 'entries'
    id = Column(Integer(), primary_key = True)
    project_id = Column(Integer)
    time = Column(Integer)
    date = Column(DateTime)
