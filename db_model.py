from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
import datetime

Base = declarative_base()

engine = create_engine('sqlite:///entries.db', echo=False)

#######################################################################
# All database models for entry information.                          #
#######################################################################

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    time_updated = Column(DateTime, default=datetime.datetime.now(), nullable=False)

    # use one-to-one for summary and plans, one-to-many for rest
    summary = relationship('Summary', uselist=False, back_populates='entries')
    plan = relationship('Plan', uselist=False, back_populates='entries')
    tasks = relationship('Task', backref='entries', cascade="all", lazy='dynamic')
    completed_tasks = relationship('CompletedTask', backref='entries', cascade="all", lazy='dynamic')
    knowledges = relationship('Knowledge', backref='entries', cascade="all", lazy='dynamic')
    failure_points = relationship('FailurePoint', backref='entries', cascade="all", lazy='dynamic')


class Summary(Base):
    __tablename__ = 'summaries'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    entries = relationship('Entry', back_populates='summary')
    content = Column(String(1024))


class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    entries = relationship('Entry', back_populates='plan')
    content = Column(String(1024))


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, Sequence('entry_id_seq'), primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    time_created = Column(DateTime, default=datetime.datetime.now())
    time_updated = Column(DateTime, default=datetime.datetime.now())
    content = Column(String(256))


class CompletedTask(Base):
    __tablename__ = 'completed_tasks'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    content = Column(String(256))


class Knowledge(Base):
    __tablename__ = 'knowledges' #plural s to avoid confusion
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    content = Column(String(256))


class FailurePoint(Base):
    __tablename__ = 'failure_points'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    content = Column(String(256))


#######################################################################
#  Function for creating a database using above models.               #
#######################################################################

def build_database():
	Base.metadata.create_all(engine)

def clear_database():
    Base.metadata.drop_all(engine)


#######################################################################                                               
# Extra functions included for development.                           #
#######################################################################

def generate_schema_dot():
    """
    Generate a .dot file for the current database schema.
    Render the graphviz directed graphs with:
        $ dot -Tpng schema.dot > schema.png
    """
    import sys
    import sadisplay
    sys.setdefaultencoding('utf8')
    reload(sys)

    desc = sadisplay.describe(globals().values())

    with open('schema.dot', 'w') as f:
        f.write(sadisplay.dot(desc))
