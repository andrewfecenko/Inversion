from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.accordion import AccordionItem

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
        self.mistakes_list = {'2016-02-31': 'Missed the morning class',
                              '2016-01-31': 'Overslept',
                              '2015-02-31': 'Forgot to call papaw'}

        accordItem1 = AccordionItem()
        accordItem1.add_widget(Slide().build())
        accordItem1.title = 'Stats'
        self.ids.container.add_widget(accordItem1)

        accordItem2 = AccordionItem()
        scroll = ScrollView()
        grid = GridLayout(id='grid', size_hint_y=None, cols=1, row_default_height='20dp', row_force_default=True, spacing=20, padding=20)
        grid.bind(minimum_height=grid.setter('height'))
        scroll.add_widget(grid)
        accordItem2.add_widget(scroll)
        accordItem2.title = 'History Mistakes'
        self.ids.container.add_widget(accordItem2)
        # self.add_widget(scroll)

        for date, mistake in self.mistakes_list.iteritems():
            new = Mistake(date=date, mistake=mistake)
            grid.add_widget(new)


class Mistake(BoxLayout):
    date = StringProperty('')
    mistake = StringProperty('')


class Analyzer(BoxLayout):
    title = StringProperty('')
    content = StringProperty('')
    chart = StringProperty('')


class Slide(Carousel):
    def build(self):
        carousel = Carousel(direction='right', loop = True, size_hint=(1,1))
        src1 = "images/mock-up.png"
        image1 = AsyncImage(source=src1, allow_stretch=True)
        ana1 = Analyzer(title='Top1: 22 times', content='You missed the morning class ;(', chart=src1)

        carousel.add_widget(ana1)

        ana2 = Analyzer(title='Top2: 10 times', content='You forgot to call papaw ;/', chart=src1)
        carousel.add_widget(ana2)

        ana3 = Analyzer(title='Top3: 3 times', content='You spent too much money on games ;0', chart=src1)
        carousel.add_widget(ana3)

        return carousel
