from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from db_function import create_entry
from db_model import build_database
from update_entry import UpdateEntry
from kivy.core.text import LabelBase
from db_function import *

KIVY_FONTS = [
    {
        "name": "RobotoCondensed",
        "fn_regular": "data/fonts/RobotoCondensed-Light.ttf",
        "fn_bold": "data/fonts/RobotoCondensed-Regular.ttf",
        "fn_italic": "data/fonts/RobotoCondensed-LightItalic.ttf",
        "fn_bolditalic": "data/fonts/RobotoCondensed-Italic.ttf"
    }
]

for font in KIVY_FONTS:
    LabelBase.register(**font)

total_entry_num = 1


class AddEntry(BoxLayout):

    added_tasks = BooleanProperty()

    def __init__(self, **kwargs):
        super(AddEntry, self).__init__(**kwargs)

        build_database()
        entry = get_days_entry()
        if entry:
            self.clear_widgets()
            self.add_widget(UpdateEntry())


        # TODO: create method to check if day's tasks have already been entered
        self.added_tasks = False
        self.entry_list = []
        self.task_grid.bind(minimum_height=self.task_grid.setter('height'))

    def add_new(self):
        global total_entry_num
        total_entry_num += 1
        new = Entry(name="TASK " + str(total_entry_num))
        self.children[1].children[0].add_widget(new)

    def submit_tasks(self):
        for child in self.children[1].children[0].children:
            if child.task_text != '':
                self.entry_list.append(child.task_text)

        if len(self.entry_list) < total_entry_num:
            content = Button(text='OK', pos_hint={'y': 2.1}, font_size='20sp', size_hint=(0.5, 0.2),
                             background_color=(52, 152, 219, 1), color=(0, 0, 0, 1))
            popup = Popup(title='Please fill all entries.', separator_height="0", title_size='20sp', content=content,
                            auto_dismiss=False, size_hint=(0.3, 0.2))
            content.bind(on_press=popup.dismiss)
            popup.open()
        else:
            print ','.join(self.entry_list)
            build_database()
            content = Button(text='OK', pos_hint={'y': 2.1}, font_size='20sp', size_hint=(0.5, 0.2),
                             background_color=(52, 152, 219, 1), color=(0, 0, 0, 1))
            popup = Popup(title='Day entries submitted!', separator_height="0", title_size='20sp', content=content,
                            auto_dismiss=False, size_hint=(0.3, 0.2))
            content.bind(on_press=popup.dismiss)
            popup.open()
            create_entry(self.entry_list)
            self.clear_widgets()
            self.add_widget(UpdateEntry())



class Entry(BoxLayout):
    name = StringProperty('')

    def remove(self):
        if self.parent is not None:
            ind = self.name.split(' ')[1]
            print ind
            for child in self.parent.children:
                if child.name.split(' ')[1] > ind:
                    child.name = 'task ' + str(int(child.name.split(' ')[1]) - 1)
            self.parent.remove_widget(self)
            global total_entry_num
            total_entry_num -= 1
