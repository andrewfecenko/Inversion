from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
<<<<<<< HEAD
from sqlalchemy.orm import sessionmaker

from database import Entry
from database import Task
=======

from database import *
>>>>>>> c8496f45f7932adf9c4f321b6f5b5f0e2827bf40



<<<<<<< HEAD
#new_entry = Entry(content='Buy milk')
#session.add(new_entry)
#session.commit()

def create_task(eid, task_content):
	new_task = Task(entry_id=eid, content=task_content)

def create_entry(task_list):
	new_entry = Entry()
	for content in task_list:
		create_task(new_entry.id, content)
=======
new_entry = Entry()
tasks = ["Task 1", "Task 2", "Task 3"]
session.add(new_entry)
session.commit()
entry_id = new_entry.id
for task in tasks:
	a = Task(entry_id=entry_id, content=task)
	session.add(a)
session.commit()

for s in session.query(Task).all():
	print s.id
	print s.entry_id
	print s.content
>>>>>>> c8496f45f7932adf9c4f321b6f5b5f0e2827bf40

