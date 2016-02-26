from kivy.app import App
from kivy.app import Widget

class Journal(Widget):
    pass

class JournalApp(App):
    
    def build(self):
        journal = Journal()
        return journal
 
if __name__ == "__main__":
    JournalApp().run()
