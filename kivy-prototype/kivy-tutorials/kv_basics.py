from kivy.app import App #import app class from kivy
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#class holding all design elements
class MyGrid(GridLayout):
    def __init__(self, **kwargs): #take an infinite amount of parameters
        super(MyGrid, self).__init__(**kwargs) #calls gridlayout constructor

        #creating second grid layout for formatting
        self.inside = GridLayout()
        self.inside.cols = 2


        self.cols = 1 #num of columns
        self.inside.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False) #text can span one line only
        self.inside.add_widget(self.name)

        self.add_widget(self.inside)

        #button
        self.submit = Button(text="Submit", font_size=30)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance): #when button pressed
        name = self.name.text #get text in name widget

        print(f"Name = {name}")
        self.name.text = ""
class MyApp(App): #class inherits from app
    #constructor of App is automatically called.

    def build(self): #main interface for app
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
