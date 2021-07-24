import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox


from bank_database.bank_db import database_file


class TranferMoney:
    def __init__(self,parent,*args,**kwargs):
        self.parent = parent
        self.parent.config(background="#068")
        self.from_account = tk.StringVar()
        self.to_account = tk.StringVar()
        self.amount = tk.DoubleVar()
        
        
        self.from_account_label = tk.Label(master=self.parent,cnf={'text':"From Account:",'font':("Helvatica",14,'bold'),
                                                                   'bg':"#068",'foreground':"#FFF"})
        self.from_account_label.grid(cnf={'row':1,'column':0,'padx':20,'pady':20,'sticky':'w'})
        
        self.from_account_entry = tk.Entry(master=self.parent,cnf={'textvariable':self.from_account,'font':("Helvatica",14),
                                                                   'width':24})
        self.from_account_entry.grid(cnf={'row':1,'column':1,'padx':20,'pady':20,'sticky':"w"})
        self.from_account_entry.focus()
        
        self.to_account_label = tk.Label(master=self.parent,cnf={'text':"To Account:",'font':("Helvatica",14,'bold'),
                                                                   'bg':"#068",'foreground':"#FFF"})
        self.to_account_label.grid(cnf={'row':2,'column':0,'padx':20,'pady':20,'sticky':'w'})
        
        self.to_account_entry = tk.Entry(master=self.parent,cnf={'textvariable':self.to_account,'font':("Helvatica",14),
                                                                   'width':24})
        self.to_account_entry.grid(cnf={'row':2,'column':1,'padx':20,'pady':20,'sticky':"w"})
        
        self.amount_label = tk.Label(master=self.parent,cnf={'text':"Amount:",'font':("Helvatica",14,'bold'),
                                                                   'bg':"#068",'foreground':"#FFF"})
        self.amount_label.grid(cnf={'row':3,'column':0,'padx':20,'pady':20,'sticky':'w'})
        
        self.amount_entry = tk.Entry(master=self.parent,cnf={'textvariable':self.amount,'font':("Helvatica",14),
                                                                   'width':24})
        self.amount_entry.grid(cnf={'row':3,'column':1,'padx':20,'pady':20,'sticky':"w"})
        
        
        self.transfer_money_btn = tk.Button(master=self.parent, cnf={'text': "Transfer", 'bg': "green",
                                                                                        'font': ('Helvatica', 14),
                                                                                        'foreground': "#fff", 'activebackground': "green",
                                                                                        'activeforeground': "#fff",
                                                                                        'command':self._transfer})
        self.transfer_money_btn.grid(cnf={'row':4,'column':0,'columnspan':2,'pady':20})


    def _transfer(self):
        'retrieve from database and initiate transaction'
        #get from database
        #do subtraction and addition
        mbox.showinfo(title="Success",message=f"An Amount Of {self.amount.get()} Has Been Debited From Acc/N0. {self.from_account.get()}, Credited To Acc/No. {self.to_account.get()}")