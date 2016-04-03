from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
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
    mistakes = relationship('Mistake', backref='mistakes', cascade="all", lazy='dynamic')

class Mistake(Base):
    __tablename__ = 'mistakes'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey(Entry.id))
    time_created = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    is_om = Column(Boolean)
    verb = Column(String(256))
    noun = Column(String(256))
    cost = Column(Integer)

Base.metadata.create_all(engine)

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
    reload(sys)
    sys.setdefaultencoding('utf8')
    desc = sadisplay.describe(globals().values())

    with open('schema.dot', 'w') as f:
        f.write(sadisplay.dot(desc))
