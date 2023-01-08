from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.stencilview import StencilView
from kivy.uix.floatlayout import FloatLayout

class Canvas(Widget):	
	pass

class MainStencil(StencilView):
	def __init__(self, **kwargs):
		super(MainStencil, self).__init__(**kwargs)

		with self.canvas:
			Color(1, 1, 1, 0.2)
			Rectangle(pos=self.pos, size=self.size)

	def on_touch_down(self, touch):
		with self.canvas:
			Color(1, 1, 0, 1)
			d = 10
			Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(10, 10))
			touch.ud["Line"] = Line(points=(touch.x, touch.y), width=d)

	def on_touch_move(self, touch):
		touch.ud["Line"].points += [touch.x, touch.y]

class MyApp(App):
	def build(self):

		root = FloatLayout()
		#canvas = Canvas()
		stencil = MainStencil(pos=(0, 0), size=(100, 100))

		#root.add_widget(canvas)
		root.add_widget(stencil)

		return root

if __name__ == "__main__":
	MyApp().run()