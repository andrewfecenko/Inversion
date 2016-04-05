from sqlalchemy.orm import sessionmaker

from db_model import Entry
from db_model import Mistake
from db_model import engine

from db_model import build_database
from db_model import clear_database

import datetime
from isoweek import Week

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

def get_entry_by_id(eid):
    entry = session.query(Entry).get(eid)
    return entry

def get_entry_mistakes_id(eid):
    try:
        mistakes = session.query(Mistake).filter(Mistake.entry_id == eid, Mistake.noun != '').all()
        mistakes_id = [m.id for m in mistakes]
        # print(mistakes_id)
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
    entry = get_entry_by_id(eid)
    givenday = datetime.datetime.now()
    time = givenday.replace(month=entry.time_created.month, day=entry.time_created.day)

    mistake = Mistake(entry_id=eid, is_om=is_om, verb=verb, noun=noun, cost=cost, time_created=time)
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

def get_entry_category_id(eid, is_om):
    mistakes = session.query(Mistake).filter(Mistake.entry_id == eid).\
        filter(Mistake.is_om == is_om)
    mistakes_id = [m.id for m in mistakes]
    return mistakes_id

def get_mistakes_category_id(is_om):
    mistakes = session.query(Mistake).filter(Mistake.is_om == is_om, Mistake.noun != '')
    mistakes_id = [m.id for m in mistakes]
    return mistakes_id

def get_mistakes_range_id(begin, end):
    mistakes = session.query(Mistake).filter(Mistake.time_created <= end).\
        filter(Mistake.time_created >= begin)
    mistakes_id = [m.id for m in mistakes]
    return mistakes_id

def get_all_mistakes_id():
    mistakes = session.query(Mistake).all()
    mistakes_id = [m.id for m in mistakes]
    return mistakes_id

def get_mistakes_range_category_len(begin, end):
    om = session.query(Mistake).filter(Mistake.time_created <= end).\
        filter(Mistake.time_created >= begin).filter(Mistake.is_om == True).all()
    cm = session.query(Mistake).filter(Mistake.time_created <= end).\
        filter(Mistake.time_created >= begin).filter(Mistake.is_om == False).all()
    return len(om), len(cm)


#######################################################################
# All functions relating keywords (verb, noun)                        #
#######################################################################

def get_all_verbs(is_om=None):
    if is_om == True or is_om == False:
        mistakes = session.query(Mistake).filter(Mistake.is_om == is_om)
    else:
        mistakes = session.query(Mistake).all()
    verbs = sorted(set([m.verb for m in mistakes]))
    return verbs # list of strings

def get_mistakes_with_verb(verb):
    mistakes = session.query(Mistake).filter(Mistake.verb == verb.capitalize())
    mistakes_id = [m.id for m in mistakes]
    return mistakes_id

def get_mistakes_with_keyword(keyword):
    mistakes = session.query(Mistake).filter(Mistake.noun.contains(keyword))
    mistakes_id = [m.id for m in mistakes]
    return mistakes_id

def get_verb_graph(is_om=None):
    verbs = get_all_verbs(is_om)
    return [len(get_mistakes_with_verb(v)) for v in verbs]


#######################################################################
# All functions for extracting distinct timestamps                    #
#######################################################################

def get_all_days():
    entries = session.query(Entry).all()
    days = sorted(set([e.time_created for e in entries]))
    #days = session.query(Entry.time_created).distinct()
    #days = [d[0] for d in days]
    return days # list of datetimes

def get_all_weeks():
    entries = session.query(Entry).all()
    weeks = sorted(set([e.time_created.isocalendar()[1] for e in entries]))
    return weeks # list of ints

def get_all_months():
    entries = session.query(Entry).all()
    months = sorted(set([e.time_created.month for e in entries]))
    return months # list of ints

def days_to_ints(days):
    ints = []
    for d in days:
        ints.append((d.month, d.day))
    return ints


#######################################################################
# All functions for generating accumulated data                       #
#######################################################################

def get_daily(day_f):
    daily = [day_f(d) for d in get_all_days()]
    return daily

