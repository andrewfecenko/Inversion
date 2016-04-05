from db_model import *
from db_function import *

clear_database()
build_database()

day1 = datetime.datetime(2016, 1, 13)
day2 = datetime.datetime(2016, 1, 20)
day3 = datetime.datetime(2016, 2, 9)
day4 = datetime.datetime(2016, 2, 7)
day5 = datetime.datetime(2016, 3, 13)
day6 = datetime.datetime(2016, 4, 5)

eid1 = create_entry(day1)
eid2 = create_entry(day2)
eid3 = create_entry(day3)
eid4 = create_entry(day4)
eid5 = create_entry(day5)
eid6 = create_entry(day6)

#day1
create_mistake(eid1, True, 'Missed',  'math class', 10)
create_mistake(eid1, False, 'Bought', 'junk food', 10)
#day2
create_mistake(eid2, True, 'Missed', 'seminar', 10)
create_mistake(eid2, True, 'Did not', 'call mom', 10)
#day3
create_mistake(eid3, True, 'Forgot', 'to email professor', 10)
create_mistake(eid3, True, 'Did not', 'hand in assignment on time', 30)
create_mistake(eid3, False, 'Spent', 'money on food delivery', 30)
#day4
create_mistake(eid4, True, 'Missed', 'database class', 10)
create_mistake(eid4, True, 'Missed', 'exam review session', 10)
#day5
create_mistake(eid5, True, 'Forgot', 'to pay the bills', 10)
create_mistake(eid5, True, 'Did not', 'do history readings today', 10)
create_mistake(eid5, True, 'Did not', 'do bonus assignment', 10)
#day6
create_mistake(eid6, True, 'Did not', 'go to the gym', 10)
create_mistake(eid6, False, 'Spent', 'too much time on history essay', 10)