Base = declarative_base()
class news_cmnt_isr(Base):
 __tablename__ = 'isr_cmnt'
 id = Column(Integer, primary_key=True)
 comment = Column(String) 