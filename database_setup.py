from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class News_Cmnt_Pal(Base):
    __tablename__ = 'pal_cmnt'
    id = Column(Integer, primary_key=True)
    comment = Column(String)

class News_Cmnt_Isr(Base):
    __tablename__ = 'isr_cmnt'
    id = Column(Integer, primary_key=True)
    comment = Column(String)  


class Food_Cmnt_Pal(Base):
	__tablename__ = "food_Pal_cmnt"
	id= Column(Integer, primary_key=True)
	Ingredients = Column(String)
	Steps = Column(String)

class Food_Cmnt_Isr(Base):
	__tablename__ = "food_Isr_cmnt"
	id= Column(Integer, primary_key=True)
	Ingredients = Column(String)
	Steps = Column(String)


class Music_Cmnt_Pal(Base):
	__tablename__ = "Music_Pal_cmnt"
	id = Column(Integer, primary_key=True)
	Song = Column(String)
	Artist = Column(String)
	Link = Column(String)
		

class Music_Cmnt_Isr(Base):
	__tablename__ = "Music_Isr_cmnt"
	id = Column(Integer, primary_key=True)
	Song = Column(String)
	Artist = Column(String)
	Link = Column(String)
		
	
		

