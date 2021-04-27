from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty,ObjectProperty

from kivy.core.window import Window
Window.size = (480,705)

Builder.load_file("trip/trip.kv") 

class ContentNavDrawer(BoxLayout):
    scr_mgr = ObjectProperty()
    nav_drawer = ObjectProperty()


class DrawerItem(OneLineAvatarIconListItem):
    icon = StringProperty()

class CityCardList(MDCard):
    pass

class BaseShadowWidget(Widget):
    pass

class ShadowToCard(CityCardList,BaseShadowWidget):
    pass

class TripPage(BoxLayout):
    def load_icons(self):
        self.icon_items = {
            "account-cash":"Set your budget",
            "map":"Travel Maps",
            "star":"Favourite Places",
            "application-cog":"Settings",
        }

    def user_logout(self):
        app = MDApp.get_running_app()
        self.parent.parent.current = 'scr_login'
        print(app.root.ids.scr_login.ids)


    def load_card_list(self):
        for i in range(5):
            self.ids.stack_item.add_widget(CityCardList())

    def load_icon_list(self):
        for icon_name in self.icon_items.keys():
            self.ids.nav_drawer.add_widget(DrawerItem(icon=icon_name, text=self.icon_items[icon_name]))


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_icons()
        self.load_card_list()
        self.load_icon_list()
        

class tripApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return TripPage()

if __name__ == '__main__':
    tripApp().run()