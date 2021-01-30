import tkinter as tk

class CurrencyConverter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x300")
        self.master.title("Currency Converter")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Convert currency")
        self.label.grid(row=0, column=0, columnspan=4)

        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.grid(row=1, column=0)

        self.currency_label = tk.Label(self, text="Currency:")
        self.currency_label.grid(row=1, column=1)

        self.exchange_label = tk.Label(self, text="Exchange to:")
        self.exchange_label.grid(row=1, column=2)

        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=2, column=0)

        self.currency_entry = tk.Entry(self)
        self.currency_entry.grid(row=2, column=1)

        self.exchange_entry = tk.Entry(self)
        self.exchange_entry.grid(row=2, column=2)

        self.convert = tk.Button(self, text="Convert")
        self.convert.grid(row=2, column=3)

        self.current_currency = tk.Entry(self)
        self.current_currency.grid(row=3, column=1)

        self.exchanged = tk.Entry(self)
        self.exchanged.grid(row=3, column=2)

root = tk.Tk()
currency_converter = CurrencyConverter(master=root)
currency_converter.mainloop()