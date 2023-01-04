from kivy.uix.widget import Widget
from kivy.app import App
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        #widget has a canvas property
        with self.canvas:
            #to change colour, the colour of the canvas must be changed first then the shape can be drawn
            Color(1, 0, 0, 1, mode="rgba")
            self.rect = Rectangle(pos=(0,0), size=(50, 50))

            Line(points=(20, 30, 12, 400))

    def on_touch_down(self, touch):
        print("down", touch.pos)
        self.rect.pos = touch.pos

    def on_touch_move(self, touch):
        print("move", touch)
        self.rect.pos = touch.pos

    def on_touch_up(self, touch):
        print("up", touch)

class MyApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp().run()

    from kivy.app import App


