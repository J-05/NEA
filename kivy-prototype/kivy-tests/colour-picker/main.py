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
    def __init__(self, **kwargs):
        super(ColourSquare, self).__init__(**kwargs)

        #ATTRIBUTES
        self.side_length = 0
        self.pos = (0, 0)
        self.current_colour = (0, 0, 0)

    def place(self, side_length, pos, colour):
        self.side_length = side_length
        self.pos = pos
        self.current_colour = colour

        self.draw()

    def draw(self):
        current_colour = [0, 0, 0]
        current_position = [*self.pos]
        rect_side_length = self.side_length/255
        constant_rgb_indexes = [x for x in range(0, 3) if self.current_colour[x] == 255]

        for max_colour_val in range(0, 256): #going vertically up the square, the maximum brightness increases
            current_position[0] = self.pos[0]
            sub_base_colour = [(val * max_colour_val/255) for val in self.current_colour] #calculates the most saturated colour in current brightness

            current_colour = [max_colour_val, max_colour_val, max_colour_val] #starts from left (no saturation, current max brightness)
            for i in range(0, 256):
                with self.canvas:
                    Color(*[val/255 for val in current_colour], 1) #convert to rbga
                    Rectangle(size=(rect_side_length, rect_side_length), pos=(current_position[0], current_position[1]))

                for index in range(0, 3): #decrement colour values by max value - target value / 255
                    if index not in constant_rgb_indexes: #prevents unnecessary decrement by 0 for the max value
                        current_colour[index] -= (max_colour_val - sub_base_colour[index])/255

                current_position[0] += rect_side_length #increment x by 1 unit

            current_position[1] += rect_side_length #increment y by 1 unit
            
    def update_colour(self, colour):
        self.current_colour = colour
        self.draw()

    def get_colour_from_coord(self, pointer_pos):
        new_colour = (0, 0, 0)
        return new_colour

class ColourBar(Widget):
    def __init__(self, **kwargs):
        super(ColourBar, self).__init__(**kwargs)

        #ATTRIBUTES
        self.pos = (0, 0)
        self.size = (0, 0)
        self.current_colour = (0, 0, 0)

    def place(self, size, pos, colour):
        self.pos = pos
        self.size = size
        self.current_colour = colour

        self.draw()

    def draw(self):
        current_colour = list(self.current_colour) #colour bar starts at 255, 0, 0
        current_colour_index = 2 #changes begin with g value, index 1
        change = -1 #value will start with adding 1
        rect_x = self.pos[0] - 1 #position of the colour bar will start at this value +1
        rect_width = self.size[0] / (6 * 255)
        rect_height = self.size[1]

        for i in range(len(current_colour)): #every colour r, g, b...
            for j in range(2): #will undergo an increase and decrease from 0 to 255
                current_colour_index = (current_colour_index + 2) % 3 #loops through list backwards starting from g giving g, r, b etc
                change *= -1 #changes from 1 to -1 etc

                for k in range(0, 255): #max colour value
                    rect_x += rect_width #size of each colour rectangle
                    current_colour[current_colour_index] = current_colour[current_colour_index] + (change) #applies the change to the value of the current colour
                    with self.canvas:
                        Color(*[x/255 for x in current_colour], 1) #changes the paint colour and changes it to rgba format
                        Rectangle(pos=(rect_x, self.pos[1]), size=(rect_width, rect_height)) #colour is drawn

    def get_colour_from_coord(self, pointer_pos):
        raw_distance_x = pointer_pos[0] - self.pos[0]
        full_distance_x = raw_distance_x * ((255 * 6) / self.size[0]) #full distance as in scaled from 0 to 255 * 6
        segment = int(((full_distance_x) // 255)) + 1 #the bar is divided into 6 segments in which r, g, or b is either changing, 255, or 0
        colour_value = int((full_distance_x)) % 255 #the rgb value of the colour that is currenty changing
        new_colour = [0, 0, 0] #final rgb value 

        if segment % 2 == 0: #if segment is even then the colour value is decreasing
            colour_value = 255 - colour_value

        max_colour_index = int(((segment // 2) % 3)) #finds the index of the colour (r, g, or b) that has a value of 255
        changing_colour_index = int(calculate_index(segment, 2)) #finds the index of the colour (r, g, or b) that is currently changing

        new_colour[max_colour_index] = 255 #adds these values to the final rbg value
        new_colour[changing_colour_index] = colour_value
        
        return new_colour

    def on_touch_down(self, touch):
        if touch.x >= self.pos[0] and touch.x <= self.pos[0] + (255 * 6 * self.size[0] / (6 * 255)):
            self.current_colour = self.get_colour_from_coord(touch.pos)
            ColourPicker().update_colour(self.current_colour)

    def on_touch_move(self, touch):
        if touch.x >= self.pos[0] and touch.x <= self.pos[0] + (255 * 6 * self.size[0] / (6 * 255)):
            self.current_colour = self.get_colour_from_coord(touch.pos)
            ColourPicker().update_colour(self.current_colour)

class ColourPreviewSquare(Widget):
    def __init__(self, **kwargs):
        super(ColourPreviewSquare, self).__init__(**kwargs)

        #ATTRIBUTES
        self.side_length = 0
        self.pos = (0, 0)
        self.colour = (0, 0, 0)

    def place(self, side_length, pos, colour):
        self.side_length = side_length
        self.pos = pos
        self.colour = colour

        self.draw()

    def draw(self):
        with self.canvas:
            print("my colour is defenitnelty", str(self.colour))
            Color(*[x/255 for x in self.colour], 1) #converts colour to rgba format
            self.colour_preview_square = Rectangle(size=(self.side_length, self.side_length), pos=(self.pos[0], self.pos[1]))

    def update_colour(self, new_colour):
            print(f"old colour: {self.colour} vs new colour {new_colour}")
            self.colour = new_colour
            print(f"my new colour is now {self.colour}")
            self.draw()


class ColourPicker(FloatLayout): #change to box layout-------------------------------------------------------------------------------------------------------
    def __init__(self, **kwargs):
        super(ColourPicker, self).__init__(**kwargs)

        #ATTRIBUTES
        self.current_colour = (255., 0., 0.) 

        #widgets
        self.colour_square = ColourSquare()
        self.colour_bar = ColourBar()
        self.colour_preview_square = ColourPreviewSquare()

        self.add_widget(self.colour_square)
        self.add_widget(self.colour_bar)
        self.add_widget(self.colour_preview_square)

        #PLACE WIDGETS
        self.set()

    def set(self):
        #when initialised/reset starts with red as chosen colour
        self.colour_square.place(400, (400, 400), self.current_colour)
        self.colour_bar.place((400, 10), (400, 300), self.current_colour)
        self.colour_preview_square.place(50, (300, 300), self.current_colour)

    def update_colour(self, new_colour):
        #updates colour square only if base colour changes
        if self.convert_colour_to_base_colour(self.current_colour) != self.convert_colour_to_base_colour(new_colour):
            self.colour_square.update_colour(new_colour)

        self.current_colour = (new_colour)
        self.colour_preview_square.update_colour(self.current_colour)

        print("HELP MY COLOUR IS DEFINETLY ", str(self.colour_preview_square.colour))

    def convert_colour_to_base_colour(self, colour): #returns base colour - brightest and most saturated
        if 255. not in colour:
            return tuple([float(x*(255/max(colour))) for x in colour])
        else:
            return colour



class MainApp(App):
    def build(self):
        return ColourPicker()
    
if __name__ == "__main__":

    Config.set('graphics', 'width', 1200)
    Config.set('graphics', 'height', 700)

    MainApp().run()