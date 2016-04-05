from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
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
                    'color': (255, 204, 204, 1),  # color of tick labels and titles
                    'bold': True},
                'tick_color': (52, 152, 100, 1),  # ticks and grid
                'border_color': (255, 204, 204, 1)}  # border drawn around each graph

        # Monthly cost graph
        self.graph1 = Graph(
                xlabel='Months',
                ylabel='Costs',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_major=5,
                y_ticks_major=10,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=12,
                ymin=0,
                ymax=200,
                **self.graph_theme)

        # Weekly cost graph
        self.graph2 = Graph(
                xlabel='Weeks',
                ylabel='Costs',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_major=5,
                y_ticks_major=10,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=20,
                ymin=0,
                ymax=100,
                **self.graph_theme)

        # Daily cost graph
        self.graph8 = Graph(
                xlabel='Days',
                ylabel='Costs',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_major=5,
                y_ticks_major=10,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=365,
                ymin=0,
                ymax=50,
                **self.graph_theme)

        # Monthly mistakes graph
        self.graph5 = Graph(
                xlabel='Months',
                ylabel='Mistakes',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_major=5,
                y_ticks_major=10,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=12,
                ymin=0,
                ymax=20,
                **self.graph_theme)

        # Weekly mistakes graph
        self.graph6 = Graph(
                xlabel='Weeks',
                ylabel='Mistakes',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_major=5,
                y_ticks_major=10,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=49,
                ymin=0,
                ymax=10,
                **self.graph_theme)

        # Daily mistakes graph
        self.graph7 = Graph(
                xlabel='Days',
                ylabel='Mistakes',
                size_hint=(0.7, 0.9),
                pos_hint={'center_x': .5, 'center_y': 0.5},
                x_ticks_major=5,
                y_ticks_major=10,
                y_grid_label=True,
                x_grid_label=True,
                padding=5,
                xmin=0,
                xmax=365,
                ymin=0,
                ymax=5,
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

    def get_daily_cost(self):
        day_list = days_to_ints(get_all_days())
        my_day_list = {}

        for (m, d) in day_list:
            if m in my_day_list:
                my_day_list[m].append(d)
            else:
                my_day_list[m] = []
                my_day_list[m].append(d)

        new_day_list = []

        for eachMonth in my_day_list:
            for eachDay in my_day_list[eachMonth]:
                new_day_list.append(eachDay + (eachMonth - 1) * 30)

        day_cost = get_daily_cost()

        points_list = self.make_pairs(new_day_list, day_cost)
        print(points_list)

        plot = SmoothLinePlot(color=[1, 0, 0, 1])
        plot.points = points_list

        self.graph8.add_plot(plot)

        self.ids['graph1'].remove_widget(self.graph2)
        self.ids['graph1'].remove_widget(self.graph1)
        self.ids['graph1'].add_widget(self.graph8)

    def get_monthly_cost(self):
        month_list = get_all_months()
        month_cost = get_monthly_cost()
        points_list = self.make_pairs(month_list, month_cost)
        print(points_list)

        plot = SmoothLinePlot(color=[1, 0, 0, 1])
        plot.points = points_list
        self.graph1.add_plot(plot)
        self.ids['graph1'].remove_widget(self.graph8)
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
        self.ids['graph1'].remove_widget(self.graph8)
        self.ids['graph1'].remove_widget(self.graph1)
        self.ids['graph1'].add_widget(self.graph2)

    def get_om_cates(self):
        all_om_verbs = get_all_verbs(True)
        self.ids['graph2'].clear_widgets()

        scroll = ScrollView()
        grid = GridLayout(id='grid', size_hint_y=None, cols=1, row_default_height='30dp', row_force_default=True, spacing=20, padding=20)
        grid.bind(minimum_height=grid.setter('height'))
        scroll.add_widget(grid)
        self.ids['graph2'].add_widget(scroll)

        for (name, times) in zip(all_om_verbs, get_verb_graph(True)):
            label_om = CateEntry(name=name, times=str(times))
            # print(name)
            # print(times)
            grid.add_widget(label_om)

    def get_cm_cates(self):
        all_cm_verbs = get_all_verbs(False)
        self.ids['graph2'].clear_widgets()

        scroll = ScrollView()
        grid = GridLayout(id='grid', size_hint_y=None, cols=1, row_default_height='30dp', row_force_default=True, spacing=20, padding=20)
        grid.bind(minimum_height=grid.setter('height'))
        scroll.add_widget(grid)
        self.ids['graph2'].add_widget(scroll)

        for (name, times) in zip(all_cm_verbs, get_verb_graph(False)):
            label_om = CateEntry(name=name, times=str(times))
            # print(name)
            # print(times)
            grid.add_widget(label_om)

    def get_daily_mistakes(self):
        day_list = days_to_ints(get_all_days())
        my_day_list = {}

        for (m, d) in day_list:
            if m in my_day_list:
                my_day_list[m].append(d)
            else:
                my_day_list[m] = []
                my_day_list[m].append(d)

        new_day_list = []

        for eachMonth in my_day_list:
            for eachDay in my_day_list[eachMonth]:
                new_day_list.append(eachDay + (eachMonth - 1) * 30)

        day_om_cost = get_daily_mistake_tuple()[0]
        day_cm_cost = get_daily_mistake_tuple()[1]
        points_om_list = self.make_pairs(new_day_list, day_om_cost)
        points_cm_list = self.make_pairs(new_day_list, day_cm_cost)
        plot_om = SmoothLinePlot(color=[0, 1, 1, 1])
        plot_om.points = points_om_list
        plot_cm = SmoothLinePlot(color=[1, 0, 0, 1])
        plot_cm.points = points_cm_list

        # print("om:" + str(points_om_list)) #Blue
        # print("cm:" + str(points_cm_list)) # Red

        self.graph7.add_plot(plot_om)
        self.graph7.add_plot(plot_cm)
        self.ids['graph3'].remove_widget(self.graph5)
        self.ids['graph3'].remove_widget(self.graph6)
        self.ids['graph3'].add_widget(self.graph7)

    def get_monthly_mistakes(self):
        month_list = get_all_months()

        month_om_cost = get_monthly_mistake_tuple()[0]
        month_cm_cost = get_monthly_mistake_tuple()[1]
        points_om_list = self.make_pairs(month_list, month_om_cost)
        points_cm_list = self.make_pairs(month_list, month_cm_cost)
        plot_om = SmoothLinePlot(color=[0, 1, 1, 1])
        plot_om.points = points_om_list
        plot_cm = SmoothLinePlot(color=[1, 0, 0, 1])
        plot_cm.points = points_cm_list

        # print("om:" + str(points_om_list)) #Blue
        # print("cm:" + str(points_cm_list)) # Red

        # month_mistakes = get_monthly_mistake_num()
        # points_list = self.make_pairs(month_list, month_mistakes)
        # print(points_list)

        plot = SmoothLinePlot(color=[1, 0, 0, 1])
        self.graph5.add_plot(plot_om)
        self.graph5.add_plot(plot_cm)
        self.ids['graph3'].remove_widget(self.graph7)
        self.ids['graph3'].remove_widget(self.graph6)
        self.ids['graph3'].add_widget(self.graph5)

    def get_weekly_mistakes(self):
        week_list = get_all_weeks()

        week_om_cost = get_monthly_mistake_tuple()[0]
        week_cm_cost = get_monthly_mistake_tuple()[1]
        points_om_list = self.make_pairs(week_list, week_om_cost)
        points_cm_list = self.make_pairs(week_list, week_cm_cost)
        plot_om = SmoothLinePlot(color=[0, 1, 1, 1])
        plot_om.points = points_om_list
        plot_cm = SmoothLinePlot(color=[1, 0, 0, 1])
        plot_cm.points = points_cm_list

        # print("om:" + str(points_om_list)) #Blue
        # print("cm:" + str(points_cm_list)) # Red

        # week_mistakes = get_weekly_mistake_num()
        # points_list = self.make_pairs(week_list, week_mistakes)
        # print(points_list)

        plot = SmoothLinePlot(color=[1, 0, 0, 1])
        self.graph6.add_plot(plot_om)
        self.graph6.add_plot(plot_cm)
        self.ids['graph3'].remove_widget(self.graph7)
        self.ids['graph3'].remove_widget(self.graph5)
        self.ids['graph3'].add_widget(self.graph6)


class CateEntry(BoxLayout):
    name = StringProperty('')
    times = StringProperty()
