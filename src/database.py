from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create SQLAlchemy engine
engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
base = declarative_base()


class ProjectData(base):
    """Database management class for project data."""

    def __init__(self, col1) -> None:
        self.col1 = col1