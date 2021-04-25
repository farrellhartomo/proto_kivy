
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from kivy.core.window import Window
Window.size = (480,705)

#Builder.load_file("login/login.kv")

class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.verifyLogin()

    def verifyLogin(self):
        info = self.ids["info_txt"]
        username = self.ids["usr_txt"].text
        password = self.ids["usr_pwd"].text

        if username == "admin" and password == "admin":
            info.text = 'logged in successfully!'
        else:
            if username =='' and password == '':
                info.text = 'Please enter username and password'
            else:
                info.text = 'Incorrect username or password'

    
class loginApp(MDApp):
    def build(self):
        return LoginPage()

if __name__ == "__main__":
    loginApp().run()
