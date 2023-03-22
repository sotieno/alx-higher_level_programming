#!/usr/bin/python3
""" Defines class State ORM object"""

# Import the 'Column', 'Integer', and 'String'
# classes from the 'sqlalchemy' module
from sqlalchemy import Column, Integer, String

# Import the 'declarative_base' function from
# the 'sqlalchemy.ext.declarative' module
from sqlalchemy.ext.declarative import declarative_base

# Import the 'relationship' function from
# the 'sqlalchemy.orm' module
from sqlalchemy.orm import relationship

# Create a declarative base class to be used by all ORM classes
Base = declarative_base()


# Define the 'State' class, which maps to the 'states' table in the database
class State(Base):
    """State ORM class"""

    # Name of the table in the database
    __tablename__ = "states"

    # 'id' column with integer type, auto-incrementing and non-nullable
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)

    # 'name' column with string type of max length 128 and non-nullable
    name = Column(String(128), nullable=False)
