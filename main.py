from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.lang import Builder

from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from kivy.graphics.vertex_instructions import Line

from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

from commission import Commission
from omission import Omission
from archive import Archive
# from archive import Archive

from database.db_function import get_entry, get_entry_mistakes_id, get_mistake_cost
from database.db_model import build_database

Builder.load_file('kv-files/commission.kv')
Builder.load_file('kv-files/omission.kv')
Builder.load_file('kv-files/archive.kv')

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
        self.current_window = None

        # initially load the journal window as main window
        journal_menu = Journal()
        self.add_window("home", journal_menu)
        self.load_window("home")

        omission = Omission()
        self.add_window("omission", omission)

        commission = Commission()
        self.add_window("commission", commission)

        archive = Archive()
        self.add_window("archive", archive)

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
        if key == 'commission':
            self.windows[key].display_mistakes()
            self.current_window = 'commission'
        elif key == 'omission':
            self.windows[key].display_mistakes()
            self.current_window = 'omission'
        elif key == 'home':
            self.windows[key].calculate_day_cost()
            self.current_window = 'home'
        elif key == 'archive':
            self.windows[key].list_entries()
            self.current_window = 'archive'
        self.clear_widgets()
        self.add_widget(self.windows[key])

    def update(self, *args):
        if self.current_window == 'home':
            self.windows['home'].update()

class MenuCanvas(BoxLayout):

    def __init__(self, **kwargs):
        super(MenuCanvas, self).__init__(**kwargs)


class Journal(BoxLayout):

    start_angle = NumericProperty()
    end_angle = NumericProperty()

    def __init__(self, **kwargs):
        super(Journal, self).__init__(**kwargs)
        self.score_canvas = self.ids['menu_canvas'].canvas
        self.start_angle = 250
        self.end_angle = 360
        self.calculate_day_cost()

    def update(self, *args):
        self.start_angle = self.start_angle + 2.5 
        self.end_angle = self.end_angle + 2.5 

    def calculate_day_cost(self):
        todays_eid = get_entry()
        todays_cost = 0

        if todays_eid is not None:
            mistakes_ids = get_entry_mistakes_id(todays_eid)
            for id in mistakes_ids:
                todays_cost += get_mistake_cost(id)

        self.ids['menu_canvas'].children[0].text = '$' + str(todays_cost)


class JournalApp(App):

    def build(self):
        build_database()
        self.journal = JournalInterfaceManager()
        Clock.schedule_interval(self.journal.update, 1/60.)
        return self.journal 

    def load_window(self, key):
        self.journal.load_window(key)

if __name__ == "__main__":

    Window.size = (600, 850)
    LabelBase.register(name='Modern Pictograms', fn_regular='images/modernpics.ttf')
    JournalApp().run()
