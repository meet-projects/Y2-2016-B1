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

