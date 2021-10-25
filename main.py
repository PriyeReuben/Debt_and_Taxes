from kivy.app import App
from kivy.properties import StringProperty, AliasProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import matplotlib.pyplot as plt


class DaTApp(BoxLayout):

    salary = 0
    max = 10000000000000000000
    your_bracket = {}  # this should be empty
    federal_tax = 0
    image_source = StringProperty('blank.jpg')
    image_name = ""
    salary_str = StringProperty("")
    federal_tax_str = StringProperty("")
    effective_tax_rate_str = StringProperty("")

    single_income_rates = {.1: 9950, .12: 40525, .22: 86375, .24: 164925, .32: 209425, .35: 523600, .37: max}
    married_jointly_income_rates = {.1: 19900, .12: 81050, .22: 172750, .24: 329850, .32: 418850, .35: 628300, .37: max}
    married_separately_income_rates = {.1: 9950, .12: 40525, .22: 86375, .24: 164925, .32: 209425, .35: 314150, .37: max}
    hoh_income_rates = {.1: 14200, .12: 54200, .22: 86350, .24: 164900, .32: 209400, .35: 523600, .37: max}



    def on_calculate_clicked(self):
        self.calculate_fed_tax()
        self.generate_graph_image()
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
        x = ["Salary\n" + self.salary_str, "Total Fed Tax\n" + self.federal_tax_str]
        y = [self.salary, self.federal_tax]
        plt.ylabel("Dollars")
        plt.title("Salary vs Actual Federal Tax")
        plt.bar(x, y)

        #save graph as new image
        self.image_name = "results.jpg"
        plt.savefig(self.image_name)
        plt.clf()  #clear matplotlib buffer.  Do this.

        #print("new image generated.")

    def update_image(self):
        self.ids.image_id.source = self.image_name
        self.ids.image_id.reload()



    def process_salary_text(self, widget):
        self.salary = float(widget.text)
        print(self.salary)

    def calculate_fed_tax(self):

        taxable = []
        working_salary = self.salary

        # make it so that the max value in your_bracket is salary * 2
        #self.your_bracket[.37] = self.salary * 2 # this breaks my code.
        #print("New max: "+ str(self.your_bracket[.37]))


        for x in self.your_bracket:
            if working_salary > 0:
                if working_salary <= self.your_bracket[x]:
                    taxable.append(working_salary * x)
                    break
                else:
                    taxable.append(self.your_bracket[x] * x)
                    working_salary = working_salary - self.your_bracket[x]
            else:
                taxable.append(0)
                print("Sir, this is a capitalist society.")
                break

        self.federal_tax = sum(taxable) # + (self.salary * .0765)  # .0765 = FICA


        self.salary_str = "$" + str(self.salary)
        self.federal_tax_str = "$" + str(self.federal_tax)
        self.effective_tax_rate_str = "%" + str(float(self.federal_tax) / float(self.salary) * 100)
        print("Your Salary: {} \n".format(self.salary_str) +
              "Your Federal Taxes: {} \n".format(self.federal_tax_str) +
              "Your Effective Federal Tax Rate: {}".format(self.effective_tax_rate_str))



class Death_and_Taxes_GUIAPP(App):
    pass

Death_and_Taxes_GUIAPP().run()