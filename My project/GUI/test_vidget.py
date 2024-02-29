from tkinter import*
root = Tk()

but = Button(root, text="Это кнопка", width=30, height=5, bg="white", fg="blue")

lab = Label(root, text="Это надпись! /n Вторая строка.", font="Arial 16")

ent = Entry(root, width=20, bd=3)

var = IntVar()
var.set(1)
rad0 = Radiobutton(root, text="Windows", variable=var, value=0)
rad1 = Radiobutton(root, text="Linux", variable=var, value=1)
rad2 = Radiobutton(root, text="macOS", variable=var, value=2)

r = ['Windows', 'macOS', 'Linux']
lis = Listbox(root, selectmode=SINGLE, height=4)
for i in r:
    lis.insert(END, i)

win = Toplevel(root, relief=SUNKEN, bd=10, bg="lightblue")
win.title("Дочернее окно")
win.minsize(width=400, height=200)

sca1 = Scale(root, orient=HORIZONTAL, length=300, from_=0, to=100, tickinterval=10, resolution=5)
sca2 = Scale(root, orient=VERTICAL, length=400, from_=1, to=2, tickinterval=0.1, resolution=0.1)

but.pack()
lab.pack()
ent.pack()
rad0.pack()
rad1.pack()
rad2.pack()
lis.pack()
sca1.pack()
sca2.pack()
win.pack_propagate()
root.mainloop()
