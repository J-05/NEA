import kivy
kivy.require("2.1.0")

from kivy.app import App #for main app
from kivy.uix.widget import Widget 
from kivy.uix.scatter import Scatter
from kivy.uix.stencilview import StencilView
from kivy.graphics import Ellipse, Rectangle, Color, Line
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen #different screens
from kivy.config import Config #change window size
from kivy.lang import Builder
import os
import sys

##### VARIABLES #####
setup_dict = {} #contain setup information e.g size of window

##### GET SETUP VALUES FROM FILE #####
#sys.path[0] returns the path of the current module
#os.path.join joins the directory path to the file name
with open(os.path.join(sys.path[0], "setup.txt"), "r") as setup_file:
    for line in setup_file.readlines():
        #split each line into key and value pair stored in setup_dict
        key = line.replace("\n", "").split(";")[0]
        value = line.replace("\n", "").split(";")[1]

        setup_dict[key] = int(value)

class MainWindow(Screen):
    toolwin_width = setup_dict["toolwin_default_width"]
    toolbar_height = setup_dict["toolbar_default_height"]

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 1, 1)
            d = 10
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d, d))
            touch.ud["Line"] = Line(points=(touch.x, touch.y), width=d)

    def on_touch_move(self, touch):
        with self.canvas:
            touch.ud["Line"].points += [touch.x, touch.y]
        

class WindowManager(ScreenManager):
    pass

class Conjure(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":    

    ##### APP RUN #####
    Config.set('graphics', 'width', setup_dict["window_width"])
    Config.set('graphics', 'height', setup_dict["window_height"])

    print("hi")
    print(setup_dict["toolwin_default_width"])

    Conjure().run()

    print("end")