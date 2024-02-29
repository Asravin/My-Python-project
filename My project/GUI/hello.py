from tkinter import*
def hello(event):
    print("Hello World!")
    
root = Tk()
but1 = Button(root)
but1["text"] = "Привет"
but1.bind("<Button-1>", hello)

root.title("Заголовок окна программы")
root.geometry("300x250")
but1.pack()
root.mainloop()