def get_weekly(range_f):
    weeks = get_all_weeks()
    weekly = []
    for w in weeks:
        d = Week(2016, w).sunday()
        beg = datetime.datetime(d.year, d.month, d.day, 0, 0)
        end = datetime.datetime(d.year, d.month, d.day+7, 0, 0)
        weekly.append(range_f(beg, end))
    return weekly

def get_monthly(range_f):
    months = get_all_months()
    monthly = []
    for m in months:
        beg = datetime.datetime(2016, m, 1, 0, 0)
        end = datetime.datetime(2016, m+1, 1, 0, 0)
        monthly.append(range_f(beg, end))
    return monthly


#######################################################################
# All functions for cost statistics                                   #
#######################################################################

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
    return get_daily(get_day_cost)

def get_weekly_cost():
    return get_weekly(get_range_cost)

def get_monthly_cost():
    return get_monthly(get_range_cost)


#######################################################################
# All functions for mistake number statistics                         #
#######################################################################

def get_day_mistake_num(givenday=datetime.datetime.now()):
    beg = givenday.replace(hour=0, minute=0, second=0, microsecond=0)
    end = givenday.replace(hour=23, minute=59, second=59, microsecond=59)
    return get_range_mistake_num(beg, end)

def get_day_mistake_tuple(givenday=datetime.datetime.now()):
    beg = givenday.replace(hour=0, minute=0, second=0, microsecond=0)
    end = givenday.replace(hour=23, minute=59, second=59, microsecond=59)
    return get_mistakes_range_category_len(beg, end)

def get_total_mistake_num():
    beg = datetime.datetime.min
    end = datetime.datetime.max
    return get_range_mistake_num(beg, end)

def get_range_mistake_num(begin, end):
    return len(get_mistakes_range_id(begin, end))

def get_daily_mistake_num():
    daily_num = [get_day_mistake_num(d) for d in get_all_days()]
    return daily_num

def get_daily_mistake_num():
    return get_daily(get_day_mistake_num)

def get_weekly_mistake_num():
    return get_weekly(get_range_mistake_num)

def get_monthly_mistake_num():
    return get_monthly(get_range_mistake_num)

def get_daily_mistake_tuple():
    tuples = get_daily(get_day_mistake_tuple)
    om_list = [t[0] for t in tuples]
    cm_list = [t[1] for t in tuples]
    return (om_list, cm_list)

def get_weekly_mistake_tuple():
    tuples = get_weekly(get_mistakes_range_category_len)
    om_list = [t[0] for t in tuples]
    cm_list = [t[1] for t in tuples]
    return (om_list, cm_list)

def get_monthly_mistake_tuple():
    tuples = get_monthly(get_mistakes_range_category_len)
    om_list = [t[0] for t in tuples]
    cm_list = [t[1] for t in tuples]
    return (om_list, cm_list)


#######################################################################
# All functions for testing                                           #
#######################################################################

def partial_info_get():
    '''
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
    '''
    print("Daily cost: {}".format(get_daily_cost()))
    print("Weekly cost: {}".format(get_weekly_cost()))
    print("Monthly cost: {}".format(get_monthly_cost()))
    print("")

    print("Daily mistkae #: {}".format(get_daily_mistake_num()))
    print("Weekly mistake #: {}".format(get_weekly_mistake_num()))
    print("Monthly mistake #: {}".format(get_monthly_mistake_num()))
    print("")

    print("Daily OM mistkae #: {}".format(get_daily_mistake_tuple()[0]))
    print("Daily CM mistkae #: {}".format(get_daily_mistake_tuple()[1]))
    print("")

    print("List of OM verbs: {}".format(get_all_verbs(True)))
    print("List of occurrences: {}".format(get_verb_graph(True)))
    print("")

    print("List of CM verbs: {}".format(get_all_verbs(False)))
    print("List of occurrences: {}".format(get_verb_graph(False)))
    print("")

    print("List of ALL verbs: {}".format(get_all_verbs()))
    print("List of occurrences: {}".format(get_verb_graph()))
    print("")

if __name__ == '__main__':
    partial_info_get()
