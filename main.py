from kivy.app import App
from kivy.app import Widget
from kivy.uix.gridlayout import GridLayout

from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.core.text import LabelBase


class Journal(GridLayout):

    locked = BooleanProperty()
    locked_text = StringProperty()

    def __init__(self, **kwargs):
        super(Journal, self).__init__(**kwargs)
        self.locked = True
        self.locked_text = '[font=Modern Pictograms][size=80]n[/size][/font]\nLock'

    def unlock_lock(self):

        if self.locked:
            # TODO: make sure that password is required to unlock
            self.locked_text = '[font=Modern Pictograms][size=80]q[/size][/font]\nLock'
            self.locked = False
        else:
            self.locked_text = '[font=Modern Pictograms][size=80]n[/size][/font]\nUnlock'
            self.locked = True


class JournalApp(App):

    def build(self):
        journal = Journal()
        return journal


if __name__ == "__main__":
    Config.set('graphics', 'width', '600')
    Config.set('graphics', 'height', '600')

    LabelBase.register(name='Modern Pictograms', fn_regular='modernpics.ttf')
    JournalApp().run()
