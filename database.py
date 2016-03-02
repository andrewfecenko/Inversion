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
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime, default=datetime.datetime.now(),
                          nullable=False)
    time_updated = Column(DateTime, default=datetime.datetime.now(),
                          nullable=False)

    # use one-to-one for summary and plans, one-to-many for rest
    summary = relationship('Summary', uselist=False, back_populates='entries')
    tasks = relationship('Task', backref='entries', lazy='dynamic')
    completed_tasks = relationship(
        'CompletedTask', backref='entries', lazy='dynamic')
    knowledge = relationship('Knowledge', backref='entries', lazy='dynamic')
    failure_points = relationship(
        'FailurePoints', backref='entries', lazy='dynamic')
    plans = relationship('Plans', uselist=False, back_populates='entries')


class Summary(Base):
    __tablename__ = 'summary'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    entries = relationship('Entry', back_populates='summary')
    content = Column(String(1024))


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, Sequence('entry_id_seq'), primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    time_created = Column(DateTime, default=datetime.datetime.now())
    time_updated = Column(DateTime, default=datetime.datetime.now())
    content = Column(String(256))


class CompletedTask(Base):
    __tablename__ = 'completed_task'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    content = Column(String(256))


class Knowledge(Base):
    __tablename__ = 'knowledge'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    content = Column(String(256))


class FailurePoints(Base):
    __tablename__ = 'failure_points'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    content = Column(String(256))


class Plans(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    entries = relationship('Entry', back_populates='plans')
    content = Column(String(1024))


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


def add_summary(entry, summary):
    entry.summary = Summary(content=summary)


def add_plan(entry, plan):
    entry.plans = Plans(content=plan)


def tasks_today():
    beg = datetime.datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0)
    end = datetime.datetime.now().replace(
        hour=23, minute=59, second=59, microsecond=59)
    out = []

    for s in session.query(Task).all():
        cur = s.time_created
        if (cur <= end and cur >= beg):
            out.append(s.content)
    return out


def get_todays_entry():
    """Get the Entry relation for today."""
    beg = datetime.datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0)
    end = datetime.datetime.now().replace(
        hour=23, minute=59, second=59, microsecond=59)

    for entry in session.query(Entry).all():
        entry_time = entry.time_created
        if (entry_time <= end and entry_time >= beg):
            return entry

    return None


class EntryContent:

    def __init__(self, summary, tasks, completed_tasks, knowledge, failure_points,
                 plans):

        self.summary = summary
        self.tasks = tasks
        self.completed_tasks = completed_tasks
        self.knowledge = knowledge
        self.failure_points = failure_points
        self.plans = plans

    def list_sections(self):
        return vars(self).keys()

    def list_repr(self):
        listed = []
        listed.append(self.summary)
        listed.append(self.tasks)
        listed.append(self.completed_tasks)
        listed.append(self.knowledge)
        listed.append(self.failure_points)
        listed.append(self.plans)
        return listed


def get_entry_info(entry):
    """Get all of entry's info returned as an EntryContent object."""
    try:
        summary = entry.summary.content
    except AttributeError:
        summary = None

    try:
        tasks = entry.tasks.filter(Task.entry_id == entry.id)
        tasks = [task.content for task in tasks]
    except AttributeError:
        tasks = None

    try:
        completed_tasks = entry.completed_tasks.filter(
            CompletedTask.entry_id == entry.id)
        completed_tasks = [c_t.content for c_t in completed_tasks]
    except AttributeError:
        completed_tasks = None

    try:
        knowledge = entry.knowledge.filter(Knowledge.entry_id == entry.id)
        knowledge = [k.content for k in knowledge]
    except AttributeError:
        knowledge = None

    try:
        failure_points = entry.failure_points.filter(
            FailurePoints.entry_id == entry.id)
        failure_points = [f.content for f in failure_points]
    except AttributeError:
        failure_points = None

    try:
        plans = entry.plans.content
    except AttributeError:
        plans = None

    return EntryContent(summary, tasks, completed_tasks, knowledge, failure_points, plans)


def get_all_entries():
    for entry in session.query(Entry).all():
        yield get_entry_info(entry)


def print_entry_list_repr(entry):
    for section in entry.list_repr():
        print section


def partial_info_get():
    """TODO: delete this function."""
    create_entry(["Task one", "Task two", "Task three"])
    todays_entry = get_todays_entry()

    add_summary(todays_entry, "testing")
    add_plan(todays_entry, "final")

    todays_entry = get_entry_info(todays_entry)
    print_entry_list_repr(todays_entry)


def generate_schema_dot():
    """
    Generate a .dot file for the current database schema.
    Render the graphviz directed graphs with:
        $ dot -Tpng schema.dot > schema.png
    """
    import sys
    import sadisplay
    reload(sys)
    sys.setdefaultencoding('utf8')

    desc = sadisplay.describe(globals().values())

    with open('schema.dot', 'w') as f:
        f.write(sadisplay.dot(desc))
