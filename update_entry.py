from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
import datetime
from kivy.core.window import Window

entry = {
    'id': 1,
    'time_created': '2009-01-05 22:14:39',
    'time_updated': '2009-01-05 22:14:39',
    'completed_tasks': ['task1', 'task2', 'task3','task1', 'task2', 'task3','task1', 'task2', 'task3','task1', 'task2', 'task3'],
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


# Create a data for a section (i.e. content inside the section)
class DetailedData(BoxLayout):
    def __init__(self, section_name, **args):
        super(DetailedData, self).__init__(**args)

        self.size_hint = (1, None)
        self.size = (Window.width, Window.height * 0.65)
        self.orientation = 'vertical'

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
        for each in sections.keys():
            item = AccordionItem()
            item.pos = (0,0)
            item.title = sections[each]
            detail = DetailedData(each)
            item.add_widget(detail)
            self.ids.container.add_widget(item)