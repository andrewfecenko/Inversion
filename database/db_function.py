from sqlalchemy.orm import sessionmaker
import datetime

from db_model import Entry
from db_model import Mistakes
from db_model import engine

from db_model import build_database
from db_model import clear_database()


Session = sessionmaker(bind=engine)
session = Session()

#######################################################################
# All functions dealing with entries.                                 #
#######################################################################

def create_entry(givenday=datetime.datetime.now()):

    beg = givenday.replace(hour=0, minute=0, second=0, microsecond=0)
    end = givenday.replace(hour=23, minute=59, second=59, microsecond=59)

    # check that an entry doesn't already exist for the day
    for entry in session.query(Entry).all():
        entry_time = entry.time_created
        if (entry_time <= end and entry_time >= beg):
            raise ValueError()

    new_entry = Entry(time_created=givenday)
    session.add(new_entry)
    session.commit()
    return new_entry.id

def get_entry_mistakes(eid):
    entry = session.query(Entry).get(eid)
    try:
        mistakes = entry.mistakes.all()
    except AttributeError:
        mistakes = None
    return mistakes

#######################################################################
# All functions for setting or getting information about a mistake.   #
#######################################################################

def create_mistake(eid, is_om, noun, cost):
    mistake = Mistake(entry_id=eid, is_om=is_om,
        noun=noun, cost=cost)
    session.add(mistake)
    session.commit()
    return mistake.id

def get_mistake(id):
    mistake = session.query(Mistake).get(id)
    return mistake

def update_mistake_cost(id, cost):
    mistake = session.query(Mistake).get(id)
    mistake.cost = cost
    session.commit()

def delete_mistake(id):
    mistake = session.query(Mistake).get(id)
    session.delete(mistake)
    session.commit()
