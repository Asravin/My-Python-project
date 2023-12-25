cars = ["audi", "vw", "lexus", "gtr", "m5"]
japan_cars = ["toyota", "nissan"]
cars += japan_cars
print(cars)

cars.append("kamaz")
print(cars)

cars.remove("kamaz")
print(cars)

cars.count("kamaz")
print(cars)
