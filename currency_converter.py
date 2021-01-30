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
        self.label = tk.Label(self, text="Convert currency", font="Arial 20")
        self.label.grid(row=0, column=0, columnspan=4, pady=20)

        self.amount_label = tk.Label(self, text="Amount:", font="Arial 12")
        self.amount_label.grid(row=1, column=0)

        self.currency_label = tk.Label(self, text="Currency:", font="Arial 12")
        self.currency_label.grid(row=1, column=1)

        self.exchange_label = tk.Label(self, text="Exchange to:", font="Arial 12")
        self.exchange_label.grid(row=1, column=2)

        self.amount_entry = tk.Entry(self, font="Arial 12", width=10)
        self.amount_entry.grid(row=2, column=0, padx=10)

        self.currency_entry = tk.Entry(self, font="Arial 12", width=10)
        self.currency_entry.grid(row=2, column=1, padx=10)

        self.exchange_entry = tk.Entry(self, font="Arial 12", width=10)
        self.exchange_entry.grid(row=2, column=2, padx=10)

        self.convert = tk.Button(self, text="Convert", font="Arial 12")
        self.convert.grid(row=2, column=3, padx=10)

        self.current_currency = tk.Entry(self, font="Arial 12", width=10)
        self.current_currency.grid(row=3, column=1, padx=10, pady=10)

        self.exchanged = tk.Entry(self, font="Arial 12", width=10)
        self.exchanged.grid(row=3, column=2, padx=10, pady=10)

root = tk.Tk()
currency_converter = CurrencyConverter(master=root)
currency_converter.mainloop()