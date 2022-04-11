from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


# Create SqlAlchemy connection to database projecttimer.db
engine = create_engine('sqlite:///projecttimer.db', echo=True)

# Init Base class for tables to use
Base = declarative_base()

# Create Object Relational Mapper (ORM) session
Session = Session()
