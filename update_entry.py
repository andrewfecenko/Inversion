from kivy.core.text import LabelBase
from kivy.uix.accordion import AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import datetime
from kivy.core.window import Window
from  kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from db_function import create_task, create_summary, create_plan

entry = {
    'eid': 1,
    'time_created': '2009-01-05 22:14:39',
    'time_updated': '2009-01-05 22:14:39',
    'completed_tasks': ['task1', 'task2', 'task3','task1', 'task2', 'task3','task1', 'task2', 'task3'],
    'failure_points': 200,
    'knowledge': ['knowledge1', 'knowledge2', 'knowledge3'],
    'plans': ['aaaaaa', 'waaaaaa', 'aeoefjfwnfoiec'],
    'summary': ['blaaah'],
    'tasks': ['Eat ramen', 'Run till die', 'Sleep all day', 'Do assignment']
}

sections = {
    'tasks': 'Goals',
    'completed_tasks': 'Goals met',
    'knowledge': 'Knowledge Gained',
    'plans': 'Plan for Tomorrow',
    'summary': 'Summary'
}


# Create a data for a section (i.e. content inside the section)
class DetailedData(ScrollView):
    def __init__(self, section_name, **kwargs):
        super(DetailedData, self).__init__(**kwargs)

        # Add data and edit button
        # TODO: make the edit button work
        for each in entry[section_name]:
            detail = Detail(each)
            self.ids['detailed_data'].add_widget(detail)

        # Add form at the end of the list
        form = Form()
        self.ids['detailed_data'].add_widget(form)


    # Handle onclick
    # TODO: dynamically add the new data to the list
    def submit_form(self, section_name):
        input_value = self.input.text
        print(input_value)
        if input_value == '':
            return None
        if section_name == 'tasks':
            create_task(entry['eid'], input_value)
        elif section_name == 'summary':
            create_summary(entry['eid'], input_value)
        elif section_name == 'plans':
            create_plan(entry['eid'], input_value)


class Detail(BoxLayout):
    def __init__(self, content, **kwargs):
        super(Detail, self).__init__(**kwargs)
        self.ids.content.text = content


class Form(BoxLayout):
    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)


class UpdateEntry(BoxLayout):
    def __init__(self, **kwargs):
        super(UpdateEntry, self).__init__(**kwargs)

        self.set_header()
        self.set_sections()

    # Set a header for the entry (date and failure points
    def set_header(self):

        # Set date
        full_date = datetime.datetime.strptime(entry['time_created'], "%Y-%m-%d %H:%M:%S")
        formatted_date = '{}, {} {}, {}'.format(full_date.strftime("%A"),\
                                            full_date.strftime("%B"),\
                                            full_date.strftime("%d"),\
                                            full_date.year)
        self.ids.header.text = formatted_date

        # Set failure points
        points = "Failure Points: {}".format(entry['failure_points'])
        self.ids.failure_points.text = points

    # Set sections for the entry
    def set_sections(self):
        for each in sections:
            item = AccordionItem()
            item.pos = (0,0)
            item.title = sections[each]
            detail = DetailedData(each)
            item.add_widget(detail)
            self.ids.container.add_widget(item)
