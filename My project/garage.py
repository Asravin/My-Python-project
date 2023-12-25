print("*" * 10, " Гараж v.0.0.1 ", "*" * 10)

cars = []
responce = 1
while responce:
    
    print("""Выбирите действие:
          1 - Добавить автомобиль
          2 - Удалить автомобиль
          3 - Вывести список автомобилей
          4 - Найти автомобиль
          5 - Отсортировать гараж
          0 = Выйти""")
    
    responce = int(input(">> "))
    
    if responce == 1:
        car = input("Введите название авто: ")
        cars.append(car)
    
    elif responce == 2:
        car = input("Введите название авто: ")
        cars.remove(car)
        
    elif responce == 3:
        if len(cars) > 0:
            for car in cars:
                print(car)
        else:
            print("В гараже пусто! ")
    
    elif responce == 4:
        car = input("Введите название авто: ")
        if car in cars:
            print("Такой автомобиль есть в гараже!")
        else:
            print("Такого автомобиля нет в гараже!")
        
    elif responce == 5:
        cars.sort()
        print("Сортировка выполнена!")
    
    else:
        print("До скорой встречи!")