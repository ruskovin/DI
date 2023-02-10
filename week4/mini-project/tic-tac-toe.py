board = ["-", "-", "-",
         "-", "-", "-",
          "-", "-","-"]

player = 'X'

def display_board(board):
    print("*********")
    print(board[0], board[1],board[2])
    print("********")
    print(board[3], board[4],board[5])
    print("********")
    print(board[6], board[7],board[8])
    print("********")

def player_input(player):
    inp = int(input("enter a number 1-9 !"))
    if 1 <=inp <= 9 and board[inp-1] == '-':
        board[inp-1] = player
    else:
        print("please enter a correct number")


def check_win():
    if board[0] == board[1] == board[2] == player:
        print(player,'won')
        return True
    elif board[3] == board[4] == board[5] == player:
        print(player,'won')
        return True
    elif board[6] == board[7] == board[8]==player:
        print(player,'won')
        return True
    elif board[0] == board[3] == board[6]==player:
        print(player,'won')
        return True
    elif board[1] == board[4] == board[7] == player:
        print(player,'won')
        return True
    elif board[2] == board[5] == board[8]==player:
        print(player,'won')
        return True
    elif board[0] == board[4] == board[8]==player:
        print(player,'won')
        return True
    elif board[2] == board[4] == board[6]==player:
        print(player,'won')
        return True

running = True

def switch_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

while running:
    display_board(board)
    player_input(player)
    check_win()
    switch_player()
    if "-" not in board:
        print("Draw match")
        break
