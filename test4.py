from kivy.app import App
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage


class StreakWidget(Widget):
    def __init__(self, **kwargs):
        super(StreakWidget, self).__init__(**kwargs)
        self.pos = kwargs.pop('pos', '')
        # Create Ellipse
        with self.canvas:
            Color(1, 1, 1)  # Set color to red
            self.ellipse = Ellipse(pos=self.pos, size=(20, 20))
            image_path = 'images/streak_Green.png'
            self.ellipse.texture = CoreImage(image_path).texture

        # Create Label
        self.label = Label(text='4 in a row +10', font_size=dp(12), pos=(self.pos[0]-50, self.pos[1]), opacity=1)
        self.add_widget(self.label)

        # Schedule the animation
        Clock.schedule_once(self.animate_objects, 1)

    def animate_objects(self, dt):
        # Animate Ellipse
        ellipse_anim = Animation(pos=(self.ellipse.pos[0], self.ellipse.pos[1] + 100), size=(15, 15), duration=1)
        ellipse_anim.bind(on_complete=self.remove_circle)
        ellipse_anim.start(self.ellipse)

        # Animate Label
        label_anim = Animation(y=self.label.y + 100, opacity=0, duration=1)
        label_anim.bind(on_complete=self.remove_label)
        label_anim.start(self.label)

    def remove_circle(self, animation, widget):
        # Remove the circle from the canvas when animation is complete
        self.canvas.remove(widget)

    def remove_label(self, animation, widget):
        self.remove_widget(widget)


class MyApp(App):
    def build(self):
        return StreakWidget(pos=(300,300))


if __name__ == '__main__':
    MyApp().run()
