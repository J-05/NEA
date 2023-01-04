from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

'''
Grid layout consists of columns and rows in which widgets are placed.
Can have grid layouts within grid layouts
'''

class MyGrid(GridLayout): #will contain all the design elements
    def __init__(self, **kwargs): #varying number of inputs can be taken in
        super(MyGrid, self).__init__(**kwargs) #sets up values
        self.cols = 2

        self.add_widget(Label(text="First Name: ")) #method inherited from GridLayout 
        self.firstname = TextInput(multiline=False) #multiline=False prevents text input from consisting of multiple lines
        self.add_widget(self.firstname)

        self.add_widget(Label(text="Last Name: ")) #method inherited from GridLayout 
        self.lastname = TextInput(multiline=False) #multiline=False prevents text input from consisting of multiple lines
        self.add_widget(self.lastname)

        self.add_widget(Label(text="Email: ")) #method inherited from GridLayout 
        self.email = TextInput(multiline=False) #multiline=False prevents text input from consisting of multiple lines
        self.add_widget(self.email)

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()