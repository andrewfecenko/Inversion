from kivy.uix.boxlayout import BoxLayout

from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

class CustomDropDown(BoxLayout):
    pass


class Form(BoxLayout):
    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)

    # Click on the plus button to complete the form
    # Change the button to the minus button
    def finish_form(self):
        self.ids.submit.text = ('[font=Modern Pictograms][size=30]'
            'X[/size][/font]')
        self.ids.submit.background_color = get_color_from_hex('#B5B5B5')
        commission.add_form()

    # Click on the minus button to delete the form
    # Remove this form from the page
    def delete_form(self):
        commission.remove_form()

class Commission(BoxLayout):
    def __init__(self, **kwargs):
        super(Commission, self).__init__(**kwargs)

        global commission
        commission = self
        self.add_form()

    def add_form(self):
        form = Form()
        self.ids.forms.add_widget(form)

    def remove_form(self, form):
        self.ids.forms.clear_widget(form)

