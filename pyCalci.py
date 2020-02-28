import kivy
kivy.require('1.09.1')

from kivy.app import App
from kivy.uix.button import Label

class CalciUI(App):

    def build(self):
        return Label(text="pyCalci: A next gen calculator")

if __name__ == "__main__":
    calc = CalciUI()
    calc.run()
