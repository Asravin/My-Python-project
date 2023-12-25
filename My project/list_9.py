cars = ["audi", "vw", "lexus", "gtr", "m5"]
japan_cars = ["toyota", "nissan"]
cars += japan_cars

print("Исходный список: ")
print(cars)

print("Сортируем список: ")
cars.sort()
print(cars)

print("Добавляем элемент 'kamaz': ")
cars.append("kamaz")
print(cars)

print("Обращаем порядок списка: ")
cars.reverse()
print(cars)