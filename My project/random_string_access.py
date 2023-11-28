import random

word = input("Введите слово: ")

max = len(word)
min = -len(word)

for i in range(10):
    position = random.randrange(min, max)
    print("word[", position, "] = ", word[position])

print()

for i in range(min, max, 1):
    print("word[", i, "] = ", word[i])