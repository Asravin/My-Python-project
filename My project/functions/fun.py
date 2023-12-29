def fun1():
    global res
    res = 50
    print(res)

def fun2():
    global res
    print(res)

res = 30
print(res)
fun1()
fun2()
print(res)