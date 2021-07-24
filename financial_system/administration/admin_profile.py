import tkinter as tk
from tkinter import ttk

from customer.create_account import CreateCustomerAccount
from .set_bank import Bank
from .view_customers import AllCustomers
from .view_daily_transactions import DailyTransactions


from bank_database.bank_db import database_file


class AdminProfile:
    """ 
    This page show the basic information about the bank
    1. this shows transactions made in a date and the number
    2. total money in the bank
    3. link to register new customer

    """

    def __init__(self, profile_tab, *args, **kwargs):
        super(AdminProfile, self).__init__(*args, **kwargs)
        self.profile_tab = profile_tab
        self.set_bank = False
        self.view_once = False
        self.dialy_trans = False

        self.top_frame = tk.Frame(master=self.profile_tab, cnf={'bg': "#068"})
        self.top_frame.pack(fill='y', side='left', pady=0)

        self.canvas_profile = tk.Canvas(master=self.top_frame, cnf={
            'bg': "#068", 'borderwidth': 0, 'bd': 0, 'width': 250, 'confine': False})

        self.frame_profile = tk.Frame(
            master=self.canvas_profile, cnf={'bg': "#068"})
        scrollbar_profile = tk.Scrollbar(master=self.top_frame, cnf={'orient': "vertical", 'command': self.canvas_profile.yview,
                                                                     'width': 10, 'elementborderwidth': 0, 'highlightthickness': 1,
                                                                     'background': "#fff", 'activebackground': "#fff", 'troughcolor': "#000",
                                                                     'activerelief': tk.RAISED})
        scrollbar_profile.pack(side='right', fill='y', expand=0)
        self.canvas_profile.config(yscrollcommand=scrollbar_profile.set)
        self.canvas_profile.create_window(
            (0, 0), anchor='nw', window=self.frame_profile)
        self.canvas_profile.pack(fill='both', expand=1)

        self.top_frame.bind('<Configure>', self.on_resize_window)

        self.admin_frames()

    def on_resize_window(self, event=None):
        self.canvas_profile.configure(
            scrollregion=self.canvas_profile.bbox("all"))

    def admin_frames(self):
        self.left_side_frame = tk.Frame(
            master=self.frame_profile, cnf={'bg': '#068'})
        self.left_side_frame.pack(fill='both', expand=1)

        self.register_btn = tk.Button(master=self.left_side_frame, cnf={'text': "Register New Customer", 'bg': "green",
                                                                        'command': self._register_customer, 'font': ('Helvatica', 14),
                                                                        'foreground': "#fff", 'activebackground': "green",
                                                                        'activeforeground': "#fff", 'height': 5})
        self.register_btn.pack(pady=30, padx=10)

        self.set_bank_btn = tk.Button(master=self.left_side_frame, cnf={'text': "SetUp Bank", 'bg': "green",
                                                                        'command': self._set_bank, 'font': ('Helvatica', 14),
                                                                        'foreground': "#fff", 'activebackground': "green",
                                                                        'activeforeground': "#fff", 'height': 5, 'width': 15})
        self.set_bank_btn.pack(pady=30, padx=10)

        self.view_customers_btn = tk.Button(master=self.left_side_frame, cnf={'text': "View Customers", 'bg': "green",
                                                                              'command': self._view_customers, 'font': ('Helvatica', 14),
                                                                              'foreground': "#fff", 'activebackground': "green",
                                                                              'activeforeground': "#fff", 'height': 5})
        self.view_customers_btn.pack(pady=30, padx=10)

        self.dialy_transaction_btn = tk.Button(master=self.left_side_frame, cnf={'text': "View Transactions", 'bg': "green",
                                                                                 'command': self._daily_transact, 'font': ('Helvatica', 14),
                                                                                 'foreground': "#fff", 'activebackground': "green",
                                                                                 'activeforeground': "#fff", 'height': 5})

        self.dialy_transaction_btn.pack(pady=30, padx=10)

    def _register_customer(self):
        top = tk.Toplevel()
        top.config(background="#069")
        c = CreateCustomerAccount(top)
        top.title("Create Customer Account")
        top.resizable(width=0, height=0)

    def _set_bank(self):
        'set up bank branch and load bank money'
        if self.set_bank:
            self.bank.close_set()
            self.set_bank = False
        else:
            self.bank = Bank(self.profile_tab)
            self.set_bank = True
            try:
                self.view.close_view()
                self.view_daily.close_daily()
            except Exception as e:
                pass

    def _view_customers(self):
        'display customer on the load'
        if self.view_once:
            self.view.close_view()
            self.view_once = False
        else:
            self.view = AllCustomers(self.profile_tab)
            self.view_once = True
            try:
                self.bank.close_set()
                self.view_daily.close_daily()
            except Exception as e:
                pass

    def _daily_transact(self):
        'display dialy transactions'
        if self.dialy_trans:
            self.view_daily.close_daily()
            self.dialy_trans = False
        else:
            self.view_daily = DailyTransactions(self.profile_tab)
            self.dialy_trans = True
            try:
                self.bank.close_set()
                self.view.close_view()
            except Exception as e:
                pass
