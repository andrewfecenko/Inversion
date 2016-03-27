from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

#from db_function import *


class Collection(BoxLayout):

# TODO:
# connect with db
# Fix sizing problem
# Make it ~beautiful~

    def __init__(self, **kwargs):
        super(Collection, self).__init__(**kwargs)
        
        #Placeholder
        self.entry_list = ["0227", "0228", "0229"]
        
        self.scrollview = ScrollView(size_hint=(None, None), size=(700, 400),
            pos_hint={'center_x':.5, 'center_y':.5}, id="1")
        
        self.gridlayout = self.generate_entry_buttons(self.entry_list)

        self.scrollview.add_widget(self.gridlayout)
        self.add_widget(self.scrollview)

        #Back button
        btn_back = Button(size_hint=(1, None))
        btn_back.text = "Back"
        self.add_widget(btn_back)


    def generate_entry_buttons(self, entry_list):
        
        gridlayout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        gridlayout.bind(minimum_height=gridlayout.setter('height'))

        #Generate a button for each entry
        for i in range(0, len(self.entry_list)):
            btn = Button(size_hint=(1, None))
            btn.text = self.entry_list[i]
            gridlayout.add_widget(btn)
            
        return gridlayout

        
    def search_entry(self, text):
        
        result = ""
        if text != "":
            result = "No entry for this date."
            for i in range(0, len(self.entry_list)):
                if self.entry_list[i] == text:
                    result = self.entry_list[i]
                    break
                    
            btn = Button(size_hint=(1, None))
            btn.text = result

            self.gridlayout.clear_widgets()
            self.gridlayout.add_widget(btn)
        return result


    def build(self):
	self.load_kv('collection.kv')
