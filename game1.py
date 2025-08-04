import random
board=['-','-','-',
       '-','-','-',
       '-','-','-']
current_player='X'
winner=None
game_running=True
def print_board(board):
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('------')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('------')
    print(board[6] + '|' + board[7] + '|' + board[8])
def player_move(board):
    player=int(input("Enter a number between 1 to 9: "))
    if player>=1 and player<=9 and board[player-1]=='-':
        board[player-1]=current_player
    else:
        print("oops player is aldready in the spot")
def check_horizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!='-':
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!='-':
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!='-':
        winner=board[6]
        return True

def check_vertical(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!='-':
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!='-':
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!='-':
        winner=board[2]
        return True
def check_diagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!='-':
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!='-':
        winner=board[2]
        return True
def check_tie(board):
    global winner
    if "-" not in board:
        print_board(board)
        print("It is a tie")
        game_running=False
def switch_player():
    global current_player
    if current_player=='X':
        current_player='O'
    else:
        current_player='X'
def check_win(board):
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print(f"The winner {winner}")

def player_computer(board):
    while current_player=='O':
        position=random.randint(0,8)
        if board[position]!='-':
            board[position]='O'
            switch_player()


while game_running:
    print_board(board)
    player_move(board)
    check_win(board)
    check_tie(board)
    switch_player()
    player_computer(board)
    check_win(board)
    check_tie(board)
