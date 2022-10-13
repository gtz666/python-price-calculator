# This is test 1 for the application in kivy

import kivy

from kivy.app import App
from kivy.uix.gridlayout import *
from kivy.config import Config

kivy.require('2.1.0')

# Setting the configuration, resizable makes the calculator fits in any screen size
Config.set('graphics', 'resizable', 1)


# Defining classes

# This class is for creating the layout for calculator
class CalcLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))

            except Exception:
                self.display.text = "Error"


# This name should be as it so it can call the kv file
class CalculatorApp(App):

    def build(self):

        return CalcLayout()


# Creating a copy of the class and run, avoiding straight calling on the class
App = CalculatorApp()
App.run()
