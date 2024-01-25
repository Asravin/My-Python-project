import pickle
mark = 0
print("*" * 10, "Тесты 2.0", "*" * 10)
try:
     datafile = open(r"test.dat", "rb")
except:
     print("Ошибка при загрузке вопросов!")
else:
     questions = pickle.load(datafile)
     answers = pickle.load(datafile)
     datafile.close()
     n = len(answers)
     i = 0
     for i in range(0, n):
          print(questions[i])
          try:
               a = int(input("Ваш ответ: "))
               if a == answers[i]:
                    mark += 1
                    print("Правильно!")
               else:
                    print("Неправильно :(")
          except:
               print("Нужно было ввести число. Ответ засчитан как неправильный!")
     print("Вы правильно ответили на ", mark, "вопросов из", n)