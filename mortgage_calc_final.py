# -*- coding: utf-8 -*-
class Calc(object):

    def __init__(self, value, deposit, interest, term):
        self.value = value
        self.deposit = deposit
        self.interest = interest
        self.term = term
    
    def monthly_payments(self):
    	loan = self.value - self.deposit
        interest_as_decimal = self.interest / 100
        interest_per_month = interest_as_decimal / 12
        total_in_months = 12 * self.term
        interest_over_term = (1 + interest_as_decimal / 12) ** total_in_months
        
        a = loan * ((interest_per_month * interest_over_term) / 
                        (interest_over_term - 1))
        
        print("The monthly payments will be £{0:,.2f}".format(a))
        return a

    def total_amount_paid(self):
        loan = self.value - self.deposit
    	total_in_months = 12 * self.term
        interest_as_decimal = self.interest / 100
        interest_per_month = interest_as_decimal / 12
        interest_over_term = (1 + interest_as_decimal / 12) ** total_in_months
    	
        pay_per_month = loan * ((interest_per_month * interest_over_term) / 
                        (interest_over_term - 1))
        
        total_amount_paid = pay_per_month * total_in_months
        print("The total amount paid at the end of your mortgage: £{0:,.2f}"
                .format(total_amount_paid))
        
        return total_amount_paid


    # This currently works by running the total amount paid method and 
    # then using its output to calculate the total interest paid.
    def total_interest_paid(self, fnc):
        loan = self.value - self.deposit
        total_interest_paid = fnc - loan
        print("The total amount of interest paid over {} years: £{:,.2f}."
                .format(self.term, total_interest_paid))
    	
value_store = {
    'value': None,
    'deposit': None,
    'interest': None,
    'term': None
    }

questions = True
while questions:
    try:
        if not value_store['value']:
            value_store['value'] = int(raw_input(
                "Enter the property value (£): ").replace(',', ''))
        if not value_store['deposit']:
            value_store['deposit'] = int(raw_input(
                "Enter your deposit amount (£): ").replace(',', ''))
        if not value_store['interest']:
            value_store['interest'] = float(raw_input(
                "Enter your bank's interest rate (%): "))
        if not value_store['term']:
            value_store['term'] = int(raw_input(
                "Enter the length of mortgage term (years): "))
        
        user = Calc(**value_store)

             
        print("select {0:1} to calculate your monthly mortgage payments"
            .format(1))
        print("select {0:1} to calculate the total amount you will pay."
            .format(2))
        print("select {0:1} to calculate the total interest you will pay"
            .format(3))
        print("select {0:1} to quit".format("q"))
        
        userchoice = raw_input("please select from above: ")

        if userchoice == "1":
            user.monthly_payments()
        elif userchoice == "2":
            user.total_amount_paid()
        elif userchoice == "3":
            user.total_interest_paid(user.total_amount_paid())
        elif userchoice == "q":
            questions = False
        else:
            print("I dont have that option available.")
        
        
        end_calc = raw_input("Would you like to continue? [y/n]: ")
        if end_calc == "n":
            print("Goodbye") 
            questions = False
        elif end_calc == "y":
            questions = True
        else:
            questions = True
    except ValueError:
        print("Oops! I expected a number there.") 



