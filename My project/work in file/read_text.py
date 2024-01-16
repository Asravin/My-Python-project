print("** Открытие и закрытие файла")
txt = open(r"C:\Users\Asravin\Desktop\Python Project\My project\work in file\read_text.py", encoding="utf-8")
txt.close()



print("** Посимвольное чтение файла")
txt = open(r"C:\Users\Asravin\Desktop\Python Project\My project\work in file\read_text.py", encoding="utf-8")
print(txt.read(1))
print(txt.read(2))
print(txt.read(3))
txt.close()


 
