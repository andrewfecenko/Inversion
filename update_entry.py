from kivy.uix.accordion import AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import datetime
from kivy.core.window import Window
from  kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from database import create_task, add_summary, add_plan

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
class DetailedData(BoxLayout):
    def __init__(self, section_name, **args):
        super(DetailedData, self).__init__(**args)

        self.size_hint = (1, None)
        self.size = (Window.width, Window.height * 0.65)
        self.orientation = 'vertical'

        # Record new data to the section
        self.form = BoxLayout()
        self.form.cols = 2
        self.form.size_hint = (1, None)
        self.form.height = self.height * 0.05

        # input form
        self.input = TextInput()
        self.input.size_hint = (1, None)
        self.input.font_size = '15sp'
        self.input.height = 30
        self.form.add_widget(self.input)

        # input button
        self.add_button = Button()
        self.add_button.text = '+'
        self.add_button.size_hint = (1, None)
        self.add_button.font_size = '15sp'
        self.add_button.background_color = (1,1,1,0.2)
        self.add_button.color = (0, 1, 0, 1)
        self.add_button.height = 30
        self.add_button.bind(on_release=self.submit_form)
        self.form.add_widget(self.add_button)

        # Add data and edit button
        # TODO: make the edit button work
        for each in entry[section_name]:
            detail = BoxLayout()
            detail.cols = 2
            detail.size_hint = (1, None)
            detail.height = self.height * 0.05
            detail.width = self.width

            label = Label(text=each)
            label.size_hint = (1, None)
            label.font_size = '15sp'
            detail.add_widget(label)

            edit = Label(text = 'Edit')
            edit.size_hint = (1, None)
            edit.font_size = '15sp'
            detail.add_widget(edit)
            self.add_widget(detail)

        self.add_widget(self.form)


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
            add_summary(entry['eid'], input_value)
        elif section_name == 'plans':
            add_plan(entry['eid'], input_value)

class UpdateEntry(BoxLayout):
    def __init__(self):
        super(UpdateEntry, self).__init__()

        self.setHeader()
        self.setSections()


    # Set a header for the entry (date and failure points
    def setHeader(self):

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
    def setSections(self):
        for each in sections:
            item = AccordionItem()
            item.pos = (0,0)
            item.title = sections[each]
            detail = DetailedData(each)
            item.add_widget(detail)
            self.ids.container.add_widget(item)