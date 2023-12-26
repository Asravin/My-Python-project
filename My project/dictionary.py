print("=" * 15, "Словарь", "=" * 15)

dict = {
    "aplle" : "яблоко",
    "bold" : "жирный",
    "bus" : "автобус",
    "cat" : "кошка",
    "car" : "автомобиль"
}

word = " "
while word != "q":
    word = input("Введите слово или 'q' для выхода: ")
    if word != "q":
        if word in dict:
            print(dict[word])
        else:
            print("Нет такого слова в словаре")
            
dict["test"] = "тест"

del dict["bus"]

# print(dict.get("test", "Нет такого слова в словаре!"))

# print(dict)
# print(dict["bus"])

# for item in dict:
#     print(item, " => ", dict[item])

# if "bus" in dict:
#     print(dict["bus"])
# else:
#     print("Слова 'bus' нет в словаре!")