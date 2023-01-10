from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color

class CircleWidget(Widget):
    def __init__(self, **kwargs):
        super(CircleWidget, self).__init__(**kwargs)

        with self.canvas:
            self.my_circle = Ellipse(size=(100, 100), pos=(100, 100))
            
    def on_touch_down(self, touch):
        with self.canvas:
            self.my_circle.pos = (200, 100)

class MyApp(App):
    def build(self):
        return CircleWidget()

if __name__ == "__main__":
    MyApp().run()