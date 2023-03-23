#!/usr/bin/python3
"""Adds a brand new State to the system!"""

# Import required modules
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

# Check if script is being executed as main program
if __name__ == "__main__":
    # Create a database engine using the values
    # of the first three command line arguments
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # The schema is created in the database specified
    # by the connection string passed to 'create_engine'
    Base.metadata.create_all(engine)

    # Create a session object to be used to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Change the name of the State where id = 2 to New Mexico
    states = session.query(State).filter(State.id == 2).all()
    if states:
        states[0].name = "New Mexico"
    session.commit()

    # Close object and database connection
    session.close()
