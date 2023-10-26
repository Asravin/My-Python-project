service = float(input("Введите стоимость технического обслуживания: "))
fuel = float(input("Стоимость топлива: "))
tax = float(input("Налоги и пошлины :"))
tuning = float(input("Тюнинг: "))
insurance = float(input("Стоимость страховки: "))

total = service + fuel + tax + tuning + insurance

print("Всего: ", total, "$")