level = 0

login = ""
while not login:
    login = input("Login: ")

password = ""
while not password:
    password = input("Password: ")
     
if login == "root" and password == "tabk":
    level = 10
elif login == "den" and password == "secret":
    level = 5

if level:
    print("Привет, ", login)
    print("Твой уровень доступа: ", level)
else:
    print("Доступ закрыт!")