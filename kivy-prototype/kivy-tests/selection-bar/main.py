from kivy.app import App
from kivy.widget import Widget

class SelectionBar(Widget):
    def __init__(self, **kwargs):
        super(SelectionBar, self).__init__(**kwargs)

        #ATTRIBUTES
        self.size = ()
        self.pos = ()




class MyApp(App):
    def build(self):
        return SelectionBar

if __name__ == "__main__":
    MyApp().run()