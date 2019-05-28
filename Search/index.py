#!/usr/bin/python

from Tkinter import *
from returnIndex import hello

def didClick():
    result = hello(textbox.get())
    label2.config(text=result)
    
    

view = Tk()
view.title("Function parameters")
view.geometry("300x200")
# var = StringVar()
label = Label(view, text="What fruit do you want to search ?",justify=RIGHT )
label.pack()
textbox = Entry(view)
textbox.pack()
B = Button(view, text ="Search", command = didClick)

B.pack()

label2 = Label(view, text= "" ,justify=RIGHT )
label2.pack()



# mainlabel = label(text="khaotu created")
# mainlabel.pack()
view.mainloop()

