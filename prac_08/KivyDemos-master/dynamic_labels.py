from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
import random


class DynamicLabels(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self):
        super().__init__()
        self.names = ['james', 'bob', 'harry', 'mitchell']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:  # Not Completed
            label = Label(text=name)
            label.color = (random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), 1)
            self.root.ids.main.add_widget(label)
        return self.root


DynamicLabels().run()
