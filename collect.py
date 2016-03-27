from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# from kivy.core.window import Window
# Window.clearcolor = 24,24,24,1

#from db_function import *

class Collection(BoxLayout):

# TODO:
# retrieve entries from db
# Generate exactly 1 button for each entry
# Make it work with scroll
# Fix sizing problem


    def __init__(self, **kwargs):
        super(Collection, self).__init__(**kwargs)

    def search_entry(self, text):
        #Placeholder
        entry_list = ["0227", "0228", "0229"]
        result = ""
        if text != "":
            result = "No entry for this date."
            for i in range(0, len(entry_list)):
                if entry_list[i] == text:
                    result = entry_list[i]
                    btn = Button(size_hint=(1, None))
                    btn.text = result
                    self.add_widget(btn)
        return result

    def generate_buttons(self):
        #Placeholder
        entry_list = ["0227", "0228", "0229"]
        for entry in range(0, len(entry_list)):
            btn = Button(size_hint=(1, None))
            btn.text = entry
            grid.add_widget(btn)

    def build(self):
	self.load_kv('collection.kv')
