from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1
        self.rows = 2

        self.subgrid = GridLayout() #mini grid within a grid
        self.subgrid.cols = 2
        
        self.subgrid.add_widget(Label(text="Firstname: "))
        self.firstname = TextInput(multiline=False)
        self.subgrid.add_widget(self.firstname)
        
        self.subgrid.add_widget(Label(text="Lastname: "))
        self.lastname = TextInput(multiline=False)
        self.subgrid.add_widget(self.lastname)
        
        self.subgrid.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.subgrid.add_widget(self.email)

        #main grid

        self.add_widget(self.subgrid)

        self.submit = Button(text="Submit", font_size=20)
        self.submit.bind(on_press=self.pressed) #takes in a function to run when pressed
        self.add_widget(self.submit)
    
    def pressed(self, instance): #called when button is pressed. instance references the button that has been pressed.
        print("Pressed")
        firstname = self.firstname.text
        lastname = self.lastname.text
        email = self.email.text

        print(f"Name: {firstname} {lastname}\nEmail: {email}")

        self.firstname.text = ""
        self.lastname.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()