Base = declarative_base()
class news_cmnt_pal(Base):
 __tablename__ = 'pal_cmnt'
 id = Column(Integer, primary_key=True)
 comment = Column(String) 