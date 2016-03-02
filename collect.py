from kivy.uix.boxlayout import BoxLayout

class Collection(BoxLayout):

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
        return result

    def build(self):
	self.load_kv('collection.kv')
