import unittest

from db_function import create_entry, create_summary, create_plan,create_task, create_completed_task, create_knowledge, create_failure_point
from db_function import tasks_today, get_days_entry, get_entry_summary
from db_function import get_entry_plan, get_entry_tasks,get_entry_completed_tasks, get_entry_knowledge, get_entry_failure_points,get_entry_info, get_all_entries

from db_model import build_database, clear_database


class DBFunctionsTest(unittest.TestCase):

    todays_entry = None
    todays_entry_content = None

    @classmethod
    def setUpClass(self):

        clear_database()
        build_database()
        create_entry(["Task one", "Task two", "Task three"])
        DBFunctionsTest.todays_entry = get_days_entry()

        eid = DBFunctionsTest.todays_entry.id
        create_summary(eid, "Finished a bunch of testing.")
        create_plan(eid, "Go on a walk tomorrow.")
        create_knowledge(eid, "Learned about testing.")
        create_failure_point(eid, "Didn't write good tests.")
        create_completed_task(eid, "Wrote a test suite.")
        create_completed_task(eid, "Wrote about writing the test suite inside the test suite.")

        DBFunctionsTest.todays_entry_content = get_entry_info(DBFunctionsTest.todays_entry)

    @classmethod
    def tearDownClass(self):
        clear_database()

    def test_get_entry_summary(self):
        assert get_entry_summary(DBFunctionsTest.todays_entry)[0] == "Finished a bunch of testing."

    def test_get_entry_plan(self):
        assert get_entry_plan(DBFunctionsTest.todays_entry)[0] == "Go on a walk tomorrow."

    def test_get_entry_knowledge(self):
        assert get_entry_knowledge(DBFunctionsTest.todays_entry)[0] == ["Learned about testing."]

    def test_get_failure_point(self):
        assert get_entry_failure_points(DBFunctionsTest.todays_entry)[0] == ["Didn't write good tests."]

    def test_get_entry_tasks(self):
        assert get_entry_tasks(DBFunctionsTest.todays_entry)[0] == ["Task one", "Task two", "Task three"]

    def test_get_completed_task(self):
        assert get_entry_completed_tasks(DBFunctionsTest.todays_entry)[0] == ["Wrote a test suite.", 
            "Wrote about writing the test suite inside the test suite."]
