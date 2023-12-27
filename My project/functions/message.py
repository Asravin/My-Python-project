def yn(message):
    resp = None
    while resp not in ("yes", "no"):
        resp = input(message).lower()
    return resp

answer = yn("Форматировать диск? [yes/no] ")
print("Ваш выбор: ", answer)