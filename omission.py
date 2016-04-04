from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from database.db_function import *
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class OmCustomDropDown(BoxLayout):
    def __init__(self, **kwargs):
        super(OmCustomDropDown, self).__init__(**kwargs)


class OmMistake(GridLayout):
    def __init__(self,mid, **kwargs):
        super(OmMistake, self).__init__(**kwargs)
        self.mid = mid

    def remove_mistake(self):
        omission.remove_mistake(self.mid)


class Omission(BoxLayout):
    def __init__(self, **kwargs):
        super(Omission, self).__init__(**kwargs)

        global omission
        omission = self

        self.display_mistakes()

    # Click on the plus button to complete the form
    # Change the button to the minus button
    def submit_form(self):
        # Insert inputs to DB

        if (not self.ids.cost.text) or (not self.ids.noun.text) or (not self.ids.verb.text):
            popup = Popup(title='Input Error',
                content=Label(text='Please enter all fieds'),
                size_hint=(None, None), size=(350, 350))

            popup.open()

        elif not (self.ids.cost.text.isdigit()):
            popup = Popup(title='Input Error',
                content=Label(text='Please enter an interger for cost'),
                size_hint=(None, None), size=(350, 350))

            self.ids.cost.text = ''

            popup.open()

        else:
            verb = self.ids.verb.text
            noun = self.ids.noun.text
            cost = self.ids.cost.text
            create_mistake(self.eid, True, verb, noun, cost)

            # Clear input field
            self.ids.verb.text = "Didn't do"
            self.ids.noun.text = ''
            self.ids.cost.text = ''

            self.display_mistakes()

    def display_mistakes(self):
        # Create/get an entry id for the day
        self.eid = get_entry()
        if self.eid is None:
            self.eid = create_entry()

        # Get a list of mistakes for today
        self.ids.mistakes.clear_widgets()
        mids = get_entry_mistakes_id(self.eid)

        for mid in mids:
            m = get_mistake(mid)
            if m.is_om is True:
                mistake = OmMistake(mid)
                mistake.ids.verb.text = m.verb
                mistake.ids.noun.text = m.noun
                mistake.ids.cost.text = str(m.cost)
                self.ids.mistakes.add_widget(mistake)

    def remove_mistake(self, mid):
        delete_mistake(mid)
        self.display_mistakes()
