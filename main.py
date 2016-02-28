from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.lang import Builder

from kivy.properties import BooleanProperty
from kivy.properties import StringProperty

from add_entry import AddEntry
from update_entry import UpdateEntry
from review_mistakes import ReviewMistakes

# load separate kv for later reference
Builder.load_file('kv-files/add_entry.kv')
Builder.load_file('kv-files/update_entry.kv')
Builder.load_file('kv-files/review_mistakes.kv')

class JournalInterfaceManager(BoxLayout):

    def __init__(self, **kwargs):
        super(JournalInterfaceManager, self).__init__(**kwargs)
        self.windows = {}

        # initially load the journal window as main window
        journal_menu = Journal()
        self.add_window("journal_menu", journal_menu)
        self.load_window("journal_menu")

        # add remaining windows to tracked windows
        enter_tasks = AddEntry()
        self.add_window("enter_tasks", enter_tasks)

        update_entry = UpdateEntry()
        self.add_window("update_entry", update_entry)

        review_mistakes = ReviewMistakes()
        self.add_window("review_mistakes", review_mistakes)

    def add_window(self, key, window):
        self.windows[key] = window

    def load_window(self, key):
        self.clear_widgets()
        self.add_widget(self.windows[key])


class Journal(GridLayout):

    locked = BooleanProperty()
    locked_text = StringProperty()

    def __init__(self, **kwargs):
        super(Journal, self).__init__(**kwargs)
        self.locked = False
        self.locked_text = '[font=Modern Pictograms][size=80]n[/size][/font]\nLock'

    def unlock_lock(self):

        if self.locked:
            # TODO: make sure that password is required to unlock
            box = BoxLayout()
            box.add_widget(Label(text='Hello world'))
            box.add_widget(TextInput(text='Hi'))

            popup = Popup(title='Test popup', content=box, size_hint=(None, None), size=(400, 400))
            popup.open()

            for section in self.ids:
                if section != 'lock':
                    self.ids[section].disabled = False
            self.locked_text = '[font=Modern Pictograms][size=80]q[/size][/font]\nLock'
            self.locked = False

        else:

            for section in self.ids:
                if section != 'lock':
                    self.ids[section].disabled = True
            self.locked_text = '[font=Modern Pictograms][size=80]n[/size][/font]\nUnlock'
            self.locked = True



class LockPopup(Popup):

    def __init__(self, **kwargs):
        super(LockPopup, self).__init__(**kwargs)
        self.title = "Test popup"

        box = BoxLayout()
        box.add_widget(Label(text='Hello world'))
        box.add_widget(TextInput(text='Hi'))

        self.content = box
        self.size_hint = None, None
        self.size = 400, 200

    def on_dismiss(self):
        pass


class JournalApp(App):

    def build(self):
        self.journal = JournalInterfaceManager()
        return self.journal

    def load_window(self, key):
        self.journal.load_window(key)

if __name__ == "__main__":
    Config.set('graphics', 'width', '600')
    Config.set('graphics', 'height', '600')

    LabelBase.register(name='Modern Pictograms', fn_regular='images/modernpics.ttf')
    JournalApp().run()
