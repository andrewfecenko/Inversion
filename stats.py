from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.properties import ObjectProperty
from database.db_function import get_entry, get_entry_mistakes_id, get_mistake_cost
from database.db_model import build_database
from database.db_function import get_all_entries_id
from database.db_function import get_entry_mistakes_id
from database.db_function import get_mistake_noun

from math import sin
from kivy.garden.graph import Graph, MeshLinePlot


class Stats(BoxLayout):

    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)
        self.calculate_day_cost()

        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]

        # would allow you to modify the xmax proprty
        #self.ids['graph'].xmax = 100
        self.ids['graph'].add_plot(plot)


    def calculate_day_cost(self):
        todays_eid = get_entry()
        todays_cost = 0

        if todays_eid is not None:
            mistakes_ids = get_entry_mistakes_id(todays_eid)
            for id in mistakes_ids:
                todays_cost += get_mistake_cost(id)

        self.ids['opportunity_cost'].text = "Total cost: $" + str(todays_cost)
