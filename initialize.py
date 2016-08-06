from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.
newsarticle=News(title="hi", content="hiii")
meal = Food( ingredients = "hummus" ,steps = "smash them" , name = "falafel" , nationality = "Palestinian" )
session.add(newsarticle)
session.add(meal)
session.commit()

 