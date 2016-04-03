from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.properties import ObjectProperty
from database.db_function import get_all_entries
from database.db_function import get_entry_mistakes_id
from database.db_function import get_mistake_noun


class Archive(BoxLayout):

    def __init__(self, **kwargs):
        super(Archive, self).__init__(**kwargs)
        self.list_entries()

    def list_entries(self):
        all_entries = get_all_entries()

        if all_entries is None:
            self.list_empty_archive()
            return

        for ind, entry in enumerate(all_entries):
            if ind == 3:
                break

            mistakes_id = get_entry_mistakes_id(entry)
            if mistakes_id is None:
                continue

            # go through all mistakes for the day
            for id in mistakes_id:
                mistake_noun = get_mistake_noun(id)
                print(mistake_noun)
                label = Label(text=mistake_noun, font_size=20,
                    halign='center', color=(0, 1, 0), size_hint=(1, 0.25))
                self.ids['mistake_scroll'].add_widget(label)

    def list_empty_archive(self):
        label = Label(text='You don\'t  have any mistakes!', font_size=40,
            halign='center')
        self.ids['mistake_scroll'].add_widget(label)
