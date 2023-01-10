from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class SelectionSlider(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        return SelectionSlider()

if __name__=="__main__":
    MyApp().run()