import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import filedialog as fd

import tempfile
import os
# import win32.win32api as mp


from bank_database.bank_db import database_file


class WithdrawMoney:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.account_id = tk.StringVar()
        self.withdraw_amount = tk.DoubleVar()
        self.account_id_label = tk.Label(master=self.parent, cnf={'text': "Account Number:", 'font': ("Helvatica", 14, 'bold'),
                                                                  'foreground': "#fff", 'bg': "#068"})
        self.account_id_label.grid(
            row=1, column=0, padx=20, pady=20, sticky='w')
        self.account_id_entry = tk.Entry(master=self.parent, cnf={
                                         'textvariable': self.account_id, 'font': ("Helvatica", 14), 'width': 24})
        self.account_id_entry.grid(
            row=1, column=1, padx=10, pady=20, sticky='w')

        self.amount_label = tk.Label(master=self.parent, cnf={'text': "Amount:", 'font': ("Helvatica", 14, 'bold'),
                                                              'foreground': "#fff", 'bg': "#068"})
        self.amount_label.grid(row=1, column=2, padx=20, pady=20, sticky='w')
        self.amount_entry = tk.Entry(master=self.parent, cnf={
                                     'textvariable': self.withdraw_amount, 'font': ("Helvatica", 14), 'width': 24})
        self.amount_entry.grid(row=1, column=3, padx=10, pady=20, sticky='w')

        self.withdraw_btn = tk.Button(master=self.parent, cnf={'text': "Withdraw", 'font': ("Helvatica", 14),
                                                               'foreground': "#fff", 'bg': "green", 'activeforeground': "#fff",
                                                               'activebackground': "green", 'command': self._width_action})
        self.withdraw_btn.grid(row=1, column=4, padx=10, pady=20, sticky='w')

        self.scroll_text_frame = tk.Frame(master=parent, cnf={'bg': "#068"})
        self.scroll_text_frame.grid(
            row=2, column=0, padx=10, pady=30, columnspan=5)
        # ===================== call methods================================
        self.display_withdraw_message()
        self.print_text_btn()

    def display_withdraw_message(self):
        self.withdraw_info = tk.Text(master=self.scroll_text_frame, cnf={'wrap': "word", 'font': ("Helvatica", 14),
                                                                         'foreground': "#013", 'height': 10, 'padx': 14, 'pady': 10})
        self.withdraw_info.pack(side='left')

        self.scroll = tk.Scrollbar(master=self.scroll_text_frame, cnf={
                                   'orient': "vertical", 'command': self.withdraw_info.yview})
        self.scroll.pack(side='right', fill='y')
        self.withdraw_info.config(yscrollcommand=self.scroll.set)

    def print_text_btn(self):
        "button for printing of the cash out information"
        self.print_btn = tk.Button(master=self.parent, cnf={'text': "Print Reciept", 'font': ("Helvatica", 16),
                                                            'activebackground': "#900", 'bg': "#a11",
                                                            'foreground': "#fff", 'activeforeground': "#FFF",
                                                            'command': self._print_receipt})
        self.print_btn.grid(row=3, column=2, pady=15)

    def _width_action(self):
        "triggered for with draw action in the account"
        number = self.account_id.get()
        amount = self.withdraw_amount.get()
        # retrive from database
        # populate in the text widget
        self.account_id_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def _print_receipt(self):
        "print the receipt"
        file_text = self.withdraw_info.get('1.0', tk.END+"-1c")
        try:
            filename = tempfile.mktemp('.txt')

            open(filename, 'w').write(file_text)
            # with open('fees_report_reciept.txt', 'w+', encoding='utf-8') as fs:
            # fs.write(file_text)
            # dir = os.getcwd()
            # file = fd.askopenfilename(initialdir=dir, title="Select any file", filetypes=(
            # ("Text files", "*.txt"), ("all files", "*.*")))
            # if file:
            mp.ShellExecute(0, 'Choose a File', filename, None, ".", 0)
            print("printer not found")
        except Exception as e:
            print("this one")
            filename = tempfile.mktemp('.txt')
            open(filename, 'w').write(file_text)
            os.startfile(filename, 'print')