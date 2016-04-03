from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.lang import Builder

from kivy.properties import BooleanProperty
from kivy.properties import StringProperty

from commission import Commission
from omission import Omission

from database.db_function import get_entry, get_entry_mistakes_id, get_mistake_cost

Builder.load_file('kv-files/commission.kv')
Builder.load_file('kv-files/omission.kv')

# from add_entry import AddEntry
# from update_entry import UpdateEntry
# from review_mistakes import ReviewMistakes
# from settings import Settings
# from collect import Collection
# from favorites import Favorites

# load separate kv for later reference
# Builder.load_file('kv-files/add_entry.kv')
# Builder.load_file('kv-files/update_entry.kv')
# Builder.load_file('kv-files/review_mistakes.kv')
# Builder.load_file('kv-files/settings.kv')
# Builder.load_file('kv-files/collection.kv')
# Builder.load_file('kv-files/favorites.kv')


class JournalInterfaceManager(BoxLayout):

    def __init__(self, **kwargs):

        super(JournalInterfaceManager, self).__init__(**kwargs)
        self.windows = {}

        # initially load the journal window as main window
        journal_menu = Journal()
        self.add_window("home", journal_menu)
        self.load_window("home")

        omission = Omission()
        self.add_window("omission", omission)

        commission = Commission()
        self.add_window("commission", commission)

        # # add remaining windows to tracked windows
        # enter_tasks = AddEntry()
        # self.add_window("enter_tasks", enter_tasks)
        #
        # update_entry = UpdateEntry()
        # self.add_window("update_entry", update_entry)
        #
        # review_mistakes = ReviewMistakes()
        # self.add_window("review_mistakes", review_mistakes)
        #
        # settings = Settings()
        # self.add_window("settings", settings)
        #
        # collections = Collection()
        # self.add_window("collections", collections)
        #
        # favourites = Favorites()
        # self.add_window("favorites",favourites)

    def add_window(self, key, window):
        self.windows[key] = window

    def load_window(self, key):
        self.clear_widgets()
        self.add_widget(self.windows[key])


class Journal(BoxLayout):

    def __init__(self, **kwargs):
        super(Journal, self).__init__(**kwargs)
        self.calculate_day_cost()

    def calculate_day_cost(self):
        todays_eid = get_entry()
        todays_cost = 0

        if todays_eid is not None:
            mistakes_ids = get_entry_mistakes_id(todays_eid)
            for id in mistakes_id:
                todays_cost += get_mistake_cost(id)

        self.ids['opportunity_cost'].text = str(todays_cost)


class JournalApp(App):

    def build(self):
        self.journal = JournalInterfaceManager()
        return self.journal

    def load_window(self, key):
        self.journal.load_window(key)

if __name__ == "__main__":

    Window.size = (600, 850)
    LabelBase.register(name='Modern Pictograms', fn_regular='images/modernpics.ttf')
    JournalApp().run()
