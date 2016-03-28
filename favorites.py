from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.properties import StringProperty

KIVY_FONTS = [
    {
        "name": "RobotoCondensed",
        "fn_regular": "data/fonts/RobotoCondensed-Light.ttf",
        "fn_bold": "data/fonts/RobotoCondensed-Regular.ttf",
        "fn_italic": "data/fonts/RobotoCondensed-LightItalic.ttf",
        "fn_bolditalic": "data/fonts/RobotoCondensed-Italic.ttf"
    }
]

for font in KIVY_FONTS:
    LabelBase.register(**font)


class Favorites(BoxLayout):

    def __init__(self, **kwargs):
        super(Favorites, self).__init__(**kwargs)
        self.mistakes_list = {'2016-02-31': 'My mistake last week',
                              '2016-01-31': 'My mistake last month',
                              '2015-02-31': 'My mistake last year'}
        self.mistake_grid.bind(minimum_height=self.mistake_grid.setter('height'))

        for date, mistake in self.mistakes_list.iteritems():
            new = Mistake(date=date, mistake=mistake)
            self.children[1].children[0].add_widget(new)


class Mistake(BoxLayout):
    date = StringProperty('')
    mistake = StringProperty('')