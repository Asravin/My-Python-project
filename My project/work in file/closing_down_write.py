import pickle
datafile = open(r"My project\work in file\names.dat", "rb")
first_names = pickle.load(datafile)
last_names = pickle.load(datafile)
datafile.close()

print(first_names)
print(last_names)