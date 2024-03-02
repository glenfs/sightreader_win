from kivy.app import App
from kivy.core.text import Label as CoreLabel
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.animation import Animation
from random import randint


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

class CircleApp(App):
    def build(self):
        root = Widget()
        animated_circles = AnimatedBubbles()
        root.add_widget(animated_circles)

        # Schedule the creation of circles
        from kivy.clock import Clock
        Clock.schedule_interval(animated_circles.create_circle, 1)

        return root

if __name__ == '__main__':
    CircleApp().run()
