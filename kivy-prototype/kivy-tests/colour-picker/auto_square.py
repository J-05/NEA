from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class MyRect(Widget):
    def __init__(self, **kwargs):
        super(MyRect, self).__init__(**kwargs)

        self.draw_colour_square(100, (100, 100), (255, 0, 0))

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

class MyApp(App):
    def build(self):
        return MyRect()

if __name__ == "__main__":
    MyApp().run()