cars = ("Nissan", "Toyota", "Lexus")
drivers = ()
print(cars)

for item in cars:
    print(item)
    
if not cars:
    print("У вас нет автомобиля!")
    
print("Сейчас у вас", len(cars), "автомобилей")

if "Nissan" in cars:
    print("В вашем гараже есть Nissam!")

print("Ваш первый автомобиль: ", cars[0])