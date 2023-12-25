cars = ["audi", "vw", "lexus", "gtr", "m5"]
japan_cars = ["toyota", "nissan"]
cars += japan_cars

del cars[0]
print(cars)
del cars[:2]
print(cars)