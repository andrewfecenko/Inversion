from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence
from sqlalchemy.sql import func

engine = create_engine('sqlite:///:memory:', echo=False)

Base = declarative_base()

class Entry(Base):
	__tablename__ = 'entries'
	id = Column(Integer, Sequence('entry_id_seq'), primary_key=True)
	time_created = Column(DateTime(timezone=True), server_default=func.now())
	time_updated = Column(DateTime(timezone=True), onupdate=func.now())
	content = Column(String(256))

Base.metadata.create_all(engine)