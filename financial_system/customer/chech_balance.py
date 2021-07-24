import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox

from bank_database.bank_db import database_file

class CheckBalance:
    def __init__(self,parent,*args,**kwargs):
        self.parent = parent
        self.parent.config(background="#068")
        self.account_number = tk.StringVar()
        
        self.show_title = tk.Label(master=self.parent,cnf={'text':"CHECK BALANCE",'font':("Helvatical",18,'underline'),
                                                           'bg':"#068",'foreground':"#FFF"})
        self.show_title.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
        
        self.account_number_label = tk.Label(master=self.parent,cnf={'text':"Account Number:",'font':("Helvatica",14,'bold'),
                                                                     'foreground':"#fff",'bg':"#068"})
        self.account_number_label.grid(row=1,column=0,sticky='w',padx=20,pady=20)
        
        self.account_number_entry = tk.Entry(master=self.parent,cnf={'textvariable':self.account_number,'font':("Helvatica",14)})
        self.account_number_entry.grid(row=1,column=1,sticky='w',padx=20,pady=20)
        self.account_number_entry.focus()
        
        self.check_btn = tk.Button(master=self.parent,cnf={'text':"Check",'bg':"green",'activebackground':"green",
                                                           'foreground':"#FFF",'foreground':"#FFF",'font':("Helvatica",14),
                                                           'activeforeground':"#fff",'command':self._check})
        self.check_btn.grid(row=1,column=2,padx=20,pady=20)
        
        self.show_frame = tk.Frame(master=self.parent,cnf={'bg':"#068"})
        self.show_frame.grid(row=2,column=0,columnspan=3,pady=20)
        # ======================================call functions =================
        self.show_balance_tree()
        
        
    def show_balance_tree(self):
        self.balance_tree = ttk.Treeview(master=self.show_frame,selectmode="browse")
        self.balance_tree['column'] = ('1','2','3')
        self.balance_tree['show'] = "headings"
        self.balance_tree.heading('#1',text="Account Number")
        self.balance_tree.heading('#2',text="Current Balance")
        self.balance_tree.heading("#3",text='Loan Status')
        self.balance_tree.pack()
        
    def _check(self):
        number = self.account_number.get()
        #retrieve from database
        #and populate the trees widget
        self.balance_tree.insert('',tk.END,values=(number,50.00,0.0))
        self.account_number_entry.delete(0,tk.END)