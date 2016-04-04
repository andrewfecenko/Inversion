from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.properties import ObjectProperty
from database.db_model import build_database
from database.db_function import *
from math import sin
from kivy.graphics import Mesh, Color, Rectangle
from kivy.garden.graph import Graph, MeshLinePlot, MeshStemPlot, LinePlot, SmoothLinePlot, ContourPlot


class Stats(BoxLayout):

    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)
        cost_max = self.calculate_day_cost()
        self.graph_theme = {
                'label_options': {
                    'color': (0, 0, 0, 1),  # color of tick labels and titles
                    'bold': True},
                'tick_color': (52, 152, 100, 1),  # ticks and grid
                'border_color': (33, 152, 219, 1)}  # border drawn around each graph

        self.graph1 = Graph(
                xlabel='Months',
                ylabel='Costs',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_minor=5,
                x_ticks_major=25,
                y_ticks_major=1,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=12,
                ymin=0,
                ymax=cost_max + 1,
                **self.graph_theme)

        self.graph2 = Graph(
                xlabel='Weeks',
                ylabel='Costs',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_minor=5,
                x_ticks_major=25,
                y_ticks_major=1,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=20,
                ymin=0,
                ymax=cost_max + 1,
                **self.graph_theme)

        self.graph5 = Graph(
                xlabel='Months',
                ylabel='Mistakes',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_minor=5,
                x_ticks_major=25,
                y_ticks_major=1,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=12,
                ymin=0,
                **self.graph_theme)

        self.graph6 = Graph(
                xlabel='Weeks',
                ylabel='Mistakes',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_minor=5,
                x_ticks_major=25,
                y_ticks_major=1,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=49,
                ymin=0,
                **self.graph_theme)

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
        return todays_cost

    def get_monthly_cost(self):
        month_list = get_all_months()
        month_cost = get_monthly_cost()
        points_list = self.make_pairs(month_list, month_cost)
        print(points_list)

        plot = SmoothLinePlot(color=[1, 0, 0, 1])
        plot.points = points_list
        self.graph1.add_plot(plot)
        self.ids['graph1'].remove_widget(self.graph2)
        self.ids['graph1'].add_widget(self.graph1)

    def get_weekly_cost(self):
        week_list = get_all_weeks()
        week_cost = get_weekly_cost()
        points_list = self.make_pairs(week_list, week_cost)
        print(points_list)

        plot = SmoothLinePlot(color=[1, 0, 0, 1])
        plot.points = points_list
        self.graph2.add_plot(plot)
        self.ids['graph1'].remove_widget(self.graph1)
        self.ids['graph1'].add_widget(self.graph2)

    def get_om_cates(self):
        all_om_verbs = get_all_verbs(True)

        for x in range(len(all_om_verbs)):
            print(all_om_verbs[x])
            label_om = Label(text=all_om_verbs[x])
            self.ids['graph3'].add_widget(label_om)

        y_list = get_verb_graph(True)


        # self.ids['graph3'].remove_widget(self.graph6)



    def get_monthly_mistakes(self):
        month_list = get_all_months()
        month_mistakes = get_monthly_mistake_num()
        points_list = self.make_pairs(month_list, month_mistakes)
        print(points_list)

        plot = SmoothLinePlot(color=[1, 0, 0, 1])
        plot.points = points_list
        self.graph5.add_plot(plot)
        self.ids['graph3'].remove_widget(self.graph6)
        self.ids['graph3'].add_widget(self.graph5)

    def get_weekly_mistakes(self):
        week_list = get_all_weeks()
        week_mistakes = get_weekly_mistake_num()
        points_list = self.make_pairs(week_list, week_mistakes)
        print(points_list)

        plot = SmoothLinePlot(color=[1, 0, 0, 1])
        plot.points = points_list
        self.graph6.add_plot(plot)
        self.ids['graph3'].remove_widget(self.graph5)
        self.ids['graph3'].add_widget(self.graph6)