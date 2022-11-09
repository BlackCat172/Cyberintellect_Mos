from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
from main import res_cos
from main import link_title

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'



root = tk.Tk()
root.geometry("400x400")
root.title("News Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)



def weblink(*args):
    index = lbx1.curselection()[0]
    item = lbx1.get(index)
    webbrowser.open_new(link_title[item])
    lbx1.delete(index)
    lbx2.insert(lbx2.size(),item)

tabControl.add(tab1, text='News')
tabControl.add(tab2, text='History')
tabControl.pack(expand=1, fill="both")
lbx1 = tk.Listbox(tab1,width=40,height=40)
lbx2 = tk.Listbox(tab2,width=40,height=40)

lbx1.bind('<<ListboxSelect>>', weblink)
for key in res_cos:
    lbx1.insert(END, key)






lbx1.pack()
lbx2.pack()

root.mainloop()
"""
lbx=Listbox(root,width=40,height=40)
lbx.pack(pady=15)

#AddItems
for i in range(30):
    lbx.insert(i,"this is a test "+str(i))


"""