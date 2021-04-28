from kivymd.app import MDApp
from kivy_garden.mapview import MapView, MapLayer,MapMarkerPopup,MapMarker
from kivymd.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

#import db needs to be commented later
import sqldbinit.sqldbinit as dbsetup 

from kivy.core.window import Window
Window.size = (480,705)

# Builder.load_file('tripgps/tripgps.kv')

class TripMap(MapView):
    pass

class TripGpsPage(BoxLayout):
    
    def set_all_location(self,lon,lat, condb):
        con = condb.
    # mainmarker = MapMarker(lat=-6.2,lon=106.8)
    # def add_mapmarker(self):       
    #     self.ids.tripmap.add_widget(self.mainmarker)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.add_mapmarker()

class tripgpsApp(MDApp):
    def build(self):
        return TripGpsPage()


if __name__ == '__main__':
    tripgpsApp().run()
