from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.theming import ThemeManager

from kivy.core.window import Window
Window.size = (480,705)

Builder.load_file("login/login.kv")

class LoginPage(BoxLayout):
    def verifyLogin(self):
        info = self.ids.info_txt
        username = self.ids.usr_txt.text
        password = self.ids.usr_pwd.text

        if username == "admin" and password == "admin":
            info.text = '[color=#ffffff]logged in successfully![/color]'
            self.parent.parent.current = 'scr_trip'

        elif username =='' and password == '':
            info.text = '[color=#ffffff]Please enter username and password[/color]'
        else:
            info.text = '[color=#ffffff]Incorrect username or password[/color]'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.verifyLogin()

class loginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return LoginPage()

if __name__ == "__main__":
    loginApp().run()
