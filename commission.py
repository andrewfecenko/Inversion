from kivy.uix.boxlayout import BoxLayout

from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from database.db_function import *


class CustomDropDown(BoxLayout):
    pass


class Mistake(BoxLayout):
    pass


class Commission(BoxLayout):
    def __init__(self, **kwargs):
        super(Commission, self).__init__(**kwargs)

        # Create/get an entry id for the day
        self.eid = get_entry()
        if self.eid == None:
            self.eid = create_entry()

        self.commission = self
        self.display_mistakes()

    # Click on the plus button to complete the form
    # Change the button to the minus button
    def finish_form(self):
        noun = self.ids.noun.text
        cost = self.ids.cost.text
        create_mistake(self.eid, True, noun, cost)
        self.display_mistakes()

    def display_mistakes(self):
        # Get a list of mistakes for today
        self.ids.mistakes.clear_widgets()
        mids = get_mistakes_category_id(self.eid, False)
        mistakes = []
        for mid in mids:
            mistakes.append(get_mistake(mid))
        for each in mistakes:
            mistake = Mistake()
            mistake.ids.noun.text = each.noun
            mistake.ids.cost.text = each.cost
            self.ids.mistakes.add_widget(mistake)

