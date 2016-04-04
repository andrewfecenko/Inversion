from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from database.db_function import *
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class ComCustomDropDown(BoxLayout):
    def __init__(self, **kwargs):
        super(ComCustomDropDown, self).__init__(**kwargs)


class ComMistake(GridLayout):
    def __init__(self, mid, commission, **kwargs):
        super(ComMistake, self).__init__(**kwargs)
        self.mid = mid
        self.commission = commission

    def remove_mistake(self):
        self.commission.remove_mistake(self.mid)

    def update_noun(self, new_noun):
        if new_noun == '':
            return
        else:
            update_mistake_noun(self.mid, new_noun)
            self.commission.display_mistakes()

    def update_cost(self, new_cost):
        if new_cost == '' or not new_cost.isdigit():
            return
        else:
            update_mistake_cost(self.mid, new_cost)
            self.commission.display_mistakes()

    def edit_noun(self):
        verb = self.ids.verb
        cost = self.ids.cost
        btn = self.ids.rm
        default = self.ids.noun.text
        self.clear_widgets()
        self.add_widget(verb)
        self.add_widget(EditForm(default, self, 'noun', size_hint=(0.35, 1)))
        self.add_widget(cost)
        self.add_widget(btn)

    def edit_cost(self):
        verb = self.ids.verb
        noun = self.ids.noun
        btn = self.ids.rm
        default = self.ids.cost.text
        self.clear_widgets()
        self.add_widget(verb)
        self.add_widget(noun)
        self.add_widget(EditForm(default, self, 'cost', size_hint=(0.2, 1)))
        self.add_widget(btn)


class EditForm(TextInput):
    def __init__(self, default, mistake, type, **kwargs):
        super(EditForm, self).__init__(**kwargs)
        self.text = default
        self.focus = True
        self.mistake = mistake
        self.type = type

    def update_mistake(self):
        if self.type == 'noun':
            self.mistake.update_noun(self.text)
        elif self.type == 'cost':
            self.mistake.update_cost(self.text)


class ComOption(Button):
    def __init__(self, opt, **kwargs):
        super(ComOption, self).__init__(**kwargs)

        self.text = opt


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

        if (not self.ids.cost.text) or (not self.ids.noun.text) or (not self.ids.verb.text):
            popup = Popup(title='Input Error',
                content=Label(text='Please enter all fields'),
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
            create_mistake(self.eid, False, verb, noun, cost)

            # Clear input field
            self.ids.verb.text = "Did"
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
        mids.reverse()

        for mid in mids:
            m = get_mistake(mid)
            if m.is_om is False:
                mistake = ComMistake(mid, self)
                mistake.ids.verb.text = m.verb
                mistake.ids.noun.text = m.noun
                mistake.ids.cost.text = str(m.cost)
                self.ids.mistakes.add_widget(mistake)

        self.display_verbs()

    def display_verbs(self):
        dropdown = DropDown()
        verbs = get_all_verbs(False)

        for verb in verbs:
            new_option = ComOption(verb)
            new_option.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(new_option)

        mainbutton = self.ids.verb
        mainbutton.text = 'Did'
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

    def remove_mistake(self, mid):
        delete_mistake(mid)
        self.display_mistakes()

    def add_verb(self):
        verb = self.ids.new_verb.text
        if verb == '':
            popup = Popup(title='Input Error',
                content=Label(text="Empty input"),
                size_hint=(None, None), size=(350, 350))
            popup.open()
            return

        # Empty noun to insert verb to DB
        create_mistake(self.eid, False, verb, '', 0)
        self.ids.new_verb.text = ''
        self.display_verbs()