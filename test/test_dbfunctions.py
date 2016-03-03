import unittest

from db_function import create_entry, create_summary, create_plan,create_task, create_completed_task, create_knowledge, create_failure_point
from db_function import tasks_today, get_todays_entry, get_entry_summary
from db_function import get_entry_plan, get_entry_tasks,get_entry_completed_tasks, get_entry_knowledge, get_entry_failure_points,get_entry_info, get_all_entries, print_entry_list_repr
from db_model import build_database, clear_database


class DBFunctionsTest(unittest.TestCase):

    todays_entry = None
    todays_entry_content = None

    @classmethod
    def setUpClass(self):

        build_database()
        create_entry(["Task one", "Task two", "Task three"])
        DBFunctionsTest.todays_entry = get_todays_entry()
        
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
        assert get_entry_summary(DBFunctionsTest.todays_entry) == "Finished a bunch of testing."

    def test_get_entry_plan(self):
        assert get_entry_plan(DBFunctionsTest.todays_entry) == "Go on a walk tomorrow."
