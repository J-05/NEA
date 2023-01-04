from kivy.app import App
from kivy.lang import Builder #will allow a kv file to be recognised despite the name of the app
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen): #first window, login window
    pass

class SecondWindow(Screen): #after login goto this page
    pass

class WindowManager(ScreenManager): #represent the transitions between main window and second window
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()