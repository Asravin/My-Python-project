board = list(range(1, 10))



#Функция создания игрового поля
def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)




#Функция ввода и проверки информации
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        
        try:
            player_answer = int(player_answer)
        
        except:
            print("Некоректный ввод. Вы уверены, что ввели число?")
            continue
    
#проверка коректного ввода
    if player_answer >= 1 and player_answer <= 9:
        
        if(str(board[player_answer - 1]) not in "XO"):
            board[player_answer - 1] = player_token
            valid = True
        else:
            print("Эта клетка уже занята")
    
    else:
        print("Некоректный ввод. Введите число от 1 до 9!")