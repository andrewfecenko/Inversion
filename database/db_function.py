from sqlalchemy.orm import sessionmaker

from db_model import Entry
from db_model import Mistake
from db_model import engine

from db_model import build_database
from db_model import clear_database

import datetime

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

def get_entry(givenday=datetime.datetime.now()):

    beg = givenday.replace(hour=0, minute=0, second=0, microsecond=0)
    end = givenday.replace(hour=23, minute=59, second=59, microsecond=59)

    # return entry for the givenday
    for entry in session.query(Entry).all():
        entry_time = entry.time_created
        if (entry_time <= end and entry_time >= beg):
            return entry.id

    return None

def get_entry_mistakes_id(eid):
    entry = session.query(Entry).get(eid)
    try:
        mistakes = entry.mistakes.all()
        mistakes_id = [m.id for m in mistakes]
    except AttributeError:
        mistakes_id = []
    return mistakes_id

def get_all_entries():
    for entry in session.query(Entry).all():
        yield entry

#######################################################################
# All functions for setting or getting information about a mistake.   #
#######################################################################

def create_mistake(eid, is_om, noun, cost):
    mistake = Mistake(entry_id=eid, is_om=is_om, noun=noun, cost=cost)
    session.add(mistake)
    session.commit()
    return mistake.id

def get_mistake(id):
    mistake = session.query(Mistake).get(id)
    return mistake

def get_mistake_noun(id):
	mistake = session.query(Mistake).get(id)
	noun = mistake.noun
	return noun

def get_mistake_cost(id):
	mistake = session.query(Mistake).get(id)
	cost = mistake.cost
	return cost

def update_mistake_noun(id, noun):
    mistake = session.query(Mistake).get(id)
    mistake.noun = noun
    session.commit()

def update_mistake_cost(id, cost):
    mistake = session.query(Mistake).get(id)
    mistake.cost = cost
    session.commit()

def delete_mistake(id):
    mistake = session.query(Mistake).get(id)
    session.delete(mistake)
    session.commit()

#######################################################################
# Functions for getting information about omissions or commissions.   #
#######################################################################

def get_mistakes_category_id(eid, is_om):
    mistake_ids = get_entry_mistakes_id(eid)
    mistakes = [get_mistake(id) for id in mistake_ids]
    mistakes = get_mistakes_category(mistakes, is_om)
    mistakes_id = [m.id for m in mistakes]
    return mistakes_id

def get_mistakes_range_id(begin, end):
    mistakes = session.query(Mistake).filter(Mistake.time_created <= end).\
        filter(Mistake.time_created >= begin)
    mistakes_id = [m.id for m in mistakes]
    return mistakes_id

def get_mistakes_category(mistakes, is_om):
    category_mistakes = filter(lambda x: x.is_om == is_om, mistakes)
    return category_mistakes


#######################################################################
# All functions for testing                                           #
#######################################################################

def partial_info_get():
    """TODO: delete this function."""
    clear_database()
    build_database()

    eid = create_entry()

    mid1 = create_mistake(eid, True, 'Didn\'t work', 50)
    mid2 = create_mistake(eid, False, 'Bought too much food', 30)

    omid_list = get_mistakes_category_id(eid, True)
    cmid_list = get_mistakes_category_id(eid, False)

    for omid in omid_list:
    	print("Omission mistake: {}-{} costs ${}".format(omid, get_mistake_noun(omid), get_mistake_cost(omid)))
    for cmid in cmid_list:
    	print("Commission mistake: {}-{} costs ${}".format(cmid, get_mistake_noun(cmid), get_mistake_cost(cmid)))

#partial_info_get()
