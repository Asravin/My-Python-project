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
    
    
    
    
#Проверка игрового поля и результа игры
def check_win(board):
    win_coord = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False



#Вызов основных функций
def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        count += 1
        
        if count > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выйграл!")
                win = True
                break
        
        if count == 9:
            print("Ничья!")
            break
    
    draw_board(board)
    
    
    
main(board)