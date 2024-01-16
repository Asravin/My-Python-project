print("** Открытие и закрытие файла")
txt = open(r"My project\work in file\text.txt", encoding="utf-8")
txt.close()

print()

print("** Посимвольное чтение файла")
txt = open(r"My project\work in file\text.txt")
print(txt.read(1))
print(txt.read(2))
print(txt.read(6))
txt.close()

print()

print("** Посимвольное чтение файла с указанием кодировки")
txt = open(r"My project\work in file\text.txt", encoding="utf-8")
print(txt.read(1))
print(txt.read(2))
print(txt.read(6))
txt.close()

print()

print("** Чтение всего файла")
txt = open(r"My project\work in file\text.txt", encoding="utf-8")
content = txt.read()
print(content)
txt.close()