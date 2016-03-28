from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

#from main import Journal
from update_entry import UpdateEntry
from functools import partial
#from db_function import *


class Collection(BoxLayout):

# TODO:
# Connect with db
# Give buttons actions (change window)
# Fix sizing problem and color
# Be consistent with other windows

    def __init__(self, **kwargs):
        super(Collection, self).__init__(**kwargs)
        
        #Placeholder
        self.entry_list = ["0227", "0228", "0229"]
        
        self.scrollview = ScrollView(size_hint=(None, None), size=(700, 400),
            pos_hint={'center_x':.5, 'center_y':.5})
        
        self.gridlayout = self.generate_entry_buttons(self.entry_list)

        self.scrollview.add_widget(self.gridlayout)
        self.add_widget(self.scrollview)

        #Back button
#        btn_back = Button(text='Back', size_hint=(1, None))
#        btn_back.background_color = (0.502, 0.502, 0.502, 1)
##        btn_back.bind(on_press=partial(self.change_window, "Journal()"))
#        self.add_widget(btn_back)


    def generate_entry_buttons(self, entry_list):
        
        gridlayout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        gridlayout.bind(minimum_height=gridlayout.setter('height'))

        #Generate a button for each entry
        for i in range(0, len(self.entry_list)):
            btn = Button(size_hint=(1, None))
            btn.text = self.entry_list[i]
            btn.background_color = (0.278, 0.706, 0.459, 1)
#            btn.bind(on_press=partial(self.change_window, "UpdateEntry()"))
            gridlayout.add_widget(btn)
            
        return gridlayout


#    def change_window(self, *args):
#        window = args[1]
#        self.clear_widgets()
#        self.add_widget(window)

        
    def search_entry(self, text):
        
        result = ""
        found = False
        if text != "":
            result = "No entry for this date."
            for i in range(0, len(self.entry_list)):
                if self.entry_list[i] == text:
                    result = self.entry_list[i]
                    found = True
                    break
                
            if found:            
                btn = Button(size_hint=(1, None))
                btn.text = result
                btn.background_color = (0.278, 0.706, 0.459, 1)
                self.gridlayout.clear_widgets()
                self.gridlayout.add_widget(btn)

            else: #generate label instead
                label = Label(text=result)
                self.gridlayout.clear_widgets()
                self.gridlayout.add_widget(label)

        else: #i.e. search bar empty/cleared
            self.gridlayout = self.generate_entry_buttons(self.entry_list)
            self.scrollview.clear_widgets()
            self.scrollview.add_widget(self.gridlayout)
            
        return result


    def build(self):
	self.load_kv('collection.kv')
