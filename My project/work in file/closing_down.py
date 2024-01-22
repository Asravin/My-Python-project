import shelve
s = shelve.open("names2.dat")
s["first_name"] = ["Оля", "Вася", "Коля"]
s["last_name"] = ["Петрова", "Пупкин", "Смирнов"]
s.sync()
s.close()

s = shelve.open("names2.dat")
print(s["last_name"])