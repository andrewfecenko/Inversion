from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label



class Collection(BoxLayout):


    def __init__(self, **kwargs):
        super(Collection, self).__init__(**kwargs)


    def search_entry(self, text):
        #Placeholder
        entry_list = ["0227", "0228", "0229"]
        result = "No entry for this date"
        for i in range(0, len(entry_list)):
            if entry_list[i] == text:
                result = entry_list[i]
                self.add_widget(Label(text=result))
                # return Label(text=text)
   #     self.search_result.item_strings = result
        #print("Searching entry '{}'".format(self.search_input.text))

