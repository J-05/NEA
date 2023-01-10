from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from extra import convert_rgb_to_rgba
from selection_cursor import SelectionCursorCircle

class SelectionBar(Widget):
    def __init__(self, size, pos, **kwargs):
        super(SelectionBar, self).__init__(**kwargs)

        self.size = size
        self.pos = pos

    def draw(self):
        with self.canvas:
            Color(1, 1, 1, 0.5)
            Rectangle(pos=self.get_pos(), size=self.get_size())

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

class MyApp(App):
    def build(self):
        bar = SelectionBar((500, 10), (100, 300))
        bar.draw()

        return bar

if __name__ == "__main__":
    MyApp().run()