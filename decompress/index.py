#!/usr/bin/python

from Tkinter import *
from decompress import decompress

def didClick():
    result = decompress(textbox.get())
    label2.config(text=result)
    
view = Tk()
view.title("Decompress string")
view.geometry("300x200")
label = Label(view, text="Input decompress string :",justify=RIGHT )
form = Label(view, text="form exsample : 2[as]3[fp]4[eoirere]12[yu]",justify=RIGHT )
form.pack()
label.pack()
textbox = Entry(view)
textbox.pack()
B = Button(view, text ="enter", command = didClick)

B.pack()

label2 = Label(view, text= "" ,justify=RIGHT )
label2.pack()
view.mainloop()

