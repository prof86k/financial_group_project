import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox


class Bank:
    def __init__(self, parent_name, *args, **kwargs):
        self.parent_name = parent_name
        self.parent_name.config(background="#068")
        self.branch_code = tk.StringVar()
        self.load_bank = tk.DoubleVar()
        self.bank_name = tk.StringVar()

        self.parent = tk.Frame(self.parent_name, cnf={'bg': "#068"})
        self.parent.pack()
        tk.Label(master=self.parent, cnf={'text': 'SETUP BANK FOR OPERATION "BRANCH NUMBER IS USE FOR CUSTOMER ACCOUNT"',
                                          'font': ("Helvatica", 16, 'underline'), 'foreground': "#fff", 'bg': "#068"}
                 ).grid(cnf={'row': 0, 'column': 0, 'columnspan': 3, 'pady': 10})
        
        self.bank_name_label = tk.Label(master=self.parent, cnf={'text': "Bank Name:", 'bg': "#068",
                                                                  'font': ("Helvatica", 14, 'bold'),
                                                                  'foreground': "#fff"})
        self.bank_name_label.grid(cnf={'row': 1, 'column': 0, 'padx': 20,
                                        'pady': 20, 'sticky': "w"})

        self.bank_name_entry = tk.Entry(master=self.parent, cnf={'textvariable': self.bank_name, 'font': ("Helvatica", 14),
                                                                  'width': 24, })
        self.bank_name_entry.grid(
            cnf={'row': 1, 'column': 1, 'padx': 20, 'pady': 20, 'sticky': "w"})
        self.bank_name_entry.focus()

        self.set_branch_label = tk.Label(master=self.parent, cnf={'text': "Branch Code:", 'bg': "#068",
                                                                  'font': ("Helvatica", 14, 'bold'),
                                                                  'foreground': "#fff"})
        self.set_branch_label.grid(cnf={'row': 2, 'column': 0, 'padx': 20,
                                        'pady': 20, 'sticky': "w"})

        self.set_branch_entry = tk.Entry(master=self.parent, cnf={'textvariable': self.branch_code, 'font': ("Helvatica", 14),
                                                                  'width': 24, })
        self.set_branch_entry.grid(
            cnf={'row': 2, 'column': 1, 'padx': 20, 'pady': 20, 'sticky': "w"})

        self.set_branch_btn = tk.Button(master=self.parent, cnf={'text': "Set Branch Code", 'font': ("Helvatica", 14),
                                                                 'foreground': "#fff", 'activeforeground': "#fff", 'bg': "green",
                                                                 'activebackground': "green", 'command': self._set_branch_code})
        self.set_branch_btn.grid(
            cnf={'row': 2, 'column': 2, 'padx': 10, 'pady': 20, 'sticky': "w"})

        self.load_label = tk.Label(master=self.parent, cnf={'text': "Load Bank:", 'bg': "#068",
                                                            'font': ("Helvatica", 14, 'bold'),
                                                            'foreground': "#fff"})

        self.load_label.grid(cnf={'row': 3, 'column': 0, 'padx': 20,
                                  'pady': 20, 'sticky': "w"})
        self.load_entry = tk.Entry(master=self.parent, cnf={'textvariable': self.load_bank, 'font': ("Helvatica", 14),
                                                            'width': 24})
        self.load_entry.grid(
            cnf={'row': 3, 'column': 1, 'padx': 20, 'pady': 20, 'sticky': "w"})

        self.load_bank_btn = tk.Button(master=self.parent, cnf={'text': "Load Money", 'font': ("Helvatica", 14),
                                                                'foreground': "#fff", 'activeforeground': "#fff", 'bg': "green",
                                                                'activebackground': "green", 'command': self._load_money})

        self.load_bank_btn.grid(
            cnf={'row': 3, 'column': 2, 'padx': 10, 'pady': 20, 'sticky': "w"})

        self.show_info_frame = tk.Frame(master=self.parent, cnf={'bg': "#068"})
        self.show_info_frame.grid(
            cnf={'row': 4, 'column': 0, 'columnspan': 3, 'padx': 20, 'pady': 20})

        # =================== call functions here ====================
        self.show_info_tree()

    def _set_branch_code(self):
        'add to database is once'
        mbox.showinfo(title='Success',
                      message="Branch Code Has Been Set Successfully")
        self.set_branch_entry.delete(0, tk.END)

    def _load_money(self):
        'set up bank with some money'
        'initial deposite and subsequent deposites are update'
        mbox.showinfo(
            title='Success', message=f"Loading An Amount Of {self.load_bank.get()} Is Successful.")
        self.load_entry.delete(0, tk.END)

    def show_info_tree(self):
        'show update in tree view widget'
        self.tree = ttk.Treeview(self.show_info_frame, selectmode="browse")
        self.tree['column'] = ('1', '2', '3','4')
        self.tree['show'] = "headings"
        self.tree.heading('#1',text="Bank Name")
        self.tree.heading('#2', text="New Item")
        self.tree.heading('#3', text="Update")
        self.tree.heading('#4', text="Date")
        self.tree.pack()

    def close_set(self):
        "close bank settings"
        self.parent.destroy()