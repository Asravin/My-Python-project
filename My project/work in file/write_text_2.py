with open(r"My project\work in file\somefile.txt", "w") as f:
    print("Hello Word!", file=f)
    
    

print("Чтение созданного файла:")
txt = open(r"My project\work in file\somefile.txt", "r", encoding="utf-8")
for line in txt:
    print(line)
txt.close()