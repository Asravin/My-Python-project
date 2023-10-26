consum = 0       # Средний расход 10.5 л/100 км
dist = 0         # Расстояние, км

consum = float(input("Введите средний расход л./100 км: "))
dist = float(input("Введите расстояние, км: "))

result = consum * dist / 100

print("Будет затрачено ", result, " литров")