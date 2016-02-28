from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

class AddEntry(BoxLayout):

    added_tasks = BooleanProperty()

    def __init__(self, **kwargs):
        super(AddEntry, self).__init__(**kwargs)
        # TODO: create method to check if day's tasks have already been entered
        self.added_tasks = False

    def submit_tasks(self):
        print self.ids.task_one_entry.task_text
        print self.ids.task_two_entry.task_text
        print self.ids.task_three_entry.task_text
