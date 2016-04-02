from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from db_function import get_days_entry
from db_function import get_entry_failure_points
from datetime import datetime, timedelta


class ReviewMistakes(BoxLayout):

    def __init__(self, **kwargs):

        super(ReviewMistakes, self).__init__(**kwargs)
        yesterday = datetime.today() - timedelta(days=1)
        yesterdays_entry = get_days_entry(givenday=yesterday)
        self.yesterdays_mistakes = get_entry_failure_points(yesterdays_entry)[0]
        print(self.yesterdays_mistakes) 
        self.generate_label_widgets()
        self.display_mistakes()

    def generate_label_widgets(self):
        if self.yesterdays_mistakes is None:
            return

        for label in self.yesterdays_mistakes:
            curr_label = Label()
            self.children[1].add_widget(curr_label)

    def display_mistakes(self):
        if self.yesterdays_mistakes is None:
            return

        for ind, mistake in enumerate(self.yesterdays_mistakes):
            self.children[1].children[ind].text = mistake
