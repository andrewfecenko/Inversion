from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.properties import ObjectProperty
from database.db_model import build_database
from database.db_function import *


from math import sin
from kivy.garden.graph import Graph, MeshLinePlot


class Stats(BoxLayout):

    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)
        self.calculate_day_cost()

        # would allow you to modify the xmax proprty
        #self.ids['graph'].xmax = 100

        month_list = get_all_months()
        month_cost = get_monthly_cost()
        # print("days:" + str(day_list))
        # print("daily cost:" + str(day_cost))
        points_list = self.make_pairs(month_list, month_cost)
        print(points_list)

        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = points_list
        self.ids['graph'].add_plot(plot)



    def make_pairs(self, list1, list2):
        points = []
        for (month,cost) in zip(list1, list2):
            points.append((month, cost))
        return points

    def calculate_day_cost(self):
        todays_eid = get_entry()
        todays_cost = 0

        if todays_eid is not None:
            mistakes_ids = get_entry_mistakes_id(todays_eid)
            for id in mistakes_ids:
                todays_cost += get_mistake_cost(id)

        self.ids['opportunity_cost'].text = "Total cost: $" + str(todays_cost)
