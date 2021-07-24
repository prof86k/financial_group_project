import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from bank_database.bank_db import database_file

class DespositMoney:
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.parent.config(background="#068")

        self.account_number = tk.StringVar()
        self.amount = tk.DoubleVar()

        self.account_number_label = tk.Label(master=self.parent, cnf={'text': "Account Number:", 'font': ("Helvatica", 14),
                                                                      'bg': "#068", 'foreground': "#fff"})
        self.account_number_label.grid(
            row=1, column=0, pady=10, padx=20, sticky='w')
        self.account_entry = tk.Entry(master=self.parent, cnf={
                                      'textvariable': self.account_number, 'width': 24, 'font': ("Helvatica", 14)})
        self.account_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        self.account_entry.focus()

        self.amount_label = tk.Label(master=self.parent, cnf={'text': "Amount:", 'font': ("Helvatica", 14),
                                                              'bg': "#068", 'foreground': "#fff"})
        self.amount_label.grid(row=2, column=0, pady=10, padx=20, sticky='w')
        self.amount_entry = tk.Entry(master=self.parent, cnf={
            'textvariable': self.amount, 'width': 24, 'font': ("Helvatica", 14)})
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        self.deposit_btn = tk.Button(self.parent, cnf={'text': "Deposite", "bg": "green", 'foreground': "#fff",
                                                       'activebackground': "green", 'font': ("Helvatica", 14),
                                                       'activeforeground': "#fff", 'command': self._deposite})
        self.deposit_btn.grid(row=3, column=0, columnspan=2, pady=20)

    def _deposite(self):
        'send action'
        acc_no = self.account_number.get()
        amount = self.amount.get()
        if acc_no and amount:
            # send to database
            mbox.showinfo(
                title="success", message=f"An Amount {amount} Has Been Credited Into Account No. {acc_no} ... Thank You.")
            self.parent.withdraw()
        else:
            mbox.showerror(
                title="Error", message="Please ensure all fields are correct.")
            self.parent.withdraw()