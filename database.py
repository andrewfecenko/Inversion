from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=False)

Base = declarative_base()

class Entry(Base):
	__tablename__ = 'entries'
	id = Column(Integer, Sequence('entry_id_seq'), primary_key=True)
	time_created = Column(DateTime(timezone=True), server_default=func.now())
	time_updated = Column(DateTime(timezone=True), onupdate=func.now())

class Task(Base):
	__tablename__ = 'tasks'
	id = Column(Integer, Sequence('entry_id_seq'), primary_key=True)
	entry_id = Column(Integer, ForeignKey('entries.id'))
	time_created = Column(DateTime(timezone=True), server_default=func.now())
	time_updated = Column(DateTime(timezone=True), onupdate=func.now())
	content = Column(String(256))
	entry = relationship('Entry', backref="tasks")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_task(eid, task_content):
	new_task = Task(entry_id=eid, content=task_content)
	session.add(new_task)
	session.commit()

def create_entry(task_list):
	new_entry = Entry()
	session.add(new_entry)
	session.commit()
	for content in task_list:
		create_task(new_entry.id, content)

