from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.config import Config
from index_calculator import calculate_index

'''
RBG TRANSITIONS

r: 255 | 255 | 0   | 0   | 0   | 255 | 255
g: 0   | 255 | 255 | 255 | 0   | 0   | 0
b: 0   | 0   | 0   | 255 | 255 | 255 | 0
'''

class ColourWheel(Widget):
    def __init__(self, colour_width, start_x, y, **kwargs):
        super(ColourWheel, self).__init__(**kwargs)

        #colour bar starts at 255, 0, 0
        colours = [255, 0, 0]

        index = 2 #changes begin with g value, index 1
        change = -1 #value will start with adding 1
        colour_x = start_x - 1 #position of the colour bar will start at this value +1
        self.start_x = start_x
        self.colour_y = y
        self.colour_width = colour_width

        with self.canvas:
            print("wow")
            Color(1, 1, 0, 1)
            point1 = self.start_x
            point2 = self.start_x + (255 * 6 * self.colour_width)
            print(f"1: {point1}, 2:{point2}")
            Line(points=(point1, 50, point2, 50))

        with self.canvas:
            self.colour_preview_square = Rectangle(size=(100, 100), pos=(500, 350))

            for i in range(len(colours)): #every colour r, g, b...
                for i in range(2): #will undergo an increase and decrease from 0 to 255
                    index = (index + 2) % 3 #loops through list backwards starting from g giving g, r, b etc
                    change *= -1 #changes from 1 to -1 etc
                    for i in range(255): #max colour value
                        colour_x += colour_width #size of each colour rectangle
                        colours[index] = colours[index] + (change) #applies the change to the value of the current colour
                        Color(colours[0]/255, colours[1]/255, colours[2]/255, 1) #changes the paint colour and changes it to rgba format
                        Rectangle(pos=(colour_x, self.colour_y), size=(colour_width, 10)) #colour is drawn

    def on_touch_down(self, touch):
        pass

    def on_touch_move(self, touch):
        if touch.x >= self.start_x and touch.x <= self.start_x + (255 * 6 * self.colour_width):
            raw_distance_x = touch.x - self.start_x
            full_distance_x = raw_distance_x / self.colour_width
            segment = int(((full_distance_x)// 255)) + 1
            colour_value = int((full_distance_x)) % 255
            print(f"og colour val: {colour_value}")

            if segment % 2 == 0:
                colour_value = 255 - colour_value

                
            colour_preview_square_colour = [0, 0, 0]
            max_colour_index = int(((segment // 2) % 3))
            changing_colour_index = int(calculate_index(segment, 2))
            print(f"segment:{segment}, max colour index: {max_colour_index}, changing colour index: {changing_colour_index}")

            colour_preview_square_colour[max_colour_index] = 1
            colour_preview_square_colour[changing_colour_index] = colour_value/255
            
            with self.canvas:
                Color(*colour_preview_square_colour, 1)
                self.colour_preview = Rectangle(size=(100, 100), pos=(500, 350))

                print(colour_preview_square_colour)
        print("")

class MainApp(App):
    def build(self):
        return ColourWheel(0.2, 10, 350)
    
if __name__ == "__main__":

    Config.set('graphics', 'width', 1200)
    Config.set('graphics', 'height', 700)

    MainApp().run()