import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox


class DailyTransactions:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        self.frame = tk.Frame(master=self.parent, cnf={'bg': "#068"})
        self.frame.pack(pady=20)

        tk.Label(master=self.frame, cnf={'text': "VIEWING TODAY'S TRANSACTIONS IN THE BANK",
                                         'font': ("Helvatica", 16, 'underline'), 'foreground': "#fff", 'bg': "#068"}
                 ).pack(pady=10)

        self.tree = ttk.Treeview(master=self.frame, selectmode="browse")
        self.tree['column'] = ('1', '2', '3')
        self.tree['show'] = "headings"
        self.tree.heading('#1', text="Account No.")
        self.tree.heading('#2', text="Amount")
        self.tree.heading('#3', text='Transaction Type')
        self.tree.pack(side='left', fill='x', expand=1)

        self.scrollbar = tk.Scrollbar(master=self.frame, cnf={
                                      'orient': "vertical", 'command': self.tree.yview})
        self.scrollbar.pack(side='right', fill='y')

        self.tree.config(yscrollcommand=self.scrollbar.set)

    def close_daily(self):
        'close the frame of daily transactions'
        self.frame.destroy()