print("\t\t\t Имя v.0.0.2\n")
name = input("Как тебя зовут? ")

import winsound
Freq = 2500            #частота
Dur = 1000        #длительность
winsound.Beep(Freq, Dur)


print("Привет, ", name)