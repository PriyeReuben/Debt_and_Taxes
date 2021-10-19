from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


class DaTApp(BoxLayout):
    salary = float(input("What is your salary?"))
    max = salary * 2
    your_bracket = {}  # this should be empty
    taxable = []

    single_income_rates = {.1: 9950, .12: 40525, .22: 86375, .24: 164925, .32: 209425, .35: 523600, .37: max}
    married_jointly_income_rates = {.1: 19900, .12: 81050, .22: 172750, .24: 329850, .32: 418850, .35: 628300, .37: max}
    married_separately_income_rates = {.1: 9950, .12: 40525, .22: 86375, .24: 164925, .32: 209425, .35: 314150, .37: max}
    hoh_income_rates = {.1: 14200, .12: 54200, .22: 86350, .24: 164900, .32: 209400, .35: 523600, .37: max}


class Death_and_Taxes_GUIAPP(App):
    pass

Death_and_Taxes_GUIAPP().run()