from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget #when using kv file then class will inherit from widget
from kivy.properties import ObjectProperty

class MyGrid(Widget): 
    name = ObjectProperty(None) #initially there will be no value in this obejct property until the kv file is read

    def button_activate(self):
        print(f"Name: {self.name.text}")
        self.name.text = ""
        self.name.text = ""

class KvLangPractice(App): #kivy will automatically  look for a kv file with the name my.kv
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    KvLangPractice().run()
