from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class AddEntry(BoxLayout):

    task_one = StringProperty()
    task_two = StringProperty()
    task_three = StringProperty()

    def __init__(self, **kwargs):
        super(AddEntry, self).__init__(**kwargs)


