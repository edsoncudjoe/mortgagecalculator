# -*- coding:utf-8 -*-

from Tkinter import *
import ttk as tk
import tkMessageBox

class MortgageMonthPay(Frame):
	"""Calculates monthly payments"""

	def __init__(self, master=None):
		Frame.__init__(self, master, relief=FLAT, bd=10)
		self.grid()
		

		# Menu
		self.menubar = Menu(self)
		menu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="File", menu=menu)
		menu.add_command(label="Clear", command=self.clear_text)
		menu.add_command(label="Quit", command=self.quit)

		menu = Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="Help", menu=menu)
		menu.add_command(label="About", command=self.about)

		try:
			self.master.config(menu=self.menubar)
		except AttributeError:
			# master is a toplevel window (Python 1.4/Tkinter 1.63)
			self.master.tk.call(master, "config", "-menu", self.menubar)

		self.create_widgets()

	def get_values(self):
		value = self.hs_val.get().replace(',', '')
		deposit = self.usr_deposit.get().replace(',', '')
		interest = self.interest_ent.get()
		term = self.term_ent.get()
		try:
			self.hs_price = int(value)
			self.usr_dep = int(deposit)
			self.usr_int = float(interest)
			self.usr_term = int(term)
		except ValueError:
			tkMessageBox.showerror("", 
				"Please check that all fields are numbers.")

	def calc_results(self):
		loan = self.hs_price - self.usr_dep
		int_as_decimal = self.usr_int / 100
		int_per_month = int_as_decimal / 12
		total_months = 12 * self.usr_term
		int_over_term = (1 + int_as_decimal / 12) ** total_months
		self.final = loan * ((int_per_month * int_over_term) / 
			(int_over_term - 1))

		self.result.delete(0.0, END)
		self.result.insert(0.0, 
			"Your monthly payments will be approximately £%6.2f " % self.final)

	def monthly_pay(self):
		self.get_values()
		self.calc_results()

	def create_widgets(self):
		# House price
		self.price = tk.Label(self, text="Enter the property value (£):")
		#self.price.config(padx=10)
		self.price.grid(row=0, column=0)

		self.hs_val = StringVar()
		self.price_ent = tk.Entry(self, textvariable=self.hs_val)
		self.price_ent.grid(row=0, column=1)

		# Deposit
		self.deposit = tk.Label(self, text="Enter your deposit amount (£):")
		#self.deposit.config(padx=10)
		self.deposit.grid(row=1, column=0)

		self.usr_deposit = StringVar()
		self.deposit_ent = tk.Entry(self, textvariable=self.usr_deposit)
		self.deposit_ent.config()
		self.deposit_ent.grid(row=1, column=1)

		# Interest
		self.interest = tk.Label(self, 
			text="Enter your bank's interest rate (%):")
		self.interest.config()
		self.interest.grid(row=2, column=0)

		self.interest_ent = StringVar()
		self.interest_entry = tk.Entry(self, textvariable=self.interest_ent)
		self.interest_entry.grid(row=2, column=1)

		# Term
		self.length_of_term = tk.Label(self, 
			text="Enter the length of the mortgage term (years):")
		self.length_of_term.grid(row=3, column=0)

		self.term_ent = StringVar()
		self.term_entry = tk.Entry(self, textvariable=self.term_ent)
		self.term_entry.grid(row=3, column=1)

		# Calculate Button
		#add command to calculate
		self.calculate = tk.Button(self, text="Calculate",
			command=self.monthly_pay)
		self.calculate.grid(row=4, column=1, padx=5, pady=5)

		# Quit Button
		self.quit_app = tk.Button(self, text="Quit", command=self.quit)
		self.quit_app.grid(row=8, column=0, padx=5, pady=5)

		self.clear = tk.Button(self, text="Clear", command=self.clear_text)
		self.clear.grid(row=8, column=1)

		# Result
		self.result = Text(self, x=0, y=50, width=70, height=5, wrap=WORD)
		self.result.grid(row=7, columnspan=2)

	def clear_text(self):
		self.result.delete(0.0, END)

	def about(self):
		tkMessageBox.showinfo("Mortgage Monthly Payment Calculator",
			"\nMortgage Monthly Payment Calculator\n\n"
			"\nCreated by E.Cudjoe"
			"\nVersion 1.0"
			"\nCopyright " + u"\u00A9" + " 2014-2015 E.cudjoe"
			"\nhttps://github.com/edsondudjoe")


root = Tk()
root.title("Mortgage Monthly Payment Calculator")
#root.geometry('525x300+100+100')
#root.configure(background="alice blue")
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
app = MortgageMonthPay(root)
app.grid()

root.mainloop()