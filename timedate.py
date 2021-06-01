from os import scandir
import time
from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('Clock')
root.config(bg='light blue')

def clock():
    hr = time.strftime('%I')
    mn = time.strftime('%M')
    sc = time.strftime('%S')
    day = time.strftime('%A')
    am_pm = time.strftime('%p') 
    zone = time.strftime('%Z')

    l1.config(text=hr + ':'+ mn +':' + sc + " "  + am_pm)
    l1.after(1000,clock)

    l2.config(text= "DAY: " +day)
    l3.config(text= "Time Zone: " + zone)

l1=Label(root,text="",font=('Helvetica',18,'italic'),fg='white',bg='black')
l1.pack(pady=100)
l2=Label(root,text="",font=('Helvetica',18),fg='green',bg='orange')
l2.pack(pady=5)
l3=Label(root,text="",font=('Helvetica',18),fg='green',bg='orange')
l3.pack(pady=5)

clock()
root.mainloop()