from kivy.uix.boxlayout import BoxLayout
from database.db_function import get_all_entries


class Archive(BoxLayout):

    def __init__(self, **kwargs):
        super(Archive, self).__init__(**kwargs)

    def list_entries(self):
        all_entries = get_all_entries()
        if all_entries is None:
            self.list_empty_archive()
            return

        for ind, entry in enumerate(all_entries):
            if ind == 5:
                break

            print(self.ids['mistake_scroll'])



    def list_empty_archive(self):
        pass
         
