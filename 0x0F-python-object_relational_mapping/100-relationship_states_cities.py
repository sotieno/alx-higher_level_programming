#!/usr/bin/python3
"""Create 'State' “California” with the 'City' “San Francisco”"""

# Import required modules
from sys import argv
from relationship_state import Base, State
from relationship_city import City
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

    # Create 'State' "California"
    new_state = State(name="California")
    session.add(new_state)
    session.commit()

    # Create 'City' "San Francisco"
    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()

    # Close object and database connection
    session.close()
