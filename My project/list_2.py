cars = ["audi", "vw", "lexus", "gtr", "m5"]
car = input("Введите искомый автомобиль: ")
if car in cars:
    print("У вас есть такой автомобиль!")
else:
    print("У вас нет такого автомобиля :()")