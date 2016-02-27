from kivy.app import App
from kivy.app import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.text import LabelBase

class Journal(GridLayout):
	pass

class JournalApp(App):

	def build(self):
		journal = Journal()
		return journal


if __name__ == "__main__":
    Config.set('graphics', 'width', '600')
    Config.set('graphics', 'height', '600')

    LabelBase.register(name='Modern Pictograms', fn_regular = 'modernpics.ttf')
    JournalApp().run()
