from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from extra import convert_rgb_to_rgba

class SelectionCursor(Widget):
    def __init__(self, size, pos, colour, **kwargs):
        super(SelectionCursor, self).__init__(**kwargs)

        #ATTRIBUTES
        self.size = size
        self.pos = pos
        self.cursor = None
        self.colour = colour

        self.shape_size = None
        self.shape_pos = None

    def draw(self):
        pass

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_pos(self):
        return self.pos

    def get_colour(self):
        return self.colour
        
    def set_colour(self, colour):
        self.colour = colour

    def set_pos(self, pos):
        self.pos = pos

    def get_shape_size(self):
        return self.shape_size

    def set_shape_size(self, size):
        self.shape_size = size

    def get_shape_pos(self):
        return self.shape_pos

    def set_shape_pos(self, pos):
        self.shape_pos = pos

class SelectionCursorCircle(SelectionCursor):
    def __init__(self, size, pos, colour, **kwargs):
        super(SelectionCursorCircle, self).__init__(size, pos, colour, **kwargs)
    
    def draw(self): #override draw
        with self.canvas:
            self.canvas.clear()
            Color(*convert_rgb_to_rgba(self.get_colour()))
            self.cursor = Ellipse(size=(self.get_size()), pos=(self.get_pos()))

class MyApp(App):
    def build(self):
        my_cursor = SelectionCursorCircle((100, 100), (50, 50), (255, 255, 0))
        my_cursor.draw()
        my_cursor2 = SelectionCursorCircle((50, 50), (50, 50), (255, 0, 0))
        my_cursor2.draw()

        return my_cursor2

if __name__ == "__main__":
    MyApp().run()