import tkinter as tk
from tkinter import ttk
from main_app import main_interface as mit

def manager():
    root = tk.Tk()
    root.wm_title("BANKING SYSTEM")
    root.config(background="#068")
    root.geometry("500x500")
    root.resizable(width=0, height=0)
    tk.Label(master=root, cnf={'text': "BANKING AND FINANCE", 'font': (
        "Helvatica", 18), 'foreground': "#fff", 'bg': "#068"}).pack(side=tk.TOP)
    main = mit.MainInterface(root)
    #run the app here
    root.mainloop()

if __name__ == "__main__":
    manager()
