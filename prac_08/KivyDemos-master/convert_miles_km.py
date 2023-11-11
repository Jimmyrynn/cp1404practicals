from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM_RATE = 1.609344
INCREMENT = 1


class MilesConverterApp(App):
    """App for converting miles to kilometres."""
    def build(self):
        Window.size = (500, 200)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def add_increment(self, value):
        """Add increment to input when button is pressed"""
        try:
            result = int(value) + INCREMENT
            self.root.ids.input_number.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0)

    def subtract_increment(self, value):
        """Subtract increment from input when button is pressed"""
        try:
            result = int(value) - INCREMENT
            self.root.ids.input_number.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0)

    def convert_miles_to_km(self, value):
        """Convert miles to kilometers"""
        try:
            result = int(value) * MILES_TO_KM_RATE
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0)


MilesConverterApp().run()
