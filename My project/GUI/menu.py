from tkinter import*
root = Tk()

m = Menu(root)                        # Создается объект Меню на шлавном окне
root.config(menu=m)                   # Окно конфигурируется с указанием меню для него

fm = Menu(m)                          # Создается пункт меню с размещением на основном меню (m)
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Открыть...")
fm.add_command(label="Создать")
fm.add_command(label="Сохранить...")
fm.add_command(label="Выход")

hm = Menu()                           # Второй пункт меню
m.add_cascade(label="?", menu=hm)
hm.add_command(label="Справка")
hm.add_command(label="О программе")

nfm = Menu()                          # Создание ветки в основном меню
fm.add_cascade(label="Import", menu=nfm)
nfm.add_command(label="Image")
nfm.add_command(label="Text")

root.mainloop()