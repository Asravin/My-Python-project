import pickle

#Запись
first_name = ["Оля", "Вася", "Коля"]
last_name = ["Петрова", "Пупкин", "Смирнов"]

datafile = open(r"My project\work in file\names.dat", "wb")
pickle.dump(first_name, datafile)
pickle.dump(last_name, datafile)
datafile.close()


