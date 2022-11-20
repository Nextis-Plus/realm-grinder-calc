from tkinter import *
from tkinter import ttk

def initUIStructure(height,width):
    root=Tk()
    
    header=ttk.Frame(root,height=height,width=width)
    content=ttk.Frame(root,height=height,width=width)
    selectBar=ttk.Frame(root,height=height,width=width)

    header.grid(column=0,row=0,sticky="new")
    content.grid(column=0,row=1,sticky="nsew")
    selectBar.grid(column=0,row=2,sticky="sew")

    root.columnconfigure(0,minsize=100,weight=1)
    root.rowconfigure(0,minsize=100)
    root.rowconfigure(1,minsize=100,weight=1)
    root.rowconfigure(2,minsize=100)
    root.mainloop()
    

initUIStructure(300,100)

    