import tkinter as tk
from tkinter import ttk

from .deposite_to_account import DespositMoney
from .chech_balance import CheckBalance
from .withdraw_money import WithdrawMoney
from .loans_help import LoanAndAid
from .view_transactions import ViewTranseactions
from .transfer_money import TranferMoney

from bank_database.bank_db import database_file

class CustomerProfile:
    """
    create basic funtionalities of a customer
    """

    def __init__(self, customer_tab, *args, **kwargs):
        self.current_amount = 0.0
        self.customer_tab = customer_tab
        self.customer_frames()

    def customer_frames(self):
        # create customer page on a frame
        tk.Label(master=self.customer_tab, cnf={'text': "CUSTOMER PROFILE.", 'font': ("Helvatica", 18, 'underline'),
                                                'foreground': "#fff", 'bg': "#068"}).pack()
        self.customer_top_frame = tk.Frame(
            master=self.customer_tab, cnf={'bg': "#068"})
        self.customer_top_frame.pack(side='top', fill='x', pady=10, padx=30)

        self.customer_left_side_frame = tk.Frame(
            master=self.customer_tab, cnf={'bg': '#068'})
        self.customer_left_side_frame.pack(side='left', fill='y', padx=30)

        self.customer_right_side_frame = tk.Frame(
            master=self.customer_tab, cnf={'bg': '#068'})
        self.customer_right_side_frame.pack(side='right', fill='y', padx=30)

        self.deposite_btn = tk.Button(master=self.customer_top_frame, cnf={'text': "Deposite Account ", 'bg': "green",
                                                                           'font': ('Helvatica', 13),
                                                                           'foreground': "#fff", 'activebackground': "green",
                                                                           'activeforeground': "#fff", 'height': 5,
                                                                           'command': self._deposite_money})
        self.deposite_btn.pack(pady=20, side='left', padx=50)

        self.check_balance_btn = tk.Button(master=self.customer_top_frame, cnf={'text': "Check Balance", 'bg': "green",
                                                                                'font': ('Helvatica', 13),
                                                                                'foreground': "#fff", 'activebackground': "green",
                                                                                'activeforeground': "#fff", 'height': 5, 'command': self._check_balance})
        self.check_balance_btn.pack(pady=50, side='right', padx=50)

        self.withdraw_money_btn = tk.Button(master=self.customer_right_side_frame, cnf={'text': "WithDraw Cash", 'bg': "green",
                                                                                        'font': ('Helvatica', 13),
                                                                                        'foreground': "#fff", 'activebackground': "green",
                                                                                        'activeforeground': "#fff", 'height': 5, 'command': self._withdraw})
        self.withdraw_money_btn.pack(pady=50, padx=50)

        self.transfer_money_btn = tk.Button(master=self.customer_right_side_frame, cnf={'text': "Transfer Money", 'bg': "green",
                                                                                        'font': ('Helvatica', 13),
                                                                                        'foreground': "#fff", 'activebackground': "green",
                                                                                        'activeforeground': "#fff", 'height': 5,'command':self._transfer_money})
        self.transfer_money_btn.pack(pady=50, padx=50)

        self.take_loan_money_btn = tk.Button(master=self.customer_left_side_frame, cnf={'text': "Loans And help", 'bg': "green",
                                                                                        'font': ('Helvatica', 13),
                                                                                        'foreground': "#fff", 'activebackground': "green",
                                                                                        'activeforeground': "#fff", 'height': 5,'command':self._take_loan_pay})
        self.take_loan_money_btn.pack(pady=50, padx=50)

        self.view_transaction_btn = tk.Button(master=self.customer_left_side_frame, cnf={'text': "View Transactions", 'bg': "green",
                                                                                       'font': ('Helvatica', 13),
                                                                                       'foreground': "#fff", 'activebackground': "green",
                                                                                       'activeforeground': "#fff", 'height': 5,'command':self._view_transactions})
        self.view_transaction_btn.pack(pady=50, padx=50)

    def _deposite_money(self):
        # call deposite file
        top = tk.Toplevel()
        DespositMoney(top)
        top.resizable(height=0, width=0)

    def _check_balance(self):
        "return the current amount in the account"
        top = tk.Toplevel()
        CheckBalance(top)
        top.resizable(width=0, height=0)
        top.title("Check Balance")

    def _transfer_money(self):
        "if the two accounts exists then send the money"
        top = tk.Toplevel()
        TranferMoney(top)
        top.resizable(width=0, height=0)
        top.title("Transfer Money")

    def _withdraw(self):
        "remove some amount from the account"
        top = tk.Toplevel()
        WithdrawMoney(top)
        top.resizable(width=0, height=0)
        top.title("Withdraw From Account.")
        top.config(background="#068")

    def _take_loan_pay(self):
        "take a loan from the bank"
        top = tk.Toplevel()
        LoanAndAid(top)
        top.title("Take Loan")
        top.resizable(width=0, height=0)

    def _view_transactions(self):
        "pay back loan to the bank"
        top = tk.Toplevel()
        ViewTranseactions(top)
        top.resizable(width=0, height=0)
        top.title("View Transaction")