from tkinter import *
from Paint import *


def main():
        root = Tk()
        root.geometry("800x600+300+300")
        app = Print(root)
        root.mainloop()

if __name__ == "__main__":
    main()