from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex

tasks = [
    {
        'id': 1,
        'date': '2016-09-26 16:34:40.278298',  # python datetime
        'task': 'Be rich',
        'favorite': True,
        'tags': 'work',
        'complete': True},
    {
        'id': 2,
        'date': '2016-09-26 16:46:40.278298',  # python datetime
        'task': 'Finish A2',
        'favorite': False,
        'tags': 'study',
        'complete': False},
    {
        'id': 3,
        'date': '2016-09-26 18:46:40.278298',  # python datetime
        'task': 'Eat ramen',
        'favorite': False,
        'tags': 'food',
        'complete': True},
    {
        'id': 4,
        'date': '2016-09-26 18:48:40.278298',  # python datetime
        'task': 'Sleep',
        'favorite': True,
        'tags': 'sleeping',
        'complete': False},
    {
        'id': 2,
        'date': '2016-09-26 16:46:40.278298',  # python datetime
        'task': 'Finish A2',
        'favorite': False,
        'tags': 'study',
        'complete': False},
    {
        'id': 3,
        'date': '2016-09-26 18:46:40.278298',  # python datetime
        'task': 'Eat ramen',
        'favorite': False,
        'tags': 'food',
        'complete': True},
    {
        'id': 4,
        'date': '2016-09-26 18:48:40.278298',  # python datetime
        'task': 'Sleep',
        'favorite': True,
        'tags': 'sleeping',
        'complete': False},
    {
        'id': 2,
        'date': '2016-09-26 16:46:40.278298',  # python datetime
        'task': 'Finish A2',
        'favorite': False,
        'tags': 'study',
        'complete': False},
    {
        'id': 3,
        'date': '2016-09-26 18:46:40.278298',  # python datetime
        'task': 'Eat ramen',
        'favorite': False,
        'tags': 'food',
        'complete': True},
    {
        'id': 4,
        'date': '2016-09-26 18:48:40.278298',  # python datetime
        'task': 'Sleep',
        'favorite': True,
        'tags': 'sleeping',
        'complete': False},
    {
        'id': 2,
        'date': '2016-09-26 16:46:40.278298',  # python datetime
        'task': 'Finish A2',
        'favorite': False,
        'tags': 'study',
        'complete': False},
    {
        'id': 3,
        'date': '2016-09-26 18:46:40.278298',  # python datetime
        'task': 'Eat ramen',
        'favorite': False,
        'tags': 'food',
        'complete': True},
    {
        'id': 4,
        'date': '2016-09-26 18:48:40.278298',  # python datetime
        'task': 'Sleep',
        'favorite': True,
        'tags': 'sleeping',
        'complete': False},
    {
        'id': 2,
        'date': '2016-09-26 16:46:40.278298',  # python datetime
        'task': 'Finish A2',
        'favorite': False,
        'tags': 'study',
        'complete': False},
    {
        'id': 3,
        'date': '2016-09-26 18:46:40.278298',  # python datetime
        'task': 'Eat ramen',
        'favorite': False,
        'tags': 'food',
        'complete': True},
    {
        'id': 4,
        'date': '2016-09-26 18:48:40.278298',  # python datetime
        'task': 'Sleep',
        'favorite': True,
        'tags': 'sleeping',
        'complete': False},
    {
        'id': 2,
        'date': '2016-09-26 16:46:40.278298',  # python datetime
        'task': 'Finish A2',
        'favorite': False,
        'tags': 'study',
        'complete': False},
    {
        'id': 3,
        'date': '2016-09-26 18:46:40.278298',  # python datetime
        'task': 'Eat ramen',
        'favorite': False,
        'tags': 'food',
        'complete': True},
    {
        'id': 4,
        'date': '2016-09-26 18:48:40.278298',  # python datetime
        'task': 'Sleep',
        'favorite': True,
        'tags': 'sleeping',
        'complete': False}
]

# Create a form to add

# Create a task
class Task(GridLayout):
    def __init__(self, taskData, **args):
        super(Task, self).__init__(**args)

        # Layout of each task panel
        self.cols = 2
        self.size_hint = (0.9, 0.9)
        self.add_widget(CheckBox())
        self.add_widget(Label(text=taskData['task']))


# Create a list of tasks
class Tasks(GridLayout):
    def __init__(self, **args):
        super(Tasks, self).__init__(**args)

        # Layout of the task list
        self.bind(minimum_height=self.setter('height'))
        self.size_hint_y = None
        self.spacing = 0
        self.cols = 1
        self.row_default_height = 20

        for taskData in tasks:
            self.add_widget(Task(taskData))


# Scrollable container
class Container(ScrollView):
    def __init__(self, **args):
        super(Container, self).__init__(**args)

        # Layout of the scroll view
        self.size_hint_x = 0.8
        self.pos_hint = {'left': 0, 'right': 1, 'top': 0.2}
        self.add_widget(Tasks())


class UpdateEntry(BoxLayout):
    def __init__(self):
        super(UpdateEntry, self).__init__()
        self.add_widget(Container())