#!/usr/bin/python3
""" Defines City ORM object"""

# Import the 'Column', 'Integer', 'String', 'ForeignKey'
# classes from the 'sqlalchemy' module
from sqlalchemy import Column, Integer, String, ForeignKey

# Import the 'Base' function from
# the 'relationship_state' module
from relationship_state import Base

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
