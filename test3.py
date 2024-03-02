from random import randint

from kivy.app import App
from kivy.graphics import Color, Ellipse
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget


class AnimatedBubbles(Widget):
    def create_circle(self, dt):
        x = randint(0, self.width)
        y = 0
        # Draw a small circle
        with self.canvas:
            Color(1, 1, 1)
            ellipse = Ellipse(pos=(x, y), size=(30, 30))

            # Animate the circle to move upwards and vanish
            anim = Animation(pos=(x, self.height), duration=3)
            anim.bind(on_complete=self.remove_circle)
            anim.start(ellipse)


    def remove_circle(self, animation, widget):
        # Remove the circle from the canvas when animation is complete
        self.canvas.remove(widget)

class AnimatedLabel(Label):
    def __init__(self, **kwargs):
        super(AnimatedLabel, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.font_size = '20sp'
        self.center_x = Window.width / 2
        self.y = 100

    def animate(self):
        anim = Animation(y=Window.height, duration=3)
        anim.start(self)
        Clock.schedule_once(lambda dt: self.parent.remove_widget(self), 2)


class AnimatedTextApp(App):
    def build(self):
        root = Label()
        root.size_hint = (None, None)
        root.size = Window.size

        label = AnimatedLabel(text="Hello, World!")
        root.add_widget(label)
        label.animate()

        return root


if __name__ == "__main__":
    AnimatedTextApp().run()
