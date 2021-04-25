
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.window import Window
Window.size = (480,705)

from trip.trip import TripPage
from login.login import LoginPage

class MainScreen(BoxLayout):
    screen_log = LoginPage()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.scr_login.add_widget(self.screen_log)
        self.ids.scr_trip.add_widget(self.screen_trip)

class frlApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return MainScreen()

if __name__ == '__main__':
    frlApp().run()