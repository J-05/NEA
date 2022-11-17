from kivy.app import App
from kivy.uix.widget import Widget

class Touch(Widget):
    def on_touch_down(self, touch):
        pass

    def on_touch_move(self, touch):
        pass

    def on_touch_up(self, touch):
        pass

class UserInputs(App):
    def build(self):
        return 

if __name__ == "__main__":
    UserInputs().run()