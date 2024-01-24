try:
    a = int(input("Введите целое число a: "))
    b = int(input("Введите целое число b: "))
    print("a / b =", a / b)
except ValueError:
    print("Нужно было ввести целое число!!!")
except ZeroDivisionError as e:
    print("На 0 делить нельзя!")
    print("А вот ругательство интерпритатора: ")
    print(e)