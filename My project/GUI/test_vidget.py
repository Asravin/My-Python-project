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



but.pack()
lab.pack()
ent.pack()
rad0.pack()
rad1.pack()
rad2.pack()
lis.pack()
root.mainloop()
