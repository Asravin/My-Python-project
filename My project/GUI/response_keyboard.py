from tkinter import *
root = Tk()


def exit(event):
    root.destroy()

def caption(event):
    temp = ent.get()
    lbl.configure(text = temp)
    
    
ent = Entry(root, width=40)
lbl = Label(root, width=80)


ent.pack()
lbl.pack()


ent.bind('<Return>', caption)
root.bind('<Control-z>', exit)


root.mainloop()