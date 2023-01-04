from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.widget import Widget #grid class has to inherit from widget when using kv files

class MyGrid(Widget):
    pass

class MyApp(App): #kv file named after this class name, but if app is present then remove app from the name
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()