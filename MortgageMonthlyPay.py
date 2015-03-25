# -*- coding:utf-8 -*-

import Tkinter as tk
import ttk 
import tkMessageBox

class MortgageMonthPay(tk.Frame):
	"""Calculates monthly payments"""

	def __init__(self, master=None):
		tk.Frame.__init__(self, master, relief=tk.FLAT, bd=10)
		self.grid()
		

		# Menu
		self.menubar = tk.Menu(self)
		menu = tk.Menu(self.menubar, tearoff=0)
		self.menubar.add_cascade(label="File", menu=menu)
		menu.add_command(label="Clear", command=self.clear_text)
		menu.add_command(label="Quit", command=self.quit)

		menu = tk.Menu(self.menubar, tearoff=0)
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
		try:
			if self.usr_dep >= self.hs_price:
				tkMessageBox.showinfo("", "The deposit exceeds or is equal to "
					"the house value. You won't need a mortgage.")
			else:
				if self.usr_term > 60:
					raise OverflowError
				else:
					loan = self.hs_price - self.usr_dep
					int_as_decimal = self.usr_int / 100
					int_per_month = int_as_decimal / 12
					total_months = 12 * self.usr_term
					int_over_term = (1 + int_as_decimal / 12) ** total_months
					self.final = loan * ((int_per_month * int_over_term) / 
						(int_over_term - 1))

					self.result.delete(0.0, tk.END)
					self.result.insert(0.0, 
						"House price: £%d\n"
						"Deposit: £%d\n"
						"Interest rate: %2.2f%%\n"
						"Your monthly payments will be approximately £%6.2f " 
						% (self.hs_price, self.usr_dep, self.usr_int, self.final))
		except AttributeError:
			print("Not all user-fields were completed."
				"\nUnable to complete process")
		except OverflowError:
			tkMessageBox.showerror("", "You probably won't live for another %d years."
				"\nUse a more realistic mortgage term." % self.usr_term)

	def monthly_pay(self):
		self.get_values()
		self.calc_results()

	def create_widgets(self):
		# House price
		self.price = ttk.Label(self, text="Enter the property value (£):")
		#self.price.config(padx=10)
		self.price.grid(row=0, column=0)

		self.hs_val = tk.StringVar()
		self.price_ent = ttk.Entry(self, textvariable=self.hs_val)
		self.price_ent.grid(row=0, column=1)

		# Deposit
		self.deposit = ttk.Label(self, text="Enter your deposit amount (£):")
		#self.deposit.config(padx=10)
		self.deposit.grid(row=1, column=0)

		self.usr_deposit = tk.StringVar()
		self.deposit_ent = ttk.Entry(self, textvariable=self.usr_deposit)
		self.deposit_ent.config()
		self.deposit_ent.grid(row=1, column=1)

		# Interest
		self.interest = ttk.Label(self, 
			text="Enter your bank's interest rate (%):")
		self.interest.config()
		self.interest.grid(row=2, column=0)

		self.interest_ent = tk.StringVar()
		self.interest_entry = ttk.Entry(self, textvariable=self.interest_ent)
		self.interest_entry.grid(row=2, column=1)

		# Term
		self.length_of_term = ttk.Label(self, 
			text="Enter the length of the mortgage term (years):")
		self.length_of_term.grid(row=3, column=0)

		self.term_ent = tk.StringVar()
		self.term_entry = ttk.Entry(self, textvariable=self.term_ent)
		self.term_entry.grid(row=3, column=1)

		# Calculate Button
		#add command to calculate
		self.calculate = ttk.Button(self, text="Calculate",
			command=self.monthly_pay)
		self.calculate.grid(row=4, column=1, padx=5, pady=5)

		# Quit Button
		self.quit_app = ttk.Button(self, text="Quit", command=self.quit)
		self.quit_app.grid(row=8, column=0, padx=5, pady=5)

		self.clear = ttk.Button(self, text="Clear", command=self.clear_text)
		self.clear.grid(row=8, column=1)

		# Result
		self.result = tk.Text(self, x=0, y=50, width=70, height=5, wrap=tk.WORD)
		self.result.grid(row=7, columnspan=2)

	def clear_text(self):
		self.result.delete(0.0, tk.END)

	def about(self):
		tkMessageBox.showinfo("Mortgage Monthly Payment Calculator",
			"\nMortgage Monthly Payment Calculator\n\n"
			"\nCreated by E.Cudjoe"
			"\nVersion 1.0"
			"\nCopyright " + u"\u00A9" + " 2014-2015 E.cudjoe"
			"\nhttps://github.com/edsondudjoe")


root = tk.Tk()
root.title("Mortgage Monthly Payment Calculator")
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
app = MortgageMonthPay(root)
app.grid()

root.mainloop()