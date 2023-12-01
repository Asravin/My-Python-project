cars = ()                                            # Пустой кортеж, кортеж как условие
if not cars:
    print("У вас пока нет автомобиля")

cars = ("nissan", "toyota", "lexus")                 # Вывод элемента кортежа
print("Выводим кортеж функцией print()")
print(cars)
print("Поэлементный перебор кортежа")
for item in cars:
    print(item)
    
print("Сейчас у вас ", len(cars), "автомобилей")     # len() и in
car = input("Поиск авто: ")
if car in cars:
    print("Автомобиль найден!")
else:
    print("Автомобиля", car, "у вас нет")

new_cars = ("ford", "audi")                          # Слияние кортежей
all_cars = cars + new_cars
print("Результат слияния: ")
print(all_cars)