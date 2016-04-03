from kivy.uix.boxlayout import BoxLayout
from database.db_function import *
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class CustomDropDown(BoxLayout):
    def __init__(self, **kwargs):
        super(CustomDropDown, self).__init__(**kwargs)
        self.refs = [self.dropdown.__self__,
                     self.ratebutton.__self__,
                     self.instructions.__self__,
                     self.leaderboard.__self__]

class Mistake(BoxLayout):
    def __init__(self,mid, **kwargs):
        super(Mistake, self).__init__(**kwargs)
        self.mid = mid

    def remove_form(self):
        commission.remove_mistake(self.mid)


class Commission(BoxLayout):
    def __init__(self, **kwargs):
        super(Commission, self).__init__(**kwargs)

        global commission
        commission = self

        self.display_mistakes()

    # Click on the plus button to complete the form
    # Change the button to the minus button
    def submit_form(self):
        # Insert inputs to DB

        if not (self.ids.cost.text) or not (self.ids.noun.text):
            popup = Popup(title='Input Error',
                content=Label(text='Please enter all fieds'),
                size_hint=(None, None), size=(350, 350))
            popup.open()

            # Clear input field
            self.ids.verb.text = ''
            self.ids.noun.text = ''
            self.ids.cost.text = ''


        elif not (self.ids.cost.text.isdigit()):
            popup = Popup(title='Input Error',
                content=Label(text='Please enter an interger for cost'),
                size_hint=(None, None), size=(350, 350))

            popup.open()

            # Clear input field
            self.ids.verb.text = ''
            self.ids.noun.text = ''
            self.ids.cost.text = ''


        else:
            verb = self.ids.verb.text
            noun = self.ids.noun.text
            cost = self.ids.cost.text

            create_mistake(self.eid, False, verb, noun, cost)

            # Clear input field
            self.ids.verb.text = ''
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
        mistakes = []
        for mid in mids:
            m = get_mistake(mid)
            if not m.is_om:
                mistake = Mistake(mid)
                mistake.ids.verb.text = m.verb
                mistake.ids.noun.text = m.noun
                mistake.ids.cost.text = str(m.cost)
                self.ids.mistakes.add_widget(mistake)

    def remove_mistake(self, mid):
        delete_mistake(mid)
        self.display_mistakes()
