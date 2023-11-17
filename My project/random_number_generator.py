import random
print("*" * 10, "Угадай число", "*" * 10)

print("Компьютер будет загадывать число 1 до 10. Попробуй угадать число. Для выхода введи 0")
answer = 1
score = 0
i = 0

while answer:
    i += 1
    rand = random.randint(1, 10)
    answer = int(input("Число загадано. Попробуй отгдать: "))
    if answer == rand:
        score += 1
        print("Правильно! Всего ты отгадал чисел ", score, "из", i)
    else:
        print("Неправильно :(")

print("До встречи в следующий раз")


