from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database import Entry
from database import Task

engine = create_engine('sqlite:///:memory:', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

#new_entry = Entry(content='Buy milk')
#session.add(new_entry)
#session.commit()

def create_task(eid, task_content):
	new_task = Task(entry_id=eid, content=task_content)

def create_entry(task_list):
	new_entry = Entry()
	for content in task_list:
		create_task(new_entry.id, content)

