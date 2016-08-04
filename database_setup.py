from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Food(Base):
	__tablename__ = "food"
	id= Column(Integer, primary_key=True)
	ingredients = Column(String)
	steps = Column(String)
	name = Column(String)
	nationality = Column(String)


class Music(Base):
	__tablename__ = "music"
	id = Column(Integer, primary_key=True)
	song = Column(String)
	nationality = Column(String)
	artist = Column(String)
	link = Column(String)



class News(Base):
	__tablename__ = "news"
	id = Column (Integer , primary_key=True)
	title = Column(String)
	content = Column(String)
	comments = relationship("News_Comments")



class News_Comments(Base):
	__tablename__ = "news_comments"

	id = Column (Integer , primary_key=True)
	name = Column(String)
	news_id = Column(Integer, ForeignKey('news.id'))
	text = Column(String)
	nationality = Column(String)



