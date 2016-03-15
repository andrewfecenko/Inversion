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

from collections import namedtuple

engine = create_engine('sqlite:///entries.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

#######################################################################
# Quick access method for all information of an entry.                #
#######################################################################

EntryContent = namedtuple('EntryContent', ['summary', 'plan', 'tasks',
        'completed_tasks', 'knowledges', 'failure_points'])

#######################################################################
# All functions for entering new entry information into the database. #
#######################################################################

def create_entry(task_list):
    new_entry = Entry()
    session.add(new_entry)
    session.commit()
    for content in task_list:
        create_task(new_entry.id, content)


def create_summary(eid, summary):
    new_summary = Summary(entry_id=eid, content=summary)
    session.add(new_summary)
    session.commit()


def create_plan(eid, plan):
    new_plan = Plan(entry_id=eid, content=plan)
    session.add(new_plan)
    session.commit()


def create_task(eid, task_content):
    new_task = Task(entry_id=eid, content=task_content)
    session.add(new_task)
    session.commit()


def create_completed_task(eid, task_content):
    new_completed_task = CompletedTask(entry_id=eid,
                                       content=task_content)
    session.add(new_completed_task)
    session.commit()


def create_knowledge(eid, knowledge):
    new_knowledge = Knowledge(entry_id=eid, content=knowledge)
    session.add(new_knowledge)
    session.commit()


def create_failure_point(eid, failure_point):
    new_failure_point = FailurePoint(entry_id=eid,
                                     content=failure_point)
    session.add(new_failure_point)
    session.commit()


#######################################################################
# All functions for entering new entry information into the database. #
#######################################################################

def delete_entry(task_list):
    new_entry = Entry()
    session.add(new_entry)
    session.commit()
    for content in task_list:
        create_task(new_entry.id, content)


def delete_summary(eid, summary):
    new_summary = Summary(entry_id=eid, content=summary)
    session.add(new_summary)
    session.commit()


def delete_plan(eid, plan):
    new_plan = Plan(entry_id=eid, content=plan)
    session.add(new_plan)
    session.commit()


def delete_task(eid, task_content):
    new_task = Task(entry_id=eid, content=task_content)
    session.add(new_task)
    session.commit()


def delete_completed_task(eid, task_content):
    new_completed_task = CompletedTask(entry_id=eid,
                                       content=task_content)
    session.add(new_completed_task)
    session.commit()


def delete_knowledge(eid, knowledge):
    new_knowledge = Knowledge(entry_id=eid, content=knowledge)
    session.add(new_knowledge)
    session.commit()


def delete_failure_point(eid, failure_point):
    new_failure_point = FailurePoint(entry_id=eid,
                                     content=failure_point)
    session.add(new_failure_point)
    session.commit()


#######################################################################
# All functions for retrieving information from the database.         #
#######################################################################

def tasks_today(givenday=None):
	if givenday == None:	# retrieve today's entry
		if not days_entry_exists():
			return []
		days_entry = get_days_entry()
	else:					# retrieve givenday's entry
		if not days_entry_exists(givenday):
			return []
		days_entry = get_days_entry(givenday)
    return get_entry_tasks(days_entry)


def get_todays_entry():
    """Get the Entry relation for today."""
    beg = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end = datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=59)

    for entry in session.query(Entry).all():
        entry_time = entry.time_created
        if (entry_time <= end and entry_time >= beg):
            return entry
    return None


def get_days_entry(givenday=datetime.datetime.now()):
	beg = givenday.replace(hour=0, minute=0, second=0, microsecond=0)
    end = givenday.replace(hour=23, minute=59, second=59, microsecond=59)

    for entry in session.query(Entry).all():
        entry_time = entry.time_created
        if (entry_time <= end and entry_time >= beg):
            return entry
    return None


def todays_entry_exists():
    return get_todays_entry() is not None


def get_entry_summary(entry):
    try:
        summary = entry.summary.content
    except AttributeError:
        summary = None
    return summary


def get_entry_plan(entry):
    try:
        plan = entry.plan.content
    except AttributeError:
        plan = None
    return plan


def get_entry_tasks(entry):
    try:
        tasks = entry.tasks.filter(Task.entry_id == entry.id)
        tasks = [t.content for t in tasks]
    except AttributeError:
        tasks = None
    return tasks


def get_entry_completed_tasks(entry):
    try:
        completed_tasks = entry.completed_tasks.filter(CompletedTask.entry_id == entry.id)
        completed_tasks = [ct.content for ct in completed_tasks]
    except AttributeError:
        completed_tasks = None
    return completed_tasks


def get_entry_knowledge(entry):
    try:
        knowledges = entry.knowledges.filter(Knowledge.entry_id == entry.id)
        knowledges = [k.content for k in knowledges]
    except AttributeError:
        knowledges = None
    return knowledges


def get_entry_failure_points(entry):
    try:
        failure_points = entry.failure_points.filter(FailurePoint.entry_id == entry.id)
        failure_points = [f.content for f in failure_points]
    except AttributeError:
        failure_points = None
    return failure_points


def get_entry_info(entry):
    """Get all of entry's info returned as an EntryContent object."""

    summary = get_entry_summary(entry)
    plan = get_entry_plan(entry)
    tasks = get_entry_tasks(entry)
    completed_tasks = get_entry_completed_tasks(entry)
    knowledge = get_entry_knowledge(entry)
    failure_points = get_entry_failure_points(entry)

    return EntryContent(summary, plan, tasks, completed_tasks, knowledge, failure_points)


def get_all_entries():
    for entry in session.query(Entry).all():
        yield get_entry_info(entry)
