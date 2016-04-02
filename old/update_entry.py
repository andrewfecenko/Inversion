from kivy.uix.accordion import AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from db_function import *
import collections

# entry = {
#     'eid': 1,
#     'time_created': '2009-01-05 22:14:39',
#     'time_updated': '2009-01-05 22:14:39',
#     'completed_tasks': ['task1', 'task2', 'task3','task1', 'task2', 'task3','task1', 'task2', 'task3'],
#     'failure_points': 200,
#     'knowledge': ['knowledge1', 'knowledge2', 'knowledge3'],
#     'plans': ['aaaaaa', 'waaaaaa', 'aeoefjfwnfoiec'],
#     'summary': ['blaaah'],
#     'tasks': ['Eat ramen', 'Run till die', 'Sleep all day', 'Do assignment']
# }

sections = collections.OrderedDict(
    (('tasks', 'Tasks'),
    ('completed_tasks', 'Tasks Achieved'),
    ('failure_points', 'Mistakes'),
    ('knowledge', 'Knowledge Gained'),
    ('plans', 'Plan for Tomorrow'),
    ('summaries', 'Summary'))
)


# Create a data for a section (i.e. content inside the section)
class DetailedData(ScrollView):
    def __init__(self, section_name, **kwargs):
        super(DetailedData, self).__init__(**kwargs)

        self.section_name = section_name
        self.set_contents()

    def set_contents(self):
        # Add data and edit button
        # TODO: make the edit button work
        if self.section_name == 'tasks':
            section = get_entry_tasks(entry)
        elif self.section_name == 'summaries':
            tmp = get_entry_summary(entry)
            section = [tmp[0]], [tmp[1]]
        elif self.section_name == 'plans':
            tmp = get_entry_plan(entry)
            section = [tmp[0]], [tmp[1]]
        elif self.section_name == 'knowledge':
            section = get_entry_knowledge(entry)
        elif self.section_name == 'failure_points':
            section = get_entry_failure_points(entry)
        elif self.section_name == 'completed_tasks':
            section = get_entry_completed_tasks(entry)

        if section == ([None], [None]):
            section = [], []

        # Add form at the end of the list if the section can contain multiple entries
        if self.section_name not in ['summaries', 'plans'] or \
                (self.section_name in ['summaries', 'plans'] and section == ([], [])):
            self.ids['detail_container'].add_widget(Form(self))

        # Add entries for the section
        items = section[0]
        ids = section[1]
        for i in range(0, len(ids)):
            detail = Detail(items[i], ids[i], self)
            self.ids['detail_container'].add_widget(detail)


class Detail(BoxLayout):
    def __init__(self, item, item_id, section, **kwargs):
        super(Detail, self).__init__(**kwargs)
        self.item = item
        self.id = str(item_id)
        self.ids['content'].text = self.item
        self.section = section

    def delete_data(self):
        if self.section.section_name == 'tasks':
            delete_task(self.id)
        elif self.section.section_name == 'summaries':
            delete_summary(self.id)
        elif self.section.section_name == 'plans':
            delete_plan(self.id)
        elif self.section.section_name == 'knowledge':
            delete_knowledge(self.id)
        elif self.section.section_name == 'failure_points':
            delete_failure_point(self.id)
        elif self.section.section_name == 'completed_tasks':
            delete_completed_task(self.id)

        self.section.ids['detail_container'].clear_widgets()
        self.section.set_contents()

    def update_data(self):
        self.clear_widgets()
        self.add_widget(EditForm(self))


class EditForm(BoxLayout):
    def __init__(self, detail, **kwargs):
        super(EditForm, self).__init__(**kwargs)
        self.detail = detail
        self.ids.input_field.text = detail.item

    # Handle onclick
    def submit_form(self):
        input_value = self.ids.input_field.text

        if input_value == '':
            return None
        elif self.detail.section.section_name == 'tasks':
            update_task(self.detail.id, input_value)
        elif self.detail.section.section_name == 'summaries':
            update_summary(self.detail.id, input_value)
        elif self.detail.section.section_name == 'plans':
            update_plan(self.detail.id, input_value)
        elif self.detail.section.section_name == 'knowledge':
            update_knowledge(self.detail.id, input_value)
        elif self.detail.section.section_name == 'failure_points':
            update_failure_point(self.detail.id, input_value)
        elif self.detail.section.section_name == 'completed_tasks':
            update_completed_task(self.detail.id, input_value)

        self.detail.section.ids['detail_container'].clear_widgets()
        self.detail.section.set_contents()


class Form(BoxLayout):
    def __init__(self, section, **kwargs):
        super(Form, self).__init__(**kwargs)
        self.section = section

    # Handle onclick
    def submit_form(self):
        input_value = self.ids.input_field.text

        if input_value == '':
            return None
        elif self.section.section_name == 'tasks':
            create_task(entry.id, input_value)
        elif self.section.section_name == 'summaries':
            create_summary(entry.id, input_value)
        elif self.section.section_name == 'plans':
            create_plan(entry.id, input_value)
        elif self.section.section_name == 'knowledge':
            create_knowledge(entry.id, input_value)
        elif self.section.section_name == 'failure_points':
            create_failure_point(entry.id, input_value)
        elif self.section.section_name == 'completed_tasks':
            create_completed_task(entry.id, input_value)

        self.section.ids['detail_container'].clear_widgets()
        self.section.set_contents()


class UpdateEntry(BoxLayout):
    def __init__(self, given_day=None, **kwargs):
        super(UpdateEntry, self).__init__(**kwargs)

        build_database()
        global entry

        if not given_day:
            entry = get_days_entry()
        else:
            entry = get_days_entry(given_day)

        if entry:
            self.set_header()
            self.set_sections()

        global page
        page = self

    # Set a header for the entry (date and failure points
    def set_header(self):

        # Set date
        full_date = datetime.datetime.strptime(str(get_days_entry().time_created), "%Y-%m-%d %H:%M:%S.%f")
        formatted_date = '{} {} {}, {}'.format(full_date.strftime("%A"),
                                               full_date.strftime("%B"),
                                               full_date.strftime("%d"),
                                               full_date.year)
        self.ids.header.text = formatted_date

    # Set sections for the entry
    def set_sections(self):
        for each in sections:
            item = AccordionItem()
            item.pos = (0, 0)
            item.title = sections[each]
            detail = DetailedData(each)
            item.add_widget(detail)
            self.ids.container.add_widget(item)
