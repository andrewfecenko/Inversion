from kivy.uix.boxlayout import BoxLayout
from database.db_function import *


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
