# This is test 1 for the application in kivy

import kivy

from kivy.app import App
from kivy.uix.gridlayout import *
from kivy.config import Config

kivy.require('2.1.0')
# Assume price of the goods are xx.xx format
# Setting the configuration, resizable makes the calculator fits in any screen size
Config.set('graphics', 'resizable', 1)

tax_ratio = 1.13


# Defining classes

# This class is for creating the layout for calculator
class CalcLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str("%.2f" % (eval(calculation)))

            # Arithmatic Error Checking
            except Exception:
                self.display.text = "Error"

    def tax(self, calculation):
        if calculation:
            try:
                self.display.text = str("%.2f" % (eval(calculation) * tax_ratio))
            # Arithmatic Error Checking
            except Exception:
                self.desplay.text = "Error"

    def delete(self, calculation):
        if calculation:
            try:
                self.display.text = self.display.text[:-1]
            # Arithmatic Error Checking
            except Exception:
                self.display.text = "Error"


# This name should be as it so it can call the kv file
class CalculatorApp(App):

    def build(self):

        return CalcLayout()


# Creating a copy of the class and run, avoiding straight calling on the class
App = CalculatorApp()
App.run()
