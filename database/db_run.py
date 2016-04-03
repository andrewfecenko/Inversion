from db_model import *
from db_function import *

clear_database()
build_database()

day1 = datetime.datetime(2014, 12, 13)
day2 = datetime.datetime(2015, 5, 4)
day3 = datetime.datetime(2016, 1, 5)
day4 = datetime.datetime(2016, 2, 12)
day5 = datetime.datetime(2016, 3, 23)
day6 = datetime.datetime(2016, 3, 24)

eid1 = create_entry(day1)
eid2 = create_entry(day2)
eid3 = create_entry(day3)
eid4 = create_entry(day4)
eid5 = create_entry(day5)
eid6 = create_entry(day6)

#day1
create_mistake(eid1, True, 'Missed math class', 10)
create_mistake(eid1, False, 'Bought junk food', 10)
#day2
create_mistake(eid2, True, 'Did not attend seminar', 10)
create_mistake(eid2, True, 'Did not call mom', 10)
#day3
create_mistake(eid3, True, 'Forgot to send email', 10)
create_mistake(eid3, False, 'Fought with friend', 10)
create_mistake(eid3, False, 'Spent money on booze', 10)
#day4
create_mistake(eid4, True, 'Missed database class', 10)
create_mistake(eid4, False, 'Ate 3 packs of jelly', 10)
#day5
create_mistake(eid5, True, 'Forgot to pay the bills', 10)
create_mistake(eid5, True, 'Did not complete homework', 10)
create_mistake(eid5, False, 'Drank too much', 10)
#day6
create_mistake(eid1, True, 'Did not brush teeth', 10)
create_mistake(eid1, False, 'Called ex', 10)