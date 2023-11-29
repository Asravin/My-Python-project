word = "привет"

print("Демо-программа 'Срезы'")
print("Введите начальный и конечный индексы для среза слова 'привет'")

begin = None
while begin != " ":
    begin = input("Начальная позиция: ")
    
    if begin:
        begin = int(begin)
        end = int(input("Конечная позиция: "))
        print(word[begin:end])