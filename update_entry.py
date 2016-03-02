from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.listview import ListView
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.utils import get_color_from_hex
import datetime

entry = {
    'id': 1,
    'time_created': '2009-01-05 22:14:39',
    'time_updated': '2009-01-05 22:14:39',
    'completed_tasks': ['task1', 'task2', 'task3'],
    'failure_points': 200,
    'knowledge': ['knowledge1', 'knowledge2', 'knowledge3'],
    'plans': ['aaaaaa', 'waaaaaa', 'aeoefjfwnfoiec'],
    'summary': 'blaaah',
    'tasks': ['Eat ramen', 'Run till die', 'Sleep all day', 'Do assignment']
}

sections = {
    'tasks': 'Goals',
    'completed_tasks': 'Goals met',
    'knowledge': 'Knowledge Gained',
    'plans': 'Plan for Tomorrow'
}

panel_open = False

# Create an section (i.e. goals, achievements, etc.)
class Section(AccordionItem):
    def __init__(self, section_name, **args):
        super(Section, self).__init__(**args)

        for each in entry[section_name]:
            self.add_widget(DetailedData(each))

        # styles
        self.title = sections[section_name]
        self.background_color = (1, 1, 1, 1)

# Create a data for a section (i.e. content inside the section)
class DetailedData(BoxLayout):
    def __init__(self, data, **args):
        super(DetailedData, self).__init__(**args)

        self.add_widget(Label(text=data))
        #self.add_widget(Button(text='edit'))

        # styles
        self.background_color = (0, 0, 0, 1)


# Scrollable container
class Container(Accordion):
    def __init__(self, **args):
        super(Container, self).__init__(**args)

        for each in sections.keys():
            self.add_widget(Section(each))

        # style
        self.orientation = 'vertical'


class ScrollContainer(ScrollView):
    def __init__(self):
        super(ScrollContainer, self).__init__()

        self.add_widget(Container())

        # styles
        self.background_color = (0, 0, 0, 1)

class Header(GridLayout):
    def __init__(self):
        super(Header, self).__init__()

        full_date = datetime.datetime.strptime(entry['time_created'], "%Y-%m-%d %H:%M:%S")
        formatted_date = '{}, {} {}, {}'.format(full_date.strftime("%A"),\
                                            full_date.strftime("%B"),\
                                            full_date.strftime("%d"),\
                                            full_date.year)

        self.add_widget(Label(text=formatted_date))
        self.add_widget(Label(text=str(entry['failure_points'])))

        # Styles
        self.cols = 2
        self.size_hint_y = 0.1
        self.pos_hint = {'top': 0, 'left': 0}

class UpdateEntry(BoxLayout):
    def __init__(self):
        super(UpdateEntry, self).__init__()

        self.add_widget(Header())
        self.add_widget(ScrollContainer())

        # Styles
        self.orientation = 'vertical'