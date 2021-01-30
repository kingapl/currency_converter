import tkinter as tk

class CurrencyConverter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Currency Converter")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass

root = tk.Tk()
currency_converter = CurrencyConverter(master=root)
currency_converter.mainloop()