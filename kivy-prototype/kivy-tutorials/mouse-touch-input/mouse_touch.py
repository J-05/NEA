from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class Touch(Widget):
    btn = ObjectProperty(None)
    def on_touch_down(self, touch): #these methods inherit from widget, so we override
        print("Mouse down", touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print("Mouse move", touch)

    def on_touch_up(self, touch):
        print("Mouse up", touch)
        self.btn.opacity = 1

class AppInputs(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    AppInputs().run()