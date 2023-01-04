from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GridMain(GridLayout):
    def __init__(self, **kwargs):
        super(GridMain, self).__init__(**kwargs)

        self.rows = 2
        self.cols = 1

        self.add_widget(MyGrid())

        self.submit = Button(text="Submit", font_size=20)
        self.add_widget(self.submit)

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Firstname: "))
        self.firstname = TextInput(multiline=False)
        self.add_widget(self.firstname)

        self.add_widget(Label(text="Lastname: "))
        self.lastname = TextInput(multiline=False)
        self.add_widget(self.lastname)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

class MyApp(App):
    def build(self):
        return GridMain()

if __name__ == "__main__":
    MyApp().run()