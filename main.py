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
import os

class DaTApp(BoxLayout):
    #salary = float(input("What is your salary?"))
    salary = 0 #delete this later
    max = salary * 2
    your_bracket = {}  # this should be empty
    federal_tax = 0


    image_source = StringProperty('blank.jpg')
    image_name = ""

    now = datetime.now()

    single_income_rates = {.1: 9950, .12: 40525, .22: 86375, .24: 164925, .32: 209425, .35: 523600, .37: max}
    married_jointly_income_rates = {.1: 19900, .12: 81050, .22: 172750, .24: 329850, .32: 418850, .35: 628300, .37: max}
    married_separately_income_rates = {.1: 9950, .12: 40525, .22: 86375, .24: 164925, .32: 209425, .35: 314150, .37: max}
    hoh_income_rates = {.1: 14200, .12: 54200, .22: 86350, .24: 164900, .32: 209400, .35: 523600, .37: max}



    def on_calculate_clicked(self):
        self.calculate_fed_tax()
        self.generate_graph_image()
        print(str(self.now))
        self.update_image()


    def spinner_selection(self, value):
        print("You selected {}".format(value))

        if value == "Single":
            self.your_bracket = self.single_income_rates
        elif value == "Married Jointly":
            self.your_bracket = self.married_jointly_income_rates
        elif value == "Married Separately":
            self.your_bracket = self.married_separately_income_rates
        elif value == "Head of Household":
            self.your_bracket = self.hoh_income_rates
        else:
            self.your_bracket = self.single_income_rates

    def generate_graph_image(self):
        #create a bar graph
        x = ["Salary", "Total Tax"]
        y = [self.salary, self.federal_tax]
        x0=0
        y0=0
        #self.max = self.salary *2
        #plt.ylim(0,self.max) #set y-axis maximum to double salary
        plt.bar(x, y)

        #generate new image name
        self.now = datetime.now() #get the current datetime
        text_now = str(self.now)
        text_now = text_now.replace('.','') #get rid of periods
        text_now = text_now.replace(':', '') #get rid of colons

        #save plot as new image
        #self.image_name = '{}.jpg'.format(text_now)
        self.image_name = "results.jpg"
        plt.savefig(self.image_name)
        plt.clf()

        print("new image generated.")

    def update_image(self):
        #print("Image name:" + self.image_name)
        #self.image_source = StringProperty(self.image_name)
        self.ids.image_id.source = self.image_name
        self.ids.image_id.reload()
        #os.remove(self.image_name)



    def process_salary_text(self, widget):
        #this can be bypassed by passing text_input_id.text in the .kv file
        #text = self.ids.text_input_id.text #i don't understand why this works, but it does.
        self.salary = float(widget.text)
        print(self.salary)

    def calculate_fed_tax(self):

        taxable = []
        working_salary = self.salary


        for x in self.your_bracket:
            if working_salary > 0:
                if working_salary <= self.your_bracket[x]:
                    taxable.append(working_salary * x)
                    # print(taxable)
                    break
                else:
                    taxable.append(self.your_bracket[x] * x)
                    working_salary = working_salary - self.your_bracket[x]
            else:
                taxable.append(0)
                print("Sir, this is a capitalist society.")
                break
        self.federal_tax = sum(taxable)
        #effective_federal_tax_rate = federal_tax / salary * 100

        print("Federal tax: " + str(self.federal_tax))



class Death_and_Taxes_GUIAPP(App):
    pass

Death_and_Taxes_GUIAPP().run()