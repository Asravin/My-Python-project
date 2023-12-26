print("=" * 15, "Словарь", "=" * 15)

# Словарь заполнен по умолчанию
dict = {                  
    "aplle" : "яблоко",
    "bold" : "жирный",
    "bus" : "автобус",
    "cat" : "кошка",
    "car" : "автомобиль"
}

# Справка. Будет выведена по команде 'h'
help_message = """
s - Поиск слова в словаре
a - Добавить новое слово
r - Удалить слово
k - Вывод всех слов
d - Вывод всего словаря
h - Отображение этой подсказки
q - Выход
"""

choice = " "
while choice != "q":
    choice = input("(h - справка)>> ")
    
# поиск слова в словаре
    if choice == "s":
        word = input("Введите слово: ")
        res = dict.get(word, "Нет такого слова!")
        print(res)

# добавление слова в словарь
    elif choice == "a":
        word = input("Введите слово: ")
        value = input("Введите перевод: ")
        dict[word] = value
        print("Слово добавлено!")
    
# удаление слов из словаря
    elif choice == "r":
        word = input("Введите слово: ")
        del dict[word]
        print("Слово ", word, " удалено")
    
# вывод всех слов
    elif choice == "k":
        print(dict.keys())
    
# вывод всего словаря
    elif choice == "d":
        for word in dict:
            print(word, ": ", dict[word])
    
# справка
    elif choice == "h":
        print(help_message)
    
# выход
    elif choice == "q":
        continue
    
    else:
        print("Нераспознанная команда. Введите 'h' для справки")
    