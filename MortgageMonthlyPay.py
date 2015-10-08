# -*- coding:utf-8 -*-

import Tkinter as tk
import ttk
import tkMessageBox


class MortgageMonthPay(tk.Frame):
    """Calculates monthly payments"""

    def __init__(self, master=None):
        tk.Frame.__init__(self, master, relief=tk.FLAT, bd=10)
        self.grid()

        self.house_price = None
        self.deposit = None
        self.interest = None
        self.term = None

        self.house_value = tk.StringVar()
        self.user_deposit = tk.StringVar()
        self.interest_rate = tk.StringVar()
        self.term_length = tk.StringVar()

        self.house_price_label = ttk.Label(self, text="Enter the property "
                                                      "value (£):")
        self.house_price_entry = ttk.Entry(self, textvariable=self.house_value)
        self.deposit_label = ttk.Label(self,
                                       text="Enter your deposit amount (£):")
        self.deposit_entry = ttk.Entry(self, textvariable=self.user_deposit)
        self.interest_rate_label = ttk.Label(self, text="Enter your bank's "
                                                        "interest rate (%):")
        self.interest_rate_entry = ttk.Entry(self,
                                             textvariable=
                                             self.interest_rate)
        self.payment_term_label = ttk.Label(self, text="Enter the length of "
                                                       "the mortgage term "
                                                       "(years):")
        self.payment_term_entry = ttk.Entry(self,
                                            textvariable=self.term_length)
        self.calculate = ttk.Button(self, text="Calculate",
                                    command=self.monthly_pay)
        self.quit_app = ttk.Button(self, text="Quit", command=self.quit)
        self.clear = ttk.Button(self, text="Clear", command=self.clear_text)
        self.result = tk.Text(self, x=0, y=50, width=70, height=5,
                              wrap=tk.WORD)

        self.house_price_label.grid(row=0, column=0)
        self.house_price_entry.grid(row=0, column=1)
        self.deposit_label.grid(row=1, column=0)
        self.deposit_entry.grid(row=1, column=1)
        self.interest_rate_label.grid(row=2, column=0)
        self.interest_rate_entry.grid(row=2, column=1)
        self.payment_term_label.grid(row=3, column=0)
        self.payment_term_entry.grid(row=3, column=1)
        self.calculate.grid(row=4, column=1, padx=5, pady=5)
        self.quit_app.grid(row=8, column=0, padx=5, pady=5)
        self.clear.grid(row=8, column=1)
        self.result.grid(row=7, columnspan=2)

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

    def get_values(self):
        """Collect inputs from GUI"""
        try:
            self.house_price = int(self.house_value.get().replace(',', ''))
            self.deposit = int(self.user_deposit.get().replace(',', ''))
            self.interest = float(self.interest_rate.get())
            self.term = int(self.term_length.get())
        except ValueError:
            tkMessageBox.showerror("",
                                   "Please check that all fields are numbers.")

    def calc_results(self):
        try:
            if self.deposit >= self.house_price:
                tkMessageBox.showinfo("", "The deposit exceeds or is equal to "
                                          "the house value. You won't need a "
                                          "mortgage.")
            else:
                if self.term > 60:
                    raise OverflowError
                else:
                    loan = self.house_price - self.deposit
                    int_as_decimal = self.interest / 100
                    int_per_month = int_as_decimal / 12
                    total_months = 12 * self.term
                    int_over_term = (1 + int_as_decimal / 12) ** total_months
                    self.final = loan * ((int_per_month * int_over_term) /
                                         (int_over_term - 1))

                    self.result.delete(0.0, tk.END)
                    self.result.insert(0.0,
                                       "House price: £%d\n"
                                       "Deposit: £%d\n"
                                       "Interest rate: %2.2f%%\n"
                                       "Your monthly payments will be "
                                       "approximately £%6.2f "
                                       % (self.house_price, self.deposit,
                                          self.interest, self.final))
        except AttributeError:
            print("Not all user-fields were completed."
                  "\nUnable to complete process")
        except OverflowError:
            tkMessageBox.showerror("",
                                   "You probably won't live for another %d "
                                   "years."
                                   "\nUse a more realistic mortgage term." %
                                   self.term)

    def monthly_pay(self):
        self.get_values()
        self.calc_results()

    def clear_text(self):
        self.result.delete(0.0, tk.END)

    def about(self):
        tkMessageBox.showinfo("Mortgage Monthly Payment Calculator",
                              "\nMortgage Monthly Payment Calculator\n\n"
                              "\nCreated by E.Cudjoe"
                              "\nVersion 1.0"
                              "\nCopyright " + u"\u00A9" + " 2014-2015 "
                                                           "E.Cudjoe"
                                                           "\nhttps://"
                                                           "github.com/"
                                                           "edsoncudjoe")


root = tk.Tk()
root.title("Mortgage Monthly Payment Calculator")
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
app = MortgageMonthPay(root)
app.grid()

root.mainloop()
