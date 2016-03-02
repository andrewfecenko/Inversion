from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

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
    tasks = relationship('Task', backref='entries', lazy='dynamic')
    completed_tasks = relationship('CompletedTask', backref='entries', lazy='dynamic')
    knowledges = relationship('Knowledge', backref='entries', lazy='dynamic')
    failure_points = relationship('FailurePoint', backref='entries', lazy='dynamic')


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
#  End database models.                                               #
#######################################################################

engine = create_engine('sqlite:///entries.db', echo=False)
Base.metadata.create_all(engine)
