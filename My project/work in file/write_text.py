print("Запись файла построчно:")
txt = open(r"My project\work in file\test.txt", "w", encoding="utf-8")
txt.write("Строка 1\n")
txt.write("Строка 2\n")
txt.close()



print("Чтение созданного файла:")
txt = open(r"My project\work in file\test.txt", "r", encoding="utf-8")
for line in txt:
    print(line)
txt.close()



