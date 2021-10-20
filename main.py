from kivy.app import App
from kivy.properties import StringProperty, AliasProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
import matplotlib.pyplot as plt
from datetime import datetime

class DaTApp(BoxLayout):
    #salary = float(input("What is your salary?"))
    salary = 0 #delete this later
    max = salary * 2
    your_bracket = {}  # this should be empty
    taxable = []

    image_source = StringProperty('chart.png')
    image_name = ""

    now = datetime.now()

    single_income_rates = {.1: 9950, .12: 40525, .22: 86375, .24: 164925, .32: 209425, .35: 523600, .37: max}
    married_jointly_income_rates = {.1: 19900, .12: 81050, .22: 172750, .24: 329850, .32: 418850, .35: 628300, .37: max}
    married_separately_income_rates = {.1: 9950, .12: 40525, .22: 86375, .24: 164925, .32: 209425, .35: 314150, .37: max}
    hoh_income_rates = {.1: 14200, .12: 54200, .22: 86350, .24: 164900, .32: 209400, .35: 523600, .37: max}



    def on_calculate_clicked(self):
        #print("Calculate Federal Taxes for {} salary when {}".format())
        self.generate_graph_image()
        #self.image_source = StringProperty('chart.png')
        print(str(self.now))
        self.update_image()


    def spinner_selection(self, value):
        print("You selected {}".format(value))

    def generate_graph_image(self):
        x = ["Salary", "Total Tax"]
        y = [self.salary, self.salary/2]
        plt.ylim(0,self.max) #set y-axis maximum to double salary
        plt.bar(x, y)

        self.now = datetime.now() #get the current datetime
        text_now = str(self.now)
        text_now = text_now[-6:]

        image_name = '{}.png'.format(text_now)
        plt.savefig(image_name) #save truncated datetime as image name

        print("new image generated.")

    def update_image(self):
        #self.image_source = self.image_name
        reload = self.ids.image_id
        reload.reload()

    def process_salary_text(self, text):
        #this can be bypassed by passing text_input_id.text in the .kv file
        #text = self.ids.text_input_id.text #i don't understand why this works, but it does.
        print(text)
        self.salary = float(text)


class Death_and_Taxes_GUIAPP(App):
    pass

Death_and_Taxes_GUIAPP().run()