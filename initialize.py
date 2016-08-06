from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.
<<<<<<< HEAD
article=News(title="New conflict in the middle east", content=" washington declaired that the middle east is in a warzone and needs to function around many different new rules that waere set by the pentagon last year in an atempt to make it better  ")
meal = Food( ingredients = "hummus" ,steps = "smash them" , name = "falafel" , nationality = "Palestinian" )
session.add(article)
session.add(meal)
=======
article=News(title="hi", content="hiii")
session.add(article)
>>>>>>> 5d202cace155afcd0fc125b743c5bd587bb20366
session.commit()

 