from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from extra import convert_rgb_to_rgba

class SelectionArea(Widget):
    def __init__(self, size, pos, **kwargs):
        super(SelectionArea, self).__init__(**kwargs)

        self.size = size
        self.pos = pos
        self.select_coords = self.pos

    def draw(self):
        pass

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

    def get_select_coords(self):
        return self.select_coords

    def set_select_coords(self, coords):
        self.select_coords = coords

class SelectionBar(SelectionArea):
    def __init__(self, size, pos, base_colour, fill_colour, **kwargs):
        super(SelectionBar, self).__init__(size, pos, **kwargs)

        self.base_colour = base_colour
        self.fill_colour = fill_colour

    def draw(self):
        with self.canvas:
            Color(*convert_rgb_to_rgba(self.get_base_colour()))
            base_rectangle = Rectangle(pos=self.get_pos(), size=self.get_size())
            Color(*convert_rgb_to_rgba(self.get_fill_colour()))
            print(*convert_rgb_to_rgba(self.get_fill_colour()))
            fill_rectangle = Rectangle(pos=self.get_pos(), size=(self.get_select_width(), self.get_size()[1]))
            
    def get_base_colour(self):
        return self.base_colour

    def set_base_colour(self, colour):
        self.base_colour = colour

    def get_fill_colour(self):
        return self.fill_colour

    def set_fill_colour(self, colour):
        self.fill_colour = colour

    def get_select_width(self):
        return self.get_select_coords()[0] - self.get_pos()[0]

class MyApp(App):
    def build(self):
        bar = SelectionBar((500, 10), (100, 300), (255, 255, 255, 1), (255, 255, 0, 1))
        bar.draw()

        return bar

if __name__ == "__main__":
    MyApp().run()