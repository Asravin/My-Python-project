print("Запись списка строк:")
lines = ["Строка 1\n", "Строка 2\n", "Строка 3\n"]
txt = open(r"My project\work in file\test.txt", "w", encoding="utf-8")
txt.writelines(lines)
txt.close()



print("Чтение созданного файла:")
txt = open(r"My project\work in file\test.txt", "r", encoding="utf-8")
for line in txt:
    print(line)
txt.close()