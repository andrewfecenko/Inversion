from kivy.uix.boxlayout import BoxLayout
from database.db_function import *

from math import sin
from kivy.garden.graph import Graph, MeshLinePlot


class Stats(BoxLayout):

    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)
        self.calculate_day_cost()

        plot = MeshLinePlot(color=[1, 0, 0, 1])
    
        week_costs = get_daily_mistake_num()
        plot.points = []
        for x, cost in enumerate(week_costs):
            print(cost)
            plot.points.append((x+1, cost))


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
