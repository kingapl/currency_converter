import tkinter as tk
from tkinter import ttk

import requests

url = 'https://api.frankfurter.app/currencies'
response = requests.get(url)
currencies_dict = response.json()
currencies = []

for currency in currencies_dict.keys():
    currencies.append(currency)


class CurrencyConverter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x300")
        self.master.title("Currency Converter")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Convert currency", font="Arial 20")
        self.label.grid(row=0, column=0, columnspan=4, pady=20)

        self.amount_label = tk.Label(self, text="Amount:", font="Arial 12")
        self.amount_label.grid(row=1, column=0)
        self.amount_var = tk.DoubleVar()
        self.amount_entry = tk.Entry(self, text=self.amount_var, 
                                    font="Arial 12", width=10)
        self.amount_entry.grid(row=2, column=0, padx=10)

        self.currency_label = tk.Label(self, text="Currency:", font="Arial 12")
        self.currency_label.grid(row=1, column=1)
        self.currency = tk.StringVar()
        self.choose_currency = ttk.Combobox(self, textvariable=self.currency, 
                                    font="Arial 12", width=10)
        self.choose_currency['values'] = (currencies)
        self.choose_currency.grid(row=2, column=1, padx=10)

        self.exchange_label = tk.Label(self, text="Exchange to:", 
                                    font="Arial 12")
        self.exchange_label.grid(row=1, column=2)
        self.exchange = tk.StringVar()
        self.exchange_to = ttk.Combobox(self, textvariable=self.exchange, 
                                    font="Arial 12", width=10)
        self.exchange_to['values'] = (currencies)
        self.exchange_to.grid(row=2, column=2, padx=10)

        self.convert = tk.Button(self, text="Convert", command=self.convert, 
                                font="Arial 12")
        self.convert.grid(row=2, column=3, padx=10)

        self.current_currency_var = tk.StringVar()
        self.current_currency = tk.Entry(self, text=self.current_currency_var, 
                                    font="Arial 12", width=10)
        self.current_currency.grid(row=3, column=1, padx=10, pady=10)

        self.exchanged_var = tk.StringVar()
        self.exchanged = tk.Entry(self, text=self.exchanged_var, 
                                    font="Arial 12", width=10)
        self.exchanged.grid(row=3, column=2, padx=10, pady=10)

    def convert(self):
        amount = self.amount_var.get()
        currency = self.currency.get()
        exchange = self.exchange.get()
        print(amount)
        print(currency)
        print(exchange)

        convert_url = f'https://api.frankfurter.app/latest?amount={amount}&from={currency}&to={exchange}'
        convert_response = requests.get(convert_url)
        convert_dict = convert_response.json()
        rates = convert_dict['rates']
        exchange_value = rates[exchange]

        self.current_currency_var.set(f"{amount} {currency}")
        self.exchanged_var.set(f"{exchange_value} {exchange}")


root = tk.Tk()
currency_converter = CurrencyConverter(master=root)
currency_converter.mainloop()