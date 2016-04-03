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
# All functions dealing with entries                                  #
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

def get_all_entries_id():
    all_entries = session.query(Entry).all()
    if all_entries is None:
        yield None
    for entry in all_entries:
        yield entry.id


#######################################################################
# All functions for setting or getting information about a mistake    #
#######################################################################

def create_mistake(eid, is_om, verb, noun, cost):
    mistake = Mistake(entry_id=eid, is_om=is_om, verb=verb, noun=noun, cost=cost)
    session.add(mistake)
    session.commit()
    return mistake.id

def get_mistake(id):
    mistake = session.query(Mistake).get(id)
    return mistake

def get_mistake_verb(id):
    mistake = session.query(Mistake).get(id)
    verb = mistake.verb
    return verb

def get_mistake_noun(id):
    mistake = session.query(Mistake).get(id)
    noun = mistake.noun
    return noun

def get_mistake_date(id):
	mistake = session.query(Mistake).get(id)
	date = mistake.time_created
	return date

def get_mistake_cost(id):
    mistake = session.query(Mistake).get(id)
    cost = mistake.cost
    return cost

def update_mistake_verb(id, verb):
    mistake = session.query(Mistake).get(id)
    mistake.verb = verb
    session.commit()

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
# All functions for getting information about omissions or commissions#
#######################################################################

def get_mistakes_category_id(eid, is_om):
	mistakes = session.query(Mistake).filter(Mistake.entry_id == eid).\
		filter(Mistake.is_om == is_om)
	mistakes_id = [m.id for m in mistakes]
	return mistakes_id

def get_mistakes_range_id(begin, end):
    mistakes = session.query(Mistake).filter(Mistake.time_created <= end).\
        filter(Mistake.time_created >= begin)
    mistakes_id = [m.id for m in mistakes]
    return mistakes_id


#######################################################################
# All functions relating keywords (verb, noun)                        #
#######################################################################

def get_mistakes_with_verb(verb):
	mistakes = session.query(Mistake).filter(Mistake.verb == verb)
	mistakes_id = [m.id for m in mistakes]
	return mistakes_id

def get_mistakes_with_keyword(keyword):
	mistakes = session.query(Mistake).filter(Mistake.noun.contains(keyword))
	mistakes_id = [m.id for m in mistakes]
	return mistakes_id

#######################################################################
# All functions for statistics                                        #
#######################################################################

def get_all_days():
    #days = session.query(Entry).all()
    #days = sorted(set([e.time_created for e in days]))
    days = session.query(Entry.time_created).distinct()
    days = [d[0] for d in days]
    return days

def get_day_cost(givenday=datetime.datetime.now()):
    beg = givenday.replace(hour=0, minute=0, second=0, microsecond=0)
    end = givenday.replace(hour=23, minute=59, second=59, microsecond=59)
    return get_range_cost(beg, end)

def get_total_cost():
    beg = datetime.datetime.min
    end = datetime.datetime.max
    return get_range_cost(beg, end)

def get_range_cost(begin, end):
    mid_list = get_mistakes_range_id(begin, end)
    total = 0
    for mid in mid_list:
        total = total + get_mistake_cost(mid)
    return total

def get_daily_cost():
    daily_cost = [get_day_cost(d) for d in get_all_days()]
    return daily_cost

def get_day_mistake_num(givenday=datetime.datetime.now()):
    beg = givenday.replace(hour=0, minute=0, second=0, microsecond=0)
    end = givenday.replace(hour=23, minute=59, second=59, microsecond=59)
    return get_range_mistake_num(beg, end)

def get_total_mistake_num():
    beg = datetime.datetime.min
    end = datetime.datetime.max
    return get_range_mistake_num(beg, end)

def get_range_mistake_num(begin, end):
    return len(get_mistakes_range_id(begin, end))

def get_daily_mistake_num():
    daily_num = [get_day_mistake_num(d) for d in get_all_days()]
    return daily_num


#######################################################################
# All functions for testing                                           #
#######################################################################

def partial_info_get():
    clear_database()
    build_database()

    eid = create_entry()

    mid1 = create_mistake(eid, True, 'Did not', 'work out', 50)
    mid2 = create_mistake(eid, False, 'Bought', 'too much food', 30)

    omid_list = get_mistakes_category_id(eid, True)
    cmid_list = get_mistakes_category_id(eid, False)

    for omid in omid_list:
        print("Omission mistake: {} {} costs ${}".format(get_mistake_verb(omid), get_mistake_noun(omid), get_mistake_cost(omid)))
    for cmid in cmid_list:
        print("Commission mistake: {} {} costs ${}".format(get_mistake_verb(cmid), get_mistake_noun(cmid), get_mistake_cost(cmid)))

    print(get_daily_cost())
    print(get_daily_mistake_num())

#partial_info_get()
