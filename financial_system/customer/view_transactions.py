import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
import os 
import tempfile


from bank_database.bank_db import database_file


class ViewTranseactions:
    def __init__(self,parent,*args,**kwargs):
        self.parent = parent
        self.parent.config(background="#068")
        self.account_num = tk.StringVar()
        
        self.account_num_label = tk.Label(master=self.parent,cnf={'text':"Account Number:",'font':("Helvatica",14,'bold'),
                                                                  'bg':"#068",'foreground':"#fff"})
        self.account_num_label.grid(row=1,column=0,padx=20,pady=20,sticky='w')
        
        self.account_num_entry = tk.Entry(master=self.parent,cnf={'textvariable':self.account_num,'font':("helvatica",14),
                                                                  'width':24})
        self.account_num_entry.grid(cnf={'row':1,'column':1,'padx':20,'pady':20,'sticky':"w"})
        self.account_num_entry.focus()
        
        self.view_btn = tk.Button(master=self.parent,cnf={'text':"View Transactions",'font':("Helvatica",14),'bg':"green",
                                                          'foreground':"#fff",'activebackground':"green",'activeforeground':"#fff",
                                                          'command':self._view_info})
        self.view_btn.grid(cnf={'row':1,'column':2,'padx':20,'pady':20,'sticky':'w'})
        
        self.view_tree_frame = tk.Frame(master=self.parent,cnf={'bg':"#068"})
        self.view_tree_frame.grid(cnf={'row':2,'column':0,'columnspan':3,'pady':20})
        
        self.view_text_frame = tk.Frame(master=self.parent,cnf={'bg':"#068"})
        self.view_text_frame.grid(cnf={'row':3,'column':0,'columnspan':3,'padx':20,'pady':20})
        
        #========================= call functions ==========================
        self.view_tree()
        self.text_to_print_info()
        #================================= define print button to print generated results ======
        self.print_inf_table_btn = tk.Button(master=self.parent,cnf={'text':"Print Results",'font':("Helvatica",14),'bg':"#a00",
                                                                 'foreground':"#fff",'activeforeground':"#FFF",
                                                                 'activebackground':"#a00",'command':self._print_table})
        self.print_inf_table_btn.grid(cnf={'row':4,'column':1,'pady':20})
        
    def view_tree(self):
        self.transaction_tree = ttk.Treeview(master=self.view_tree_frame,selectmode="browse")
        self.transaction_tree['column'] = ('1','2','3','4','5')
        self.transaction_tree['show'] = "headings"
        self.transaction_tree.heading('#1',text="Account No.")
        self.transaction_tree.heading('#2',text='Customer Name')
        self.transaction_tree.heading("#3",text='Amount')
        self.transaction_tree.heading("#4",text='Date')
        self.transaction_tree.heading('5',text="Transaction Type")
        self.transaction_tree.pack(side='left',fill='x')
        
        self.tree_scrollbar = tk.Scrollbar(master=self.view_tree_frame,cnf={'orient':"vertical",'command':self.transaction_tree.yview,
                                                                            'troughcolor':"#000"})
        self.tree_scrollbar.pack(side='right',fill='y')
        
        self.transaction_tree.config(yscrollcommand=self.tree_scrollbar.set)
    
    def text_to_print_info(self):
        self.info_text = tk.Text(master=self.view_text_frame,cnf={'font':("Helvatica",14),'foreground':"#013",
                                                                  'padx':25,'pady':25,'wrap':"word",'height':6})
        self.info_text.pack(side='left',fill='x')
        
        self.text_scrollbar = tk.Scrollbar(master=self.view_text_frame,cnf={'orient':"vertical",'command':self.info_text.yview,
                                                                            'troughcolor':"#000"})
        self.text_scrollbar.pack(side='right',fill='y')
        
        self.info_text.config(yscrollcommand=self.text_scrollbar.set)
        
    def _view_info(self):
        "retrieve from database"
        #populate tree view widget
        #populate text widget
        pass
        
    def _print_table(self):
        'print to the default type in the pc'
        text_file = self.info_text.get('1.0',tk.END+'-1c')
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(text_file)
        os.startfile(filename,'print')