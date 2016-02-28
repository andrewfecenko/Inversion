from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from database import *



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

