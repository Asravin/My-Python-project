from tkinter import *
from Segment import Segment
from Snake import Snake

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True


root = Tk()
root.title("Змейка")


c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#005500")
c.grid()


segments = [Segment(SEG_SIZE, SEG_SIZE),
            Segment(SEG_SIZE * 2, SEG_SIZE),
            Segment(SEG_SIZE * 3, SEG_SIZE)]


s = Snake(segments)
c.focus_set()
root.mainloop()