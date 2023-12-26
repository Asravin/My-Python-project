dict = {
    "aplle" : "яблоко",
    "bold" : "жирный",
    "bus" : "автобус",
    "cat" : "кошка",
    "car" : "автомобиль"
}

print(dict)
print(dict["bus"])

for item in dict:
    print(item, " => ", dict[item])