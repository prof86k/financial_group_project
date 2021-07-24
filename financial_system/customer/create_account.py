import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkcalendar import DateEntry
import time
# import other files
from bank_database.bank_db import database_file


class CreateCustomerAccount:
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.full_name = tk.StringVar()
        self.gender = tk.StringVar()
        self.phone = tk.StringVar()
        self.next_kin = tk.StringVar()
        self.dob = tk.StringVar()
        self.id_value = tk.StringVar()
        self.occupation = tk.StringVar()
        self.account_id = tk.StringVar()
        
        label_text = tk.Label(master=self.parent, cnf={'text': "REGISTER A NEW CUSTOMER", 'bg': "#069", 'font': ("Helvatica", 15, 'underline'),
                                                       'foreground': '#EEE'})
        label_text.grid(row=0, column=1, columnspan=2, pady=20)
        self.interface()

    def interface(self):
        self.full_name_label = tk.Label(master=self.parent, cnf={'text': "Full Name:", 'font': ("Helvatica", 15, 'bold'),
                                                                 'bg': "#069", 'foreground': "#fff"})
        self.full_name_label.grid(
            row=1, column=0, sticky='w', padx=20, pady=15)
        self.full_name_entry = tk.Entry(master=self.parent, cnf={'textvariable': self.full_name, 'font': ("Helvatica", 14, 'bold'),
                                                                 'width': 24})
        self.full_name_entry.grid(
            row=1, column=1, sticky='w', padx=20, pady=15)
        self.full_name_entry.focus()

        self.gender_label = tk.Label(master=self.parent, cnf={'text': "Gender:", 'font': ("Helvatica", 15, 'bold'),
                                                              'bg': "#069", 'foreground': "#fff"})
        self.gender_label.grid(row=1, column=2, sticky='w', padx=20, pady=15)

        self.gender_entry = ttk.Combobox(
            master=self.parent, textvariable=self.gender, width=22, font=("Helvatica", 14))
        self.gender_entry.grid(row=1, column=3, sticky='w', padx=20, pady=15)
        self.gender_entry['values'] = ('...', 'Male', 'Female', 'Other')
        self.gender_entry.current(0)

        self.birth_date_label = tk.Label(master=self.parent, cnf={'text': "Date Of Birth.:", 'font': ("Helvatica", 15, 'bold'),
                                                                  'bg': "#069", 'foreground': "#fff"})
        self.birth_date_label.grid(
            row=2, column=0, sticky='w', padx=20, pady=15)

        self.birth_date_entry = DateEntry(master=self.parent, textvariable=self.dob, font=("Helvatica", 14),
                                          width=22)
        self.birth_date_entry.grid(
            row=2, column=1, sticky='w', padx=20, pady=15)

        self.occupation_label = tk.Label(master=self.parent, cnf={'text': "Occupation:", 'font': ("Helvatica", 15, 'bold'),
                                                                  'bg': "#069", 'foreground': "#fff"})
        self.occupation_label.grid(
            row=2, column=2, sticky='w', padx=20, pady=15)

        self.occupation_entry = tk.Entry(master=self.parent, cnf={'textvariable': self.occupation, 'font': ("Helvatica", 14, 'bold'),
                                                                  'width': 24})
        self.occupation_entry.grid(
            row=2, column=3, sticky='w', padx=20, pady=15)

        self.next_kin_label = tk.Label(master=self.parent, cnf={'text': "Next of Kin:", 'font': ("Helvatica", 15, 'bold'),
                                                                'bg': "#069", 'foreground': "#fff"})
        self.next_kin_label.grid(row=3, column=0, sticky='w', padx=20, pady=15)

        self.next_kin_entry = tk.Entry(master=self.parent, cnf={'textvariable': self.next_kin, 'font': ("Helvatica", 14, 'bold'),
                                                                'width': 24})
        self.next_kin_entry.grid(row=3, column=1, sticky='w', padx=20, pady=15)

        self.Id_label = tk.Label(master=self.parent, cnf={'text': "National ID:", 'font': ("Helvatica", 15, 'bold'),
                                                          'bg': "#069", 'foreground': "#fff"})
        self.Id_label.grid(row=3, column=2, sticky='w', padx=20, pady=15)

        self.Id_entry = tk.Entry(master=self.parent, cnf={'textvariable': self.id_value, 'font': ("Helvatica", 14, 'bold'),
                                                          'width': 24})
        self.Id_entry.grid(row=3, column=3, sticky='w', padx=20, pady=15)

        self.phone_label = tk.Label(master=self.parent, cnf={'text': "Phone No.:", 'font': ("Helvatica", 15, 'bold'),
                                                             'bg': "#069", 'foreground': "#fff"})
        self.phone_label.grid(row=4, column=0, sticky='w', padx=20, pady=15)

        self.phone_entry = tk.Entry(master=self.parent, cnf={'textvariable': self.phone, 'font': ("Helvatica", 14, 'bold'),
                                                             'width': 24})
        self.phone_entry.grid(row=4, column=1, sticky='w', padx=20, pady=15)
        
        self.account_id_label = tk.Label(master=self.parent, cnf={'text': "Account Number:", 'font': ("Helvatica", 15, 'bold'),
                                                             'bg': "#069", 'foreground': "#fff"})
        self.account_id_label.grid(row=4, column=2, sticky='w', padx=20, pady=15)

        self.account_id_entry = tk.Entry(master=self.parent, cnf={'textvariable': self.account_id, 'font': ("Helvatica", 14, 'bold'),
                                                             'width': 24})
        self.account_id_entry.grid(row=4, column=3, sticky='w', padx=20, pady=15)


        self.register_btn = tk.Button(master=self.parent, cnf={'text': "Register", 'font': ("Helvatica", 14), 'foreground': "#fff",
                                                               'background': "green", 'activebackground': "green", 'activeforeground': "#fff",
                                                               'width': 15, 'command': self._customer_register})
        self.register_btn.grid(
            row=5, column=0, columnspan=2, padx=20, pady=15, sticky='e')
        
        self.generate_account_btn = tk.Button(master=self.parent, cnf={'text': "Register", 'font': ("Helvatica", 14), 'foreground': "#fff",
                                                               'background': "green", 'activebackground': "green", 'activeforeground': "#fff",
                                                               'width': 15, 'command': self._customer_register})
        self.generate_account_btn.grid(
            row=5, column=1, columnspan=2, padx=20, pady=15, sticky='e')

    def _customer_register(self):
        fullName = self.full_name.get()
        gender = self.gender.get()
        phone = self.phone.get()
        nation_id = self.id_value.get()
        next_ken = self.next_kin.get()
        dob = self.dob.get()
        occupation = self.occupation.get()
        if fullName != "" and gender != "" and phone != "" and nation_id != "" and dob != "" and occupation != "":
            # into database
            mbox.showinfo(title="Success",
                          message="Customer has Been Register Successfully.")
            self.parent.destroy()
        else:
            mbox.showerror(title="Error", message="Some Fields Are Empty.")
            self.parent.destroy()
        
    def _generate_account_id(self):
        "auto generate account ID using current account in the database"
        " Generate Account number for every customer in the bank system"
        first_digits = time.strftime("%Y", time.localtime())
        branch_number = "134"  # from branch number from admin site
        acc_no = first_digits+branch_number + \
            "{0:05}".format(56)  # number from database