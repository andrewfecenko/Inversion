from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

from database import Entry

engine = create_engine('sqlite:///:memory:', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

new_entry = Entry(content='Buy milk')
session.add(new_entry)
session.commit()

for e in session.query(Entry).filter(Entry.content == 'Buy milk'):
	print e.content
	print e.id
	print e.time_created