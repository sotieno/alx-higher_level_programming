#!/usr/bin/python3
"""Link class to table in database"""

# Import the 'sys' module, which is used to access command line arguments
import sys

# Import the 'Base' classe from the 'model_state' module
from model_state import Base

# Import the 'create_engine' function from the 'sqlalchemy' module
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Create a database engine using the values
    # of the first three command line arguments
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)

    # Generate the database schema based on the
    # definitions of the tables in the 'State' class

    # The schema is created in the database specified
    # by the connection string passed to 'create_engine'
    Base.metadata.create_all(engine)
