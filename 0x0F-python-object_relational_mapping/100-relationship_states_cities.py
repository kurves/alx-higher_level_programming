#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    california = State(name='California')

    san_francisco = City(name='San Francisco', state=california)

    california.cities.append(san_francisco)

    session.add(california)
    session.add(san_francisco)

    session.commit()

    session.close()
