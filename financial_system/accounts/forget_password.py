import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox

from bank_database.bank_db import database_file


class PasswordRecovery:
    def __init__(self,parent,*args,**kwargs):
        self.parent = parent
        self.code  = tk.IntVar()
        self.username = tk.StringVar()
        # ======================= call functions
        self.use_styles()
        self.create_interface()
        self.display_info()
    
    def use_styles(self):
        self. style = ttk.Style()
        self.style.theme_use("clam")
        
        self.style.configure(
            "Treeview",
            background="#fff",
            foreground="#010",
            rowheight=24,
            font=("Helvatica",16),
            fieldbackgrond="#fff",
            padding=0
            )
        
        self.style.map('Treeview', 
                       background=[('selected',"#168"),], 
                       foreground=[('selected','#fff'),],
                       )
        
    def create_interface(self):
        #create interface for the password recovery
        self.secret_number_label = tk.Label(master=self.parent,cnf={'text':"Secret Code:",'font':("Helvatica",14,'bold'),
                                                                   'foreground':"#fff",'bg':"#068"})
        self.secret_number_label.grid(row=1,column=0,padx=10,pady=10,sticky='w')
        
        self.secret_number_entry = tk.Entry(master=self.parent,cnf={'textvariable':self.code,'font':("Helvatica",14),
                                                                   'width':24})
        self.secret_number_entry.grid(row=1,column=1,padx=10,sticky='w',pady=10)
        self.secret_number_entry.focus()
        
        self.username_label = tk.Label(master=self.parent,cnf={'text':"UserName:",'font':("Helvatica",14,'bold'),
                                                                   'foreground':"#fff",'bg':"#068"})
        self.username_label.grid(row=2,column=0,padx=10,pady=10,sticky='w')
        
        self.username_entry = tk.Entry(master=self.parent,cnf={'textvariable':self.username,'font':("Helvatica",14),
                                                                   'width':24})
        self.username_entry.grid(row=2,column=1,padx=10,sticky='w',pady=10)
        
        self.recover_btn = tk.Button(master=self.parent,cnf={'text':"Recover",'font':("Helvatica",14),
                                                             'bg':"green",'foreground':"#fff",'activeforeground':"#fff",
                                                             'activebackground':"green",'activeforeground':"#fff",
                                                             'command':self._recovery})
        self.recover_btn.grid(row=3,column=0,columnspan=2)
        
    def _recovery(self):
        #show information about password and username
        
        try:
            username = self.username.get()
            code = self.code.get()
            if  username != "" and code != "":
                response = database_file.select_for_admin_password_recovery(username.lower(),code)
            
                if code == response[1] and username == response[0]:
                    #retrieve from database
                    self.secret_number_entry.delete(0,tk.END)
                    self.username_entry.delete(0,tk.END)
                    self.text_info.insert('',tk.END,values=(code,username,response[2]))
            else:
                mbox.showerror(title="Error",message="please ensure all fields are not empty.")
        except TypeError:
            mbox.showerror(title="Error",message="Sorry user Does Not Exist.")
        except Exception as e:
            mbox.showerror(title="Error",message="Splease ensure all fields are not empty.")
        
    def display_info(self):
        #recovery information
        self.tree_info = tk.Frame(master=self.parent,cnf={'bg':"#068"})
        self.tree_info.grid(row=4,column=0,columnspan=2,pady=15,padx=10)
        self.text_info = ttk.Treeview(master=self.tree_info,selectmode='browse')
        self.text_info['column'] = ('1','2','3')
        self.text_info['show'] = "headings"
        self.text_info.heading('1',text='Secret Code')
        self.text_info.heading('2',text='User Name')
        self.text_info.heading('3',text='Password')
        self.text_info.pack()
        
        
        