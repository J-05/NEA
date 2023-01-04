from kivy.app import App
from kivy.lang import Builder #allows kv files to load without fitting naming convention
from kivy.uix.screenmanager import ScreenManager, Screen #allows use of diff windows

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager): #represents transitions between windows
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()