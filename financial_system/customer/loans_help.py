import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox


from bank_database.bank_db import database_file


class LoanAndAid:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.parent.config(background="#068")
        self.account_number = tk.StringVar()
        self.loan_amount = tk.DoubleVar()
        
        self.account_number_label = tk.Label(master=self.parent,cnf={'text':"Account Number:",'bg':"#068",
                                                                     'font':("Helvatica",14,'bold'),'foreground':"#fff"})
        self.account_number_label.grid(row=1,column=0,padx=20,pady=20,sticky='w')
        self.account_number_entry = tk.Entry(master=self.parent,cnf={'textvariable':self.account_number,'font':("Helvatica",14),
                                                                     'width':24,})
        self.account_number_entry.grid(row=1,column=1,padx=20,pady=20,sticky='w')
        self.account_number_entry.focus()
        
        self.loan_amount_label = tk.Label(master=self.parent,cnf={'text':"Amount:",'bg':"#068",
                                                                     'font':("Helvatica",14,'bold'),'foreground':"#fff"})
        self.loan_amount_label.grid(row=2,column=0,padx=20,pady=20,sticky='w')
        
        self.loan_amount_entry = tk.Entry(master=self.parent,cnf={'textvariable':self.loan_amount,'font':("Helvatica",14),
                                                                     'width':24,})
        self.loan_amount_entry.grid(row=2,column=1,padx=20,pady=20,sticky='w')
        
        
        self.take_loan_btn = tk.Button(master=self.parent,cnf={'text':"Take Loan",'font':("Helvatica",14),'bg':"#a01a00",
                                                          'activebackground':"#a00022",'foreground':"#fff",
                                                          'activeforeground':"#fff",'command':self._take})
        self.take_loan_btn.grid(row=3,column=0,pady=20)
        
        self.pay_loan_btn = tk.Button(master=self.parent,cnf={'text':"Pay Loan",'font':("Helvatica",14),'bg':"#00ab8a",
                                                          'activebackground':"#00a788",'foreground':"#fff",
                                                          'activeforeground':"#fff",'command':self._pay_loan})
        self.pay_loan_btn.grid(row=3,column=1,padx=20,pady=20)
        
    
    def _take(self):
        'triger loan intake into the supposed account number'
        # retrieve from database to account number
        # show notification
        mbox.showinfo(title="Success",message=f"Your Has Been Credited With {self.loan_amount.get()} See You Soon!.")
        self.parent.withdraw()
        
    def _pay_loan(self):
        'pay loan back your loan'
        #subtract from account owing loan option in database
        #show notification
        mbox.showinfo(title="Success",message=f"An Amount Of {self.loan_amount.get()} Has Been Paid. Thank You.")
        self.parent.withdraw()