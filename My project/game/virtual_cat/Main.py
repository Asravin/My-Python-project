from class_cat import Cat
Eva = Cat()
choice = None
while choice != "0":
    print \
        ("""
        Что будем делать?
        
        0 - Выйти
        1 - Поговорить с кошкой
        2 - Покормить
        3 - Поиграть
        4 - Взвесить
        """)
        
    choice = input(">>: ")
    print()
    
    if choice == "0":
        print("Пока.")
    
    elif choice == "1":
        Eva.talk()
    
    elif choice == "2":
        Eva.eat()
        
    elif choice == "3":
        Eva.play()
    
    elif choice == "4":
        print("Вес: ", Eva.weight, " гр.")
    
    else:
        print("\n Неправильный ввод!")