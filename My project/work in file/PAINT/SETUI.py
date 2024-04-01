from tkinter import *
def setUI(self):
    self.parent.tittle("Simple paint")
    self.pack(fill=BOTH, expand=1)
    self.columnconfigure(6, weight=1)
    self.rowconfigure(2, weight=1)
    self.canv = Canvas(self, bg="white")
    self.canv.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)
    
    
    color_lab = Label(self, text="Цвет: ")
    color_lab.grid(row=0, column=0, padx=6)
    
    
    red_btn = Button(self, text="Красный", width=10)
    red_btn.grid(row=0, column=1)
    
    green_btn = Button(self, text="Зеленый", width=10)
    green_btn.grid(row=0, column=2)
    
    blue_btn = Button(self, text="Синий", width=10)
    blue_btn.grid(row=0, column=3)
    
    black_btn = Button(self, text="Черный", width=10)
    black_btn.grid(row=0, column=4)
    
    white_btn = Button(self, text="Белый", width=10)
    white_btn.grid(row=0, column=5)
    
    
    size_lab = Label(self, text="Размер кисти: ")
    size_lab.grid(row=1, column=0, padx=5)
    
    
    one_btn = Button(self, text="2x", width=10)
    one_btn.grid(row=1, column=1)
    
    two_btn = Button(self, text="5x", width=10)
    two_btn.grid(row=1, column=2)
    
    five_btn = Button(self, text="7x", width=10)
    five_btn.grid(row=1, column=3)
    
    seven_btn = Button(self, text="10x", width=10)
    seven_btn.grid(row=1, column=4)
    
    ten_btn = Button(self, text="20x", width=10)
    ten_btn.grid(row=1, column=5)
    
    twenty_btn = Button(self, text="50x", width=10)
    twenty_btn.grid(row=1, column=6, sticky=W)
    
    