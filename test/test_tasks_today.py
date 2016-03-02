from db_function import tasks_today, create_entry
from db_model import build_database

def basic_test():
    basic_tasks = [u'Task 1', u'Task 2', u'Task 3']
    build_database()
    create_entry(["Task 1", "Task 2", "Task 3"])
    assert tasks_today() == basic_tasks
