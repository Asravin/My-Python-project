import csv
max = int(input("Сколько строк вывести из файла: "))
k = 0
with open(r"My project\work in file\1.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)
        k += 1
        if k == max:
            break


