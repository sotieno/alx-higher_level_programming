#!/usr/bin/python3
""" Defines class City ORM object"""

# Import the 'Column', 'Integer', 'String', 'ForeignKey'
# classes from the 'sqlalchemy' module
from sqlalchemy import Column, Integer, String, ForeignKey

# Import the 'declarative_base' function from
# the 'sqlalchemy.ext.declarative' module
# from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class to be used by all ORM classes
# Base = declarative_base()

# Define the 'City' class, which maps to the 'cities' table in the database
class City(Base):
    """City ORM class"""

    # Name of the table in the database
    __tablename__ = "cities"

    # 'id' column with integer type, auto-incrementing and non-nullable
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)

    # 'name' column with string type of max length 128 and non-nullable
    name = Column(String(128), nullable=False)

    # 'state_id' column with integer type, foreign key and non-nullable
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
