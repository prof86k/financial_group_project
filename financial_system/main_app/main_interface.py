import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
# add other fills
from accounts import admin_registration as adr
from administration import admin_profile as adp
from customer import customer_profile as ctp
from accounts.forget_password import PasswordRecovery

# ======================= import database file -==================
from bank_database.bank_db import database_file


class MainInterface:
    """
    the main interface houses the rest of the programme
    it has ttk.Notebook that holds all the frame in their tabs
    """

    def __init__(self, parent, *args, **kwargs):
        super(MainInterface, self).__init__(*args, **kwargs)
        # define the login variables
        self.parent = parent
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        # call functions
        self.login_form()
        self.login_interface_fun()
        self.register_user()

    def login_form(self):
        self.account_tab = tk.Frame(
            master=self.parent, background="#068")
        self.account_tab.pack()

    def create_tabs(self, current_state):
        self.tabsframe = tk.Frame(
            self.parent, cnf={'relief': tk.SUNKEN, 'width': 10, 'bg': '#FFF'})
        self.tabsframe.pack()

        self.note_book_tabs = ttk.Notebook(master=self.tabsframe)

        self.profile_tab = tk.Frame(
            master=self.note_book_tabs, background="#068")
        self.note_book_tabs.add(
            self.profile_tab, text="Profile", state=current_state)
        adp.AdminProfile(self.profile_tab)

        self.customer_tab = tk.Frame(
            master=self.note_book_tabs, background="#068")
        self.note_book_tabs.add(
            self.customer_tab, text='Customer', state=current_state)

        self.canvas = tk.Canvas(master=self.customer_tab, cnf={
                                'bg': "#068", 'borderwidth': 0, 'bd': 0})
        frame = tk.Frame(master=self.canvas, cnf={'bg': "#068"})

        scrollbar = tk.Scrollbar(master=self.customer_tab, cnf={'orient': "vertical", 'command': self.canvas.yview,
                                                                'width': 10, 'elementborderwidth': 0, 'highlightthickness': 1,
                                                                'background': "#fff", 'activebackground': "#fff", 'troughcolor': "#000",
                                                                'activerelief': tk.RAISED})
        scrollbar.pack(side='right', fill='y', expand=0)

        self.canvas.config(yscrollcommand=scrollbar.set)
        self.canvas.create_window((0, 0), anchor='nw', window=frame)
        self.canvas.pack(fill='both', expand=1)
        ctp.CustomerProfile(frame)

        self.log_out_tab = tk.Frame(
            self.note_book_tabs, bg="#068", relief=tk.GROOVE)

        self.note_book_tabs.add(
            self.log_out_tab, text="L o g O u t", state=current_state)

        self.note_book_tabs.pack()

    def on_resize_window(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def login_interface_fun(self):
        """ login interface design
        containing
        1. login fields (username and password) button"""
        self.username_label = tk.Label(master=self.account_tab, cnf={'text': "User Name:", 'font': ("Helvatica", 16, 'bold'),
                                                                     'bg': "#068", 'foreground': "#fff"})

        self.username_label.grid(row=0, column=0, padx=10, pady=20, sticky='w')
        self.username_entry = tk.Entry(master=self.account_tab, cnf={
            'textvariable': self.username, 'font': ("Helvatica", 16, 'bold'), 'width': 20})
        self.username_entry.grid(row=0, column=1, padx=10, pady=20, sticky='w')
        self.username_entry.focus()

        self.user_password_label = tk.Label(master=self.account_tab, cnf={'text': "Password:", 'font': ("Helvatica", 16, 'bold'),
                                                                          'bg': "#068", 'foreground': "#fff"})
        self.user_password_label.grid(
            row=1, column=0, padx=10, pady=20, sticky='w')
        self.user_password_entry = tk.Entry(master=self.account_tab, cnf={'textvariable': self.password, 'font': ("Helvatica", 16, 'bold'),
                                                                          'show': "***", 'width': 20})
        self.user_password_entry.grid(
            row=1, column=1, padx=10, pady=20, sticky='w')
        self.login_button = tk.Button(master=self.account_tab, cnf={'text': "Login", 'font': ("Helvatica", 17), 'bg': "#00b888",
                                                                    'foreground': "#fff", 'width': 14, 'activeforeground': "#ffd",
                                                                    'activebackground': "#00ab8a", 'command': self._login})
        self.login_button.grid(
            row=2, column=0, columnspan=2, pady=20)

    def _clear_entry_fields(self):
        self.username_entry.delete(0, tk.END)
        self.user_password_entry.delete(0, tk.END)

    def _login(self):
        user_name = self.username.get()
        password = self.password.get()
        try:
            result = database_file.select_for_admin_login(user_name.lower(),password.lower())
            if user_name.lower()== result[0] and password.lower() == result[1]:
                # set state to normal and destroy login tab and logout
                self._clear_entry_fields()
                self.create_tabs(current_state='normal')
                self.note_book_tabs.bind('<Configure>', self.on_resize_window)
                self.log_out()
                self.account_tab.pack_forget()

                self.parent.geometry("1300x740")
                self.parent.resizable(width=1, height=1)
        except TypeError:
            mbox.showerror(title="Error",message="User Does Not Exist Or Password Incorrect.")

    def register_user(self):
        frame = tk.Frame(master=self.account_tab, cnf={
                         'bg': "#068", 'borderwidth': 0})
        self.register_button = tk.Button(master=frame, cnf={'text': "Register Account", 'font': ("Helvatica", 17), 'bg': "#00ad88",
                                                            'foreground': "#fff", 'width': 14, 'activeforeground': "#fff",
                                                            'activebackground': "#33aaaa", 'command': self._register_fun})
        self.register_button.pack(pady=20)

        self.forget_button = tk.Button(master=frame, cnf={'text': "Forget Password ?", 'font': ("Helvatica", 17), 'bg': "#068",
                                                          'foreground': "#f8f000", 'width': 15, 'activeforeground': "#f9f",
                                                          'activebackground': "#069", 'justify': "center",
                                                          'borderwidth': 0, 'overrelief': None, 'command': self._forget_password})
        self.forget_button.pack(pady=20)
        frame.grid(row=3, column=0, columnspan=3)

    def _register_fun(self):
        accounts = tk.Toplevel()
        adr.Accounts(accounts)
        accounts.title("REGISTER ACCOUNT")
        accounts.config(background="#068")
        accounts.resizable(width=0, height=0)

    def _logout(self):
        ''' log the user out'''
        results = mbox.askyesno("Info", "Are You Sure You Want To LogOut?")
        if results:
            # hide all all curren tabs and recreate login tab
            # self.create_tabs(current_state="hidden")
            self.tabsframe.pack_forget()
            self.login_form()
            # bring the login interface and the button with accounts to create
            self.login_interface_fun()
            self.register_user()
            self.parent.geometry("500x500")
            self.parent.resizable(width=0, height=0)

    def log_out(self):
        ''' run the logout btn'''
        self.logoutbtn = tk.Button(self.log_out_tab, text="Log Out", fg="#fff", bg="#a11", font=("Helvatica", 18),
                                   width=30, command=self._logout, activebackground="#900", activeforeground="#FFF")
        self.logoutbtn.pack(pady=240, padx=230, expand=True)

    def _forget_password(self):
        top = tk.Toplevel()
        PasswordRecovery(top)
        top.title("Password Recovery")
        top.config(background="#068")
        top.resizable(width=0, height=0)