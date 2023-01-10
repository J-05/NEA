from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color

class SelectionCursor(Widget):
    def __init__(self, **kwargs):
        super(SelectionCursor, self).__init__(**kwargs)

        #ATTRIBUTES
        self.size = (0, 0) #CHANGE THIS
        self.position = (0, 0)
        self.restriction_bounds = ((0, 0), (0, 0))
        self.cursor = None

    def draw(self):
        pass

    def place(self, size, position):
        self.set_size(size)
        self.set_position(position)

        self.draw()

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def set_restriction_bounds(self, bounds):
        self.restriction_bounds = bounds

    def set_cursor(self, cursor):
        self.cursor = cursor

class SelectionCursorCircle(SelectionCursor):
    def __init__(self, **kwargs):
        super(SelectionCursorCircle, self).__init__(**kwargs)
    
    def draw(self):
        with self.canvas:
            self.canvas.clear()
            Color(1, 1, 1, 1)
            self.cursor = Ellipse(size=(self.get_size()), pos=(self.get_position()))
            
class MyApp(App):
    def build(self):
        my_cursor = SelectionCursorCircle()
        my_cursor.place((100, 100), (0, 400))

        return my_cursor

if __name__ == "__main__":
    MyApp().run()