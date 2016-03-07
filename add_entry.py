from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from db_function import create_entry
from db_model import build_database


total_entry_num = 3


class AddEntry(BoxLayout):

    added_tasks = BooleanProperty()

    def __init__(self, **kwargs):
        super(AddEntry, self).__init__(**kwargs)
        # TODO: create method to check if day's tasks have already been entered
        self.added_tasks = False
        self.entry_list = []

    def add_new(self):
        global total_entry_num
        total_entry_num += 1
        new = Entry(name="task " + str(total_entry_num))
        self.children[1].children[0].add_widget(new)

    def submit_tasks(self):
        for child in self.children[1].children[0].children:
            if child.task_text != '':
                self.entry_list.append(child.task_text)

        if len(self.entry_list) < total_entry_num:
            content = Button(text='OK', pos_hint={'top': 1}, size_hint=(0.4, 0.25),
                             background_color=(52, 152, 219, 1), color=(0, 0, 0, 1))
            popup = Popup(title='Please fill all entries.', title_size='20sp', content=content,
                            auto_dismiss=False, size_hint=(0.4, 0.4))
            content.bind(on_press=popup.dismiss)
            popup.open()
        else:
            print ','.join(self.entry_list)
            build_database()
            create_entry(self.entry_list)
            content = Button(text='OK', pos_hint={'top': 1}, size_hint=(0.4, 0.25),
                background_color=(52, 152, 219, 1), color=(0, 0, 0, 1))
            popup = Popup(title='Day entries submitted.', title_size='20sp', content=content,
                auto_dismiss=False, size_hint=(0.4, 0.4))
            content.bind(on_press=popup.dismiss)
            popup.open()



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




