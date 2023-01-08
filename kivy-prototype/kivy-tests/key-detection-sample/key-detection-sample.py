from tkinter import SEL
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

class Layout(FloatLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode)
        if keycode[1] == 'w':
            print("yooo")
        return True

    def on_touch_down(self, touch):
        print(touch.pos)

class KeyDown(App):
    '''
    def build(self):
        Window.bind(on_key_down=self.key_action)
        return Widget()

    def key_action(self, *args):
        print ("got a key event: %s" % list(args))
    '''

    def build(self):
        return Layout()


if __name__ == '__main__':
    KeyDown().run()