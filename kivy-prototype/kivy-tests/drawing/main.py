from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.stencilview import StencilView

class Canvas(Widget):
	def on_touch_down(self, touch):
		print("woo")
		with self.canvas:
			paint_circle(touch)
			touch.ud["line"] = Line(points=((touch.x, touch.y)), width=10)

	def on_touch_move(self, touch):
		with self.canvas:
			touch.ud["line"].points += [touch.x, touch.y]


			

def paint_circle(touch):
	Color(0, 1, 1)
	d = 30.
	Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d, d))

class MyApp(App):
	def build(self):
		return Canvas()

if __name__ == "__main__":
	MyApp().run()