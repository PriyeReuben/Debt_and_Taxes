from kivy.app import App


salary=float(input("What is your salary?"))
max = salary *2
your_bracket ={} #this should be empty
taxable = []

single_income_rates={.1: 9950, .12: 40525, .22:86375, .24:164925, .32:209425, .35:523600, .37:max}
married_jointly_income_rates={.1: 19900, .12:81050, .22:172750, .24:329850, .32:418850, .35:628300, .37:max}
married_separately_income_rates={.1: 9950, .12: 40525, .22:86375, .24:164925, .32:209425, .35:314150, .37:max}
hoh_income_rates={.1: 14200, .12: 54200, .22:86350, .24:164900, .32:209400, .35:523600, .37:max}



while True:
    bracket = int(input(
        "How are you filing?\n"
        "1) Single\n"
        "2) Married jointly\n"
        "3) married separately\n"
        "4) Head of Household\n"
    ))
    if bracket == 1:
        your_bracket=single_income_rates
        break
    elif bracket ==2:
        your_bracket = married_jointly_income_rates
        break
    elif bracket == 3:
        your_bracket = married_separately_income_rates
        break
    elif bracket == 4:
        your_bracket = hoh_income_rates
        break
    else:
        print("Please select 1,2,3, or 4.  In this house, we use the Oxford comma.")##


working_salary = salary

for x in your_bracket:
    if working_salary > 0:
        if working_salary <= your_bracket[x]:
            taxable.append(working_salary*x)
            #print(taxable)
            break
        else:
            taxable.append(your_bracket[x] * x)
            working_salary = working_salary - your_bracket[x]
    else:
        taxable.append(0)
        print("Sir, this is a capitalist society.")
        break

federal_tax = sum(taxable)
state_tax = salary * .0478
total_tax = federal_tax+state_tax

effective_federal_tax_rate = federal_tax/salary*100
effective_state_tax_rate = 4.87
effective_totat_tax_rate = total_tax/salary*100

total_take_home = salary - state_tax - federal_tax
weekly_pay = total_take_home/52
hourly_pay = weekly_pay/40


print(
    "Federal tax paid:__$"+ str(federal_tax) +"\n"
    "Effective federal tax rate:__%"+ str(effective_federal_tax_rate) +"\n"
            "------------------\n"                                                           
    "State tax paid:__$"+ str(state_tax) +"\n"
    "Effective state tax rate:__%"+ str(effective_state_tax_rate) +"\n" 
            "------------------\n"         
    "Total tax paid:__$" + str(total_tax) +"\n" 
    "Effective total tax rate:__$" + str(effective_totat_tax_rate) +"\n"                                       
    "Take-home pay:__$"+ str(total_take_home) +"\n"
    "Weekly pay:__$"+ str(weekly_pay) +"\n"
    "Hourly pay:__$" + str(hourly_pay) + "\n"

    )