from kivymd.app import MDApp
from kivy_garden.mapview import MapView
from kivymd.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

from kivy.core.window import Window
Window.size = (480,705)

Builder.load_file('tripgps.kv')

class TripMap(MapView):
    pass


class TripGpsPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class tripgpsApp(MDApp):
    def build(self):
        return TripGpsPage()

if __name__ == '__main__':
    tripgpsApp().run()
