from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty
from kivy.uix.accordion import AccordionItem
from kivy.uix.textinput import TextInput
from database.db_function import *


class Archive(BoxLayout):

    def __init__(self, **kwargs):
        super(Archive, self).__init__(**kwargs)
        self.all_entries = []
        self.dates = {}
        self.category = {}
        self.searchFlag = False


        global archive_instance
        archive_instance = self

        if self.all_entries is None:
            self.list_empty_archive()
            return

        # Get all mistakes and get date list
        for ind, eid in enumerate(self.all_entries):
            mistakes_id = get_entry_mistakes_id(eid)
            if mistakes_id is None:
                continue

            # parse all mistakes by date and categories
            for id in mistakes_id:
                mistake_date = get_mistake_date(id).strftime("%Y-%m-%d")

                if mistake_date not in self.dates:
                    self.dates[mistake_date] = [id]
                else:
                    self.dates[mistake_date].append(id)

                self.category['omission'] = get_mistakes_category_id(True)
                self.category['commission'] = get_mistakes_category_id(False)

    def order_by_category(self):
        self.ids.container.clear_widgets()
        self.ids.search_holder.clear_widgets()
        self.ids.search_holder.size_hint=(1, 0)

        if self.searchFlag:
            self.searchFlag = False

        for cate in self.category:
            if cate == 'omission':
                accordItem = AccordionItem(background_normal='images/accordion_normal.png',
                                            background_selected='images/accordion_selected.png',
                                            background_disabled_normal='images/accordion_normal.png',
                                            background_disabled_selected='images/accordion_selected.png')
            else:
                accordItem = AccordionItem(background_normal='images/accordion_normal.png',
                                            background_selected='images/accordion_selected.png',
                                            background_disabled_normal='images/accordion_normal.png',
                                            background_disabled_selected='images/accordion_selected.png')
            scroll = ScrollView()
            grid = GridLayout(id='grid', size_hint_y=None, cols=1, row_default_height='80dp', row_force_default=True, spacing=20, padding=20)
            grid.bind(minimum_height=grid.setter('height'))
            scroll.add_widget(grid)
            accordItem.add_widget(scroll)
            accordItem.title = cate
            accordItem.font_name = 'Ubuntu'
            self.ids.container.add_widget(accordItem)

            id_list = self.category[cate]

            for id in id_list:
                mistake_noun = get_mistake_noun(id)
                mistake_verb = get_mistake_verb(id)
                mistake_time = get_mistake_date(id).strftime("%H:%M:%S")
                mistake_cost = str(get_mistake_cost(id))

                new = Entry(name=mistake_noun, verb=mistake_verb, time=mistake_time, cost= mistake_cost)
                grid.add_widget(new)

        self.ids.by_day.background_color = get_color_from_hex('#5D535E')
        self.ids.by_cat.background_color = get_color_from_hex('#669999')
        self.ids.by_search.background_color = get_color_from_hex('#5D535E')

    def order_by_time(self):
        self.all_entries = []
        self.dates = {}
        self.category = {}

        self.ids.container.clear_widgets()
        self.ids.search_holder.clear_widgets()
        self.ids.search_holder.size_hint=(1, 0)

        self.all_entries = get_all_entries_id()

        if self.all_entries is None:
            self.list_empty_archive()
            return

        # Get all mistakes and get date list
        for ind, eid in enumerate(self.all_entries):
            mistakes_id = get_entry_mistakes_id(eid)
            if mistakes_id is None:
                continue

            # parse all mistakes by date and categories
            for id in mistakes_id:
                mistake_date = get_mistake_date(id).strftime("%Y-%m-%d")

                if mistake_date not in self.dates:
                    self.dates[mistake_date] = [id]
                else:
                    self.dates[mistake_date].append(id)

                self.category['omission'] = get_mistakes_category_id(True)
                self.category['commission'] = get_mistakes_category_id(False)

        if self.searchFlag:
            self.searchFlag = False

        self.sortedDate= []
        for date in self.dates:
            self.sortedDate.append(datetime.datetime.strptime(date, '%Y-%m-%d').date())

        print("date: " + str(sorted(self.sortedDate)))

        # Iterate over date list and order mistakes by date
        for date in sorted(self.sortedDate):
            accordItem = AccordionItem(background_normal='images/accordion_normal.png',
                                        background_selected='images/accordion_selected.png',
                                        background_disabled_normal='images/accordion_normal.png',
                                        background_disabled_selected='images/accordion_selected.png')
            scroll = ScrollView()
            grid = GridLayout(id='grid', size_hint_y=None, cols=1, row_default_height='80dp', row_force_default=True, spacing=20, padding=20)
            grid.bind(minimum_height=grid.setter('height'))
            scroll.add_widget(grid)
            accordItem.add_widget(scroll)
            accordItem.title = date.strftime("%Y-%m-%d")
            self.ids.container.add_widget(accordItem)

            id_list = self.dates[date.strftime("%Y-%m-%d")]

            # go through all mistakes for the day
            for id in id_list:
                mistake_noun = get_mistake_noun(id)
                mistake_verb = get_mistake_verb(id)
                mistake_time = get_mistake_date(id).strftime("%H:%M:%S")
                mistake_cost = str(get_mistake_cost(id))

                new = Entry(name=mistake_noun, verb=mistake_verb, time=mistake_time, cost=mistake_cost)
                grid.add_widget(new)

        self.ids.by_day.background_color = get_color_from_hex('#669999')
        self.ids.by_cat.background_color = get_color_from_hex('#5D535E')
        self.ids.by_search.background_color = get_color_from_hex('#5D535E')

    def search(self):
        if self.searchFlag:
            return
        self.ids.container.clear_widgets()

        self.ids.by_day.background_color = get_color_from_hex('#5D535E')
        self.ids.by_cat.background_color = get_color_from_hex('#5D535E')
        self.ids.by_search.background_color = get_color_from_hex('#669999')
        self.ids.search_holder.size_hint=(1, 0.07)
        self.ids.search_holder.add_widget(SearchInput(search_text=""))
        self.searchFlag = True



    def searchList(self, mistakes_id):
        self.ids.container.clear_widgets()
        if len(mistakes_id) == 0:
            accordItem = AccordionItem(background_normal='images/accordion_normal.png',
                                        background_selected='images/accordion_selected.png',
                                        background_disabled_normal='images/accordion_normal.png',
                                        background_disabled_selected='images/accordion_selected.png')
            accordItem.title = "No archive found!"
            self.ids.container.add_widget(accordItem)

        dates = {}

        for id in mistakes_id:
                mistake_date = get_mistake_date(id).strftime("%Y-%m-%d")

                if mistake_date not in dates:
                    dates[mistake_date] = [id]
                else:
                    dates[mistake_date].append(id)

        for date in dates:
            accordItem = AccordionItem(background_normal='images/accordion_normal.png',
                                        background_selected='images/accordion_selected.png',
                                        background_disabled_normal='images/accordion_normal.png',
                                        background_disabled_selected='images/accordion_selected.png')
            scroll = ScrollView()
            grid = GridLayout(id='grid', size_hint_y=None, cols=1, row_default_height='80dp', row_force_default=True, spacing=20, padding=20)
            grid.bind(minimum_height=grid.setter('height'))
            scroll.add_widget(grid)
            accordItem.add_widget(scroll)
            accordItem.title = date
            self.ids.container.add_widget(accordItem)

            id_list = dates[date]

            # go through all mistakes for the day
            for id in id_list:
                mistake_noun = get_mistake_noun(id)
                mistake_verb = get_mistake_verb(id)
                mistake_time = get_mistake_date(id).strftime("%H:%M:%S")
                mistake_cost = str(get_mistake_cost(id))

                new = Entry(name=mistake_noun, verb=mistake_verb, time=mistake_time, cost=mistake_cost)
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


class SearchInput(BoxLayout):
    search_text = StringProperty('')

    def verb_search(self):
        mistakes_id = get_mistakes_with_verb(self.search_text)
        archive_instance.searchList(mistakes_id)

    def noun_search(self):
        mistakes_id = get_mistakes_with_keyword(self.search_text)
        archive_instance.searchList(mistakes_id)

class Menu(GridLayout):
    pass