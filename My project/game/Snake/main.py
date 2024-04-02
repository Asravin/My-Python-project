from tkinter import *

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True


root = Tk()
root.title("Змейка")


c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#005500")
c.grid()
c.focus_set()
root.mainloop()