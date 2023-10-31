program = "Путевой компьютер, v.0.0.2"

stars = 80          # Количество звездочек
tabs = 5            # Колтчество отступов

dist = 0            # Расстояние, которое нужно проехать
speed = 0           # Средняя скорость авто, км/ч
time = 0            # Время в движении (за рулем)
total_time = 0      # Общее количество времени в пути

drive_hours = 0     # Часов в движении(полных)
drive_mins = 0      # Минут(остаток)
total_hours = 0     # Часов всего(полных)
total_mins = 0      # Минут всего(полных)

tank = 0            # Размер бака
consum = 0          # Средний расход л/100 км
dist = 0            # Расстояние в км.
refuels = 0         # Количество дозаправки
refuel_time = 20    # Время дозаправкм
fuel = 0            # Сколько затрачено топлива
price = 0           # Цена топлива

breaks = 0          # Количество плановых остановок
break_time = 0      # Время каждой плановой остановки



print("\t" * tabs, program)      # Блок заголовка
print("*" * stars)



dist = int(input("Введите расстояние, км: "))       # Ввод данных
speed = int(input("Планируемая средняя скорость(целое число): "))
consum = float(input("Введите средний расход л./100 км(вещ. число): "))
tank = float(input("Обьем бака, л: "))
price = float(input("Стоимость 1 литра топлива, в рублях: "))
breaks = float(input("Количество плановых остановок(без дозаправок): "))
break_time = float(input("Время каждой плановой остановки, минут: "))



time = dist * 60 / speed           # Время за рулем
fuel = consum * dist / 100         # Всего затраченно топлива

refuels = fuel // tank             # Общее время                                              
total_time = time + refuels * refuel_time + breaks * break_time 

drive_hours = time // 60
drive_mins = time - drive_hours * 60

total_hours = total_time // 60
total_mins = total_time - total_hours * 60

total_hours = total_time // 60
total_mins = total_time - total_hours * 60

print("*" * stars)
print("\t" * tabs, "Результат: ")



print("Время за рулем: ", int(drive_hours), "ч. ", int(drive_mins), "м. ")
print("Общее время в пути: ", int(total_hours), "ч. ", int(total_mins), "м. ")
print("Количество дозаправок: ", refuels)
print("Потраченно времени на дозаправку: ", refuels * refuel_time, " минут")
print("Израсходовано топлива, л.: ", fuel)
print("Стоимость топлива, р: ", fuel * price)
