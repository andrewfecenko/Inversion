from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from db_model import Entry
from db_model import Summary
from db_model import Plan
from db_model import Task
from db_model import CompletedTask
from db_model import Knowledge
from db_model import FailurePoint

from db_model import build_database
from db_model import clear_database

from collections import namedtuple

engine = create_engine('sqlite:///entries.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

#######################################################################
# Quick access method for all information of an entry                 #
#######################################################################

EntryContent = namedtuple('EntryContent', ['summary', 'plan', 'tasks',
        'completed_tasks', 'knowledges', 'failure_points', 'time_created'])

#######################################################################
# All functions for entering new entry information into the database  #
#######################################################################

def create_entry(task_list):
    new_entry = Entry()
    session.add(new_entry)
    session.commit()
    for content in task_list:
        create_task(new_entry.id, content)
    return new_entry.id

def create_alt_entry(task_list, givenday=datetime.datetime.now()):
    new_entry = Entry(time_created=givenday)
    session.add(new_entry)
    session.commit()
    for content in task_list:
        create_task(new_entry.id, content)
    return new_entry.id

def create_summary(eid, summary):
    new_summary = Summary(entry_id=eid, content=summary)
    session.add(new_summary)
    session.commit()
    return new_summary.id


def create_plan(eid, plan):
    new_plan = Plan(entry_id=eid, content=plan)
    session.add(new_plan)
    session.commit()
    return new_plan.id


def create_task(eid, task_content):
    new_task = Task(entry_id=eid, content=task_content)
    session.add(new_task)
    session.commit()
    return new_task.id


def create_completed_task(eid, task_content):
    new_completed_task = CompletedTask(entry_id=eid,
                                       content=task_content)
    session.add(new_completed_task)
    session.commit()
    return new_completed_task.id


def create_knowledge(eid, knowledge):
    new_knowledge = Knowledge(entry_id=eid, content=knowledge)
    session.add(new_knowledge)
    session.commit()
    return new_knowledge.id


def create_failure_point(eid, failure_point):
    new_failure_point = FailurePoint(entry_id=eid,
                                     content=failure_point)
    session.add(new_failure_point)
    session.commit()
    return new_failure_point.id


#######################################################################
# All functions for deleting entry information from the database      #
#######################################################################

def delete_entry(id):
    new_entry = session.query(Entry).get(id)
    session.delete(new_entry)
    session.commit()


def delete_summary(id):
    summary = session.query(Summary).get(id)
    session.delete(summary)
    session.commit()


def delete_plan(id):
    plan = session.query(Plan).get(id)
    session.delete(plan)
    session.commit()


def delete_task(id):
    task = session.query(Task).get(id)
    session.delete(task)
    session.commit()


def delete_completed_task(id):
    ctask = session.query(CompletedTask).get(id)
    session.delete(ctask)
    session.commit()


def delete_knowledge(id):
    knowledge = session.query(Knowledge).get(id)
    session.delete(knowledge)
    session.commit()


def delete_failure_point(id):
    failure = session.query(FailurePoint).get(id)
    session.delete(failure)
    session.commit()


#######################################################################
# All functions for retrieving entry information from the database    #
#######################################################################

def get_entry_summary(entry):
    try:
        summary = entry.summary.content
        sid = entry.summary.id
    except AttributeError:
        summary, sid = None, None
    return summary, sid


def get_entry_plan(entry):
    try:
        plan = entry.plan.content
        pid = entry.plan.id
    except AttributeError:
        plan, pid = None, None
    return plan, pid


def get_entry_tasks(entry):
    try:
        tasks = entry.tasks.all()
        tid_list = [t.id for t in tasks]
        tasks = [t.content for t in tasks]
    except AttributeError:
        tasks, tid_list = [], []
    return tasks, tid_list


def get_entry_completed_tasks(entry):
    try:
        completed_tasks = entry.completed_tasks.all()
        ctid_list = [ct.id for ct in completed_tasks]
        completed_tasks = [ct.content for ct in completed_tasks]
    except AttributeError:
        completed_tasks, ctid_list = [], []
    return completed_tasks, ctid_list


def get_entry_knowledge(entry):
    try:
        knowledges = entry.knowledges.all()
        kid_list = [k.id for k in knowledges]
        knowledges = [k.content for k in knowledges]
    except AttributeError:
        knowledges, kid_list = [], []
    return knowledges, kid_list


def get_entry_failure_points(entry):
    try:
        failure_points = entry.failure_points.all()
        fid_list = [f.id for f in failure_points]
        failure_points = [f.content for f in failure_points]
    except AttributeError:
        failure_points, fid_list = [], []
    return failure_points, fid_list

def get_entry_info(entry):
    """Get all of entry's info returned as an EntryContent object."""

    summary = get_entry_summary(entry)[0]
    plan = get_entry_plan(entry)[0]
    tasks = get_entry_tasks(entry)[0]
    completed_tasks = get_entry_completed_tasks(entry)[0]
    knowledges = get_entry_knowledge(entry)[0]
    failure_points = get_entry_failure_points(entry)[0]

    return EntryContent(summary, plan, tasks, completed_tasks, knowledges, failure_points, entry.time_created)


def get_all_entries():
    for entry in session.query(Entry).all():
        yield get_entry_info(entry)


#######################################################################
# All functions for updating entry information in the database        #
#######################################################################

def update_entry(id, newcontent):
    new_entry = session.query(Entry).get(id)
    new_entry.content = newcontent
    session.commit()


def update_summary(id, newcontent):
    summary = session.query(Summary).get(id)
    summary.content = newcontent
    session.commit()


def update_plan(id, newcontent):
    plan = session.query(Plan).get(id)
    plan.content = newcontent
    session.commit()


def update_task(id, newcontent):
    task = session.query(Task).get(id)
    task.content = newcontent
    session.commit()


def update_completed_task(id, newcontent):
    ctask = session.query(CompletedTask).get(id)
    ctask.content = newcontent
    session.commit()


def update_knowledge(id, newcontent):
    knowledge = session.query(Knowledge).get(id)
    knowledge.content = newcontent
    session.commit()


def update_failure_point(id, newcontent):
    failure = session.query(FailurePoint).get(id)
    failure.content = newcontent
    session.commit()


#######################################################################
# All functions for query filtering according to given input          #
#######################################################################

def tasks_today(givenday=None):
    if givenday == None:	# retrieve today's entry
        if get_days_entry() is None:
            return []
        days_entry = get_days_entry()
    else:					# retrieve givenday's entry
        if get_days_entry(givenday) is None:
            return []
        days_entry = get_days_entry(givenday)
    return get_entry_tasks(days_entry)[0]

def get_entry(eid):
    return session.query(Entry).get(eid)

def get_days_entry(givenday=datetime.datetime.now()):
    beg = givenday.replace(hour=0, minute=0, second=0, microsecond=0)
    end = givenday.replace(hour=23, minute=59, second=59, microsecond=59)

    for entry in session.query(Entry).all():
        entry_time = entry.time_created
        if (entry_time <= end and entry_time >= beg):
            return entry
    return None


def get_tasks_keyword(keyword):
    tasks = session.query(Task).filter(Task.content.contains(keyword))
    tasks = [t.content for t in tasks]
    return tasks


#######################################################################
# All functions for testing                                           #
#######################################################################

def partial_info_get():
    """TODO: delete this function."""
    clear_database()
    build_database()

    create_entry(["Task one", "Task two", "Task three"])
    todays_entry = get_days_entry(datetime.datetime.now())

    eid = todays_entry.id
    sid = create_summary(eid, "testing")
    pid = create_plan(eid, "final")
    kid = create_knowledge(eid, "knowledge")
    fid = create_failure_point(eid, "failed")
    cid1 = create_completed_task(eid, "finished something")
    cid2 = create_completed_task(eid, "finished another thing")

    delete_completed_task(cid1)
    update_completed_task(cid2, "new content")
    update_summary(sid, 'new summary')
    todays_entry_content = get_entry_info(todays_entry)
    print(todays_entry_content)
    print(get_tasks_keyword("task"))

#partial_info_get()
