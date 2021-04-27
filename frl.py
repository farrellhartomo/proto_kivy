from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as kprop


from kivy.core.window import Window
Window.size = (480,705)

from trip.trip import TripPage
from login.login import LoginPage
from tripgps.tripgps import TripGpsPage
import db.sqldbinit as dbsetup 

class MapviewPage(TripGpsPage):
    tripgps_screen = kprop.ObjectProperty()

class TripScreen(TripPage):
    trip_screen = kprop.ObjectProperty()

class LoginScreen(LoginPage):
    log_screen = kprop.ObjectProperty()

class MainScreen(ScreenManager):
    # trippg = TripPage()
    def set_pages(self):
        self.ids.scr_login.add_widget(LoginPage())
        self.ids.scr_trip.add_widget(TripScreen())

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.set_pages()
        dbsetup

class frlApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return MainScreen()

if __name__ == '__main__':
    frlApp().run()