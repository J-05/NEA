from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button #uix folder

class MyApp(App):
    def build(self): #defines all the components in the interface
        return Label(text="test")

if __name__ == "__main__":
    MyApp().run()