from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

import kivy.properties as KVprop 

#error handling
KVprop.ObjectProperty()

from kivy.core.window import Window
Window.size = (480,705)

from login.login import loginApp
from trip.trip import TripPage


class ScreenLogin(Screen):
    pass

class ScreenTrip(Screen):
    pass

class MainScreen(ScreenManager):
    screen_login = loginApp()
    screen_trip = TripPage()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.scr_login.add_widget(self.screen_login)
        #self.ids.scr_trip.add_widget(self.screen_trip)

class frlApp(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return MainScreen()

if __name__ == '__main__':
    frlApp().run()