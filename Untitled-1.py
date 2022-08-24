
from tkinter import *
import os
from tkinter.filedialog import *

def s():
    path_ = askopenfile()
    path_ = path_.replace("/","\\\\")
    path.set(path_)

root = Tk()
Button(root,text='tr',command=s)
root.mainloop()