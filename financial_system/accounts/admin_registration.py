import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox as mbox


from bank_database.bank_db import database_file

class Accounts:
    """
    this page collects information about administrators and register them to the system

    information needed:
    1. Full name
    2. username,
    3. secret code
    4. password
    5. date birth
    """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.parent = parent
        tk.Label(master=self.parent, cnf={'text': "ACCOUNT REGISTRATION",
                                          'font': ("Helvatica", 17, 'underline'), 'foreground': "#fff",
                                          'bg': "#068"}).grid(row=0, column=0, columnspan=2, pady=20)
        # define the registration variables

        self.full_name = tk.StringVar()
        self.username = tk.StringVar()
        self.secret_code = tk.IntVar()
        self.password = tk.StringVar()
        self.date_of_birth = tk.StringVar()

        self.registration_interface()

    def registration_interface(self):
        """ define the interface"""
        self.register_fullname_label = tk.Label(master=self.parent, cnf={'text': "Full Name:", 'font': ("Helvatica", 16, 'bold'),
                                                                         'bg': "#068", 'foreground': "#fff"})
        self.register_fullname_label.grid(
            row=1, column=0, padx=10, pady=20, sticky='w')

        self.register_fullname_entry = tk.Entry(master=self.parent, cnf={
                                                'textvariable': self.full_name, 'font': ("Helvatica", 16, 'bold'), 'width': 20})
        self.register_fullname_entry.grid(
            row=1, column=1, padx=10, pady=20, sticky='w')
        self.register_fullname_entry.focus()

        self.register_birthdate_label = tk.Label(master=self.parent, cnf={'text': "Birth Date:", 'font': ("Helvatica", 16, 'bold'),
                                                                          'bg': "#068", 'foreground': "#fff"})
        self.register_birthdate_label.grid(
            row=2, column=0, padx=10, pady=20, sticky='w')
        self.register_birthdate_entry = DateEntry(
            master=self.parent, textvariable=self.date_of_birth, width=20, font=("Helvatica", 14))
        self.register_birthdate_entry.grid(
            row=2, column=1, padx=10, pady=20, sticky='w')

        self.register_username_label = tk.Label(master=self.parent, cnf={'text': "User Name:", 'font': ("Helvatica", 16, 'bold'),
                                                                         'bg': "#068", 'foreground': "#fff"})
        self.register_username_label.grid(
            row=3, column=0, padx=10, pady=20, sticky='w')

        self.register_username_entry = tk.Entry(master=self.parent, cnf={
            'textvariable': self.username, 'font': ("Helvatica", 16, 'bold'), 'width': 20})
        self.register_username_entry.grid(
            row=3, column=1, padx=10, pady=20, sticky='w')

        self.register_password_label = tk.Label(master=self.parent, cnf={'text': "Password:", 'font': ("Helvatica", 16, 'bold'),
                                                                         'bg': "#068", 'foreground': "#fff"})
        self.register_password_label.grid(
            row=4, column=0, padx=10, pady=20, sticky='w')

        self.register_password_entry = tk.Entry(master=self.parent, cnf={
                                                'textvariable': self.password, 'font': ("Helvatica", 16, 'bold'), 'width': 20})
        self.register_password_entry.grid(
            row=4, column=1, padx=10, pady=20, sticky='w')

        self.secret_code_label = tk.Label(master=self.parent, cnf={'text': "Secret Code:", 'font': ("Helvatica", 16, 'bold'),
                                                                         'bg': "#068", 'foreground': "#fff"})
        self.secret_code_label.grid(
            row=5, column=0, padx=10, pady=20, sticky='w')

        self.secret_code_entry = tk.Entry(master=self.parent, cnf={
                                                'textvariable': self.secret_code, 'font': ("Helvatica", 16, 'bold'), 'width': 20})
        self.secret_code_entry.grid(
            row=5, column=1, padx=10, pady=20, sticky='w')
        
        self.register_button = tk.Button(master=self.parent, cnf={'text': "Register", 'font': ("Helvatica", 17), 'bg': "#004dd9",
                                                                  'foreground': "#fff", 'width': 14, 'activeforeground': "#fff",
                                                                  'activebackground': "#0088aa", 'command': self._register_user})
        self.register_button.grid(row=6, column=0, columnspan=2, pady=20)

    def _clear_values(self):
        self.register_fullname_entry.delete(0, tk.END)
        self.register_birthdate_entry.delete(0, tk.END)
        self.register_username_entry.delete(0, tk.END)
        self.register_password_entry.delete(0, tk.END)
        self.secret_code_entry.delete(0, tk.END)

    def _register_user(self):
        full_name = self.full_name.get()
        dob = self.date_of_birth.get()
        username = self.username.get()
        password = self.password.get()
        secret_code = self.secret_code.get()
        
        if full_name.lower() != "" and username.lower() != "" and len(password.lower()) >= 5 and secret_code >=3:
            results = database_file.insert_administrator(full_name,dob,username,password,secret_code)
            if results == True:
                mbox.showinfo(title="Sucess",
                      message="Admin Has Been Registered Successfully.")
                self._clear_values()
                self.parent.withdraw()
            else:
                mbox.showerror(title="Error",message="Incorrect Data Format To Save")
        else:
            mbox.showerror(title='Error',message="Please Ensure That Secret Code Is More Than 3 Digit And Must Be Integers ONLY. Password Aleast 5 characters")
