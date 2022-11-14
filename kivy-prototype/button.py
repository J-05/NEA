from kivy.app import App #import kivy app module
from kivy.uix.label import Label #label for rendering text
from kivy.uix.button import Button
from functools import partial #allows us to use bind() function

#main program
class TestApp(App): #inherit from app class
    def build(self):
        button1 = Button(text="Clickable", background_color=(155, 0, 51, 53), pos=(300, 350, size_hint(0.25, 0.18))) 
        button1.bind(on_press=partial(self.disable, button1))
        button1.bind(onp_press=partial(self.update, button1))
        return button1 #returning a root widget

    def disable(self, instance, *args): #variable number of arguments, args is a local var which compiles all the parameters into a tuple.
        instance.disabled = True

    def update(self, instance, *args): #update the text of our instance
        instance.text = "I am disabled"

TestApp().run()
