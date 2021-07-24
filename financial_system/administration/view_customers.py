import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox


class AllCustomers:

    def __init__(self, parent_path, *args, **kwargs):
        self.parent_path = parent_path

        self.parent = tk.Frame(self.parent_path, cnf={'bg': "#068"})
        self.parent.pack(pady=0)

        tk.Label(master=self.parent, cnf={'text': "VIEWING ALL REGISTERED ACTIVE CUSTOMERS IN THE BANK",
                                          'font': ("Helvatica", 16, 'underline'), 'foreground': "#fff", 'bg': "#068"}
                 ).pack(pady=10)

        self.tree_view = ttk.Treeview(master=self.parent, selectmode="browse")
        self.tree_view['column'] = ('1', '2', '3', '4', '5')
        self.tree_view['show'] = "headings"
        self.tree_view.heading('#1', text="Account No.")
        self.tree_view.heading('#2', text="Customer Name")
        self.tree_view.heading('#3', text="Phone Number")
        self.tree_view.heading('#4', text="Balance")
        self.tree_view.heading('#5', text='Loan Status')
        self.tree_view.pack(side='left', expand=1)

        self.yscroll = tk.Scrollbar(
            self.parent, cnf={'orient': "vertical", 'command': self.tree_view.yview})
        self.yscroll.pack(fill='y', side='right')
        self.tree_view.config(yscrollcommand=self.yscroll.set)

        self.new_frame = tk.Frame(master=self.parent_path, cnf={'bg': "#068"})
        self.new_frame.pack(fill='x', pady=0)
        self.xscroll = tk.Scrollbar(
            self.new_frame, cnf={'orient': "horizontal", 'command': self.tree_view.yview})
        self.xscroll.pack(fill='x')

        self.tree_view.config(xscrollcommand=self.xscroll.set)

        tk.Button(master=self.new_frame, cnf={'text': "Delete Customer", 'bg': "#a00",
                                              'font': ("Helvatica", 14), 'activebackground': "#a00", 'foreground': "#fff",
                                              'activeforeground': "#fff", 'command': self._delete_item}
                  ).pack(pady=20)

        tk.Label(master=self.new_frame, cnf={'text': "TO DELETE A CUSTOMER ACCOUNT, SELECT ON THEM FROM THE TABLE ABOVE.",
                                             'font': ("Helvatica", 16,), 'foreground': "#f8f000", 'bg': "#068"}
                 ).pack()

    def close_view(self):
        "close the view frame"
        self.parent.destroy()
        self.new_frame.destroy()

    def _delete_item(self):
        mbox.askyesno(title="Dangerous Operation",
                      message="You're About To Delete A Customer Account!")