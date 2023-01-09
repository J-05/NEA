from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Line
from kivy.config import Config
from index_calculator import calculate_index

'''
RBG TRANSITIONS

r: 255 | 255 | 0   | 0   | 0   | 255 | 255
g: 0   | 255 | 255 | 255 | 0   | 0   | 0
b: 0   | 0   | 0   | 255 | 255 | 255 | 0
'''

class ColourSquare(Widget):
    def __init__(self, side_width, start_pos, **kwargs):
        super(ColourSquare, self).__init__(**kwargs)

        self.side_width = side_width
        self.start_pos = start_pos

        current_colour = (255, 0, 0)

        self.draw_colour_square(self.side_width, self.start_pos, current_colour)

    def draw_colour_square(self, side_width, start_pos, base_colour):
        current_colour = [0, 0, 0]
        current_position = [*start_pos]
        rect_side = side_width/255
        constant_rgb_indexes = [x for x in range(0, 3) if base_colour[x] == 255]

        for max_colour_val in range(0, 256): #going vertically up the square, the maximum brightness increases
            current_position[0] = start_pos[0]
            sub_base_colour = [(val * max_colour_val/255) for val in base_colour] #calculates the most saturated colour in current brightness

            current_colour = [max_colour_val, max_colour_val, max_colour_val] #starts from left (no saturation, current max brightness)
            for i in range(0, 256):
                with self.canvas:
                    Color(*[val/255 for val in current_colour], 1) #convert to rbga
                    Rectangle(size=(rect_side, rect_side), pos=(current_position[0], current_position[1]))

                for index in range(0, 3): #decrement colour values by max value - target value / 255
                    if index not in constant_rgb_indexes: #prevents unnecessary decrement by 0 for the max value
                        current_colour[index] -= (max_colour_val - sub_base_colour[index])/255

                current_position[0] += rect_side #increment x by 1 unit

            current_position[1] += rect_side #increment y by 1 unit
            

class ColourBar(Widget):
    def __init__(self, colour_width, start_x, y, **kwargs):
        super(ColourBar, self).__init__(**kwargs)

        #colour bar starts at 255, 0, 0
        colours = [255, 0, 0]

        index = 2 #changes begin with g value, index 1
        change = -1 #value will start with adding 1
        colour_x = start_x - 1 #position of the colour bar will start at this value +1
        self.start_x = start_x
        self.colour_y = y
        self.colour_width = colour_width/(255*6)

        with self.canvas:
            Color(1, 1, 0, 1)

        with self.canvas:
            self.colour_preview_square = Rectangle(size=(100, 100), pos=(100, 100))

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
        if touch.x >= self.start_x and touch.x <= self.start_x + (255 * 6 * self.colour_width):
            raw_distance_x = touch.x - self.start_x
            full_distance_x = raw_distance_x / self.colour_width
            segment = int(((full_distance_x)// 255)) + 1
            colour_value = int((full_distance_x)) % 255

            if segment % 2 == 0:
                colour_value = 255 - colour_value

                
            colour_preview_square_colour = [0, 0, 0]
            max_colour_index = int(((segment // 2) % 3))
            changing_colour_index = int(calculate_index(segment, 2))

            colour_preview_square_colour[max_colour_index] = 1
            colour_preview_square_colour[changing_colour_index] = colour_value/255
            
            with self.canvas:
                Color(*colour_preview_square_colour, 1)
                self.colour_preview = Rectangle(size=(100, 100), pos=(100, 100))

    def on_touch_move(self, touch):
        if touch.x >= self.start_x and touch.x <= self.start_x + (255 * 6 * self.colour_width):
            raw_distance_x = touch.x - self.start_x
            full_distance_x = raw_distance_x / self.colour_width
            segment = int(((full_distance_x)// 255)) + 1
            colour_value = int((full_distance_x)) % 255

            if segment % 2 == 0:
                colour_value = 255 - colour_value

                
            colour_preview_square_colour = [0, 0, 0]
            max_colour_index = int(((segment // 2) % 3))
            changing_colour_index = int(calculate_index(segment, 2))

            colour_preview_square_colour[max_colour_index] = 1
            colour_preview_square_colour[changing_colour_index] = colour_value/255
            
            with self.canvas:
                Color(*colour_preview_square_colour, 1)
                self.colour_preview = Rectangle(size=(100, 100), pos=(100, 100))

class ColourPicker(FloatLayout):
    def __init__(self, **kwargs):
        super(ColourPicker, self).__init__(**kwargs)

        #self.orientation = "verticle"
        #self.spacing = 500

        self.add_widget(ColourSquare(200, (500, 400)))
        self.add_widget(ColourBar(1000, 500, 350))

class MainApp(App):
    def build(self):
        return ColourPicker()
    
if __name__ == "__main__":

    Config.set('graphics', 'width', 1200)
    Config.set('graphics', 'height', 700)

    MainApp().run()