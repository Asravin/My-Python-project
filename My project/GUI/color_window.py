from tkinter import*
root = Tk()

fra = Frame(root, width=300, height=100, bg="Black")
fra.pack()

def colorR():
    fra.config(bg="Red")
    
def colorG():
    fra.config(bg="Green")
    
def colorB():
    fra.config(bg="Blue")
    
def square():
    fra.config(width=640)
    fra.config(height=480)
    
def rectangle():
    fra.config(width=800)
    fra.config(height=600)

m = Menu(root)
root.config(menu=m)

cm = Menu(m)
m.add_cascade(label="Цвет", menu=cm)
cm.add_command(label="Красный", command=colorR)
cm.add_command(label="Зеленый", command=colorG)
cm.add_command(label="Синий", command=colorB)

sm = Menu(root)
m.add_cascade(label="Размер", menu=sm)
sm.add_command(label="640x480", command=square)
sm.add_command(label="800x600", command=rectangle)

root.mainloop()