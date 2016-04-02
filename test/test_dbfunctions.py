import unittest
import datetime
from db_function import *


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

class DBFunctionsCollectionTest(unittest.TestCase):


    @classmethod
    def setUpClass(self):

        clear_database()
        build_database()

        yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
        create_alt_entry(['First', 'Second', 'Third'], yesterday)

        past_first = datetime.datetime(2016, 3, 5)
        past_second = datetime.datetime(2015, 4, 12)
        past_third = datetime.datetime(2014, 12, 13)

        create_alt_entry(['First', 'Second', 'Third'], past_first)
        create_alt_entry(['First', 'Second', 'Third'], past_second)
        create_alt_entry(['First', 'Second', 'Third'], past_third)


    @classmethod
    def tearDownClass(self):
        clear_database()

    def test_get_all_entries_count(self):
        num_entries = 0
        all_entries = get_all_entries()
        if all_entries is None:
            assert False
        for entry in all_entries:
            num_entries += 1
        
        assert num_entries == 4
