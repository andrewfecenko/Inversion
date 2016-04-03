from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.properties import StringProperty
from kivy.uix.accordion import AccordionItem
from database.db_function import *


class Archive(BoxLayout):

    def __init__(self, **kwargs):
        super(Archive, self).__init__(**kwargs)
        self.all_entries = get_all_entries_id()
        self.dates = {}
        self.category = {}

        if self.all_entries is None:
            self.list_empty_archive()
            return

        # Get all mistakes and get date list
        for ind, eid in enumerate(self.all_entries):
            mistakes_id = get_entry_mistakes_id(eid)
            print(mistakes_id)
            if mistakes_id is None:
                continue

            # parse all mistakes by date and categories
            for id in mistakes_id:
                # print(get_mistake_date(id))
                mistake_date = get_mistake_date(id).strftime("%Y-%m-%d")
                mistake_category = get_mistakes_category_id(id, True)

                if mistake_date not in self.dates:
                    self.dates[mistake_date] = [id]
                else:
                    self.dates[mistake_date].append(id)

                # if mistake_category not in self.category:
                #     self.category[mistake_category] = [id]
                # else:
                #     self.category[mistake_category].append(id)

    def order_by_category(self):
        for cate in self.category:
            accordItem = AccordionItem()
            scroll = ScrollView()
            grid = GridLayout(id='grid', size_hint_y=None, cols=1, row_default_height='100dp', row_force_default=True, spacing=20, padding=20)
            grid.bind(minimum_height=grid.setter('height'))
            scroll.add_widget(grid)
            accordItem.add_widget(scroll)
            accordItem.title = cate
            self.ids.container.add_widget(accordItem)

    def order_by_time(self):
        # Iterate over date list and order mistakes by date
        for date in self.dates:
            accordItem = AccordionItem()
            scroll = ScrollView()
            grid = GridLayout(id='grid', size_hint_y=None, cols=1, row_default_height='100dp', row_force_default=True, spacing=20, padding=20)
            grid.bind(minimum_height=grid.setter('height'))
            scroll.add_widget(grid)
            accordItem.add_widget(scroll)
            accordItem.title = date
            self.ids.container.add_widget(accordItem)

            id_list = self.dates[date]
            # date_title = Label(size_hint=(1, None), font_size='25sp', color=(0, 0, 0, 1), text=date)
            # self.archive_grid.add_widget(date_title)

            # go through all mistakes for the day
            for id in id_list:
                mistake_noun = get_mistake_noun(id)
                mistake_verb = get_mistake_verb(id)
                mistake_time = get_mistake_date(id).strftime("%H:%M:%S")
                mistake_cost = str(get_mistake_cost(id))



                new = Entry(name=mistake_noun, verb=mistake_verb, time=mistake_time, cost='-' + mistake_cost)
                # self.archive_grid.add_widget(new)
                grid.add_widget(new)

    def list_empty_archive(self):
        label = Label(text='You don\'t  have any mistakes!', font_size=40,
            halign='center')
        self.ids['mistake_scroll'].add_widget(label)


class Entry(BoxLayout):
    name = StringProperty('')
    verb = StringProperty('')
    time = StringProperty('')
    cost = StringProperty('')

