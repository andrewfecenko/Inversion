from database import tasks_today, create_entry

def basic_test():
    basic_tasks = [u'Task 1', u'Task 2', u'Task 3']
    create_entry(["Task 1", "Task 2", "Task 3"])
    assert tasks_today() == basic_tasks
