from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('sqlite:///:memory:', echo=False)

Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, Sequence('entry_id_seq'), primary_key=True)
    time_created = Column(DateTime, default=datetime.datetime.now(),
                          nullable=False)
    time_updated = Column(DateTime, default=datetime.datetime.now(),
                          nullable=False)
    tasks = relationship('Task', backref='entries', lazy='dynamic')


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, Sequence('entry_id_seq'), primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    time_created = Column(DateTime, default=datetime.datetime.now())
    time_updated = Column(DateTime, default=datetime.datetime.now())
    content = Column(String(256))

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

create_entry(["Task 1", "Task 2", "Task 3"])


def tasksToday():
    beg = datetime.datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0)
    end = datetime.datetime.now().replace(
        hour=23, minute=59, second=59, microsecond=59)
    out = []
    time = datetime.datetime.now()
    print time
    for s in session.query(Task).all():
        cur = s.time_created
        if (cur <= end and cur >= beg):
            print cur
            out.append(s.content)
    return out
print(tasksToday())
