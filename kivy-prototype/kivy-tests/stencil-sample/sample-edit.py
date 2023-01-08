from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.stencilview import StencilView
from random import random as r
from functools import partial


class StencilTestWidget(StencilView):
    def __init__(self, **kwargs):
        super(StencilTestWidget, self).__init__(**kwargs)
        self.pos = (10, 10)
        self.size = (300, 300)

        with self.canvas:
            Color(1, 1, 1, 0.2)
            Rectangle(size=self.size, pos=self.pos)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0, 1)
            d = 10
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d, d))
            touch.ud["Lines"] = Line(points=(touch.x, touch.y), width=d)

    def on_touch_move(self, touch):
        with self.canvas:
            touch.ud["Lines"].points += [touch.x, touch.y]

class StencilCanvasApp(App):

    def add_rects(self, label, wid, count, *largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:
            for x in range(count):
                Color(r(), 1, 1, mode='hsv')
                Rectangle(pos=(r() * wid.width + wid.x,
                               r() * wid.height + wid.y), size=(10, 10))

    def reset_stencil(self, wid, *largs):
        wid.pos = (0, 0)
        wid.size = (200, 200)

    def reset_rects(self, label, wid, *largs):
        label.text = '0'
        wid.canvas.clear()

    def build(self):
        wid = StencilTestWidget(size_hint=(None, None))

        label = Label(text='0')

        btn_add500 = Button(text='+ 200 rects')
        btn_add500.bind(on_press=partial(self.add_rects, label, wid, 200))

        btn_reset = Button(text='Reset Rectangles')
        btn_reset.bind(on_press=partial(self.reset_rects, label, wid))

        btn_stencil = Button(text='Reset Stencil')
        btn_stencil.bind(on_press=partial(self.reset_stencil, wid))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add500)
        layout.add_widget(btn_reset)
        layout.add_widget(btn_stencil)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        rfl = FloatLayout()
        rfl.add_widget(wid)
        root.add_widget(rfl)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    StencilCanvasApp().run()