# part 1
n = int(input("Give a number: "))
for i in range(1, n + 1, 2):
    print(" " * (n - i), end=' ')
    print('* ' * i)
for i in range(n - 2, 0, -2):
    print(" " * (n - i), end=' ')
    print('* ' * i)


# part 2
import random

def print_line(spaces, ch, char_times):
    for i in range(spaces):
        print(' ', end=' ')
    for i in range(char_times):
        if random.random() > 0.8:
            print('0', end= ' ')
        else:
            print(ch, end=' ')
    print()
ch = input("Give a charachter: ")
n = int(input("Give a number: "))
spaces = n // 2
asterisks = 1

for i in range(spaces, -1, -1):
    print_line(i, ch, asterisks)
    asterisks += 2

print_line(spaces, '#', 1)


# part 3
print("TIC-TAC-TOE GAME")
def display_board(b):
    for r in range(3):
        for c in range(3):
            print(b[r][c], end=" ")
        print()

def play():
    row = int(input("Row: ")) - 1
    col = int(input("Col: ")) - 1
    return row, col

def check_winner(board, player):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True
        
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True
            
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

board = [['-'] * 3 for i in range(3)]
player = 'X'    
counter = 0

while True:
    display_board(board)
    r, c = play()
    if board[r][c] == '-':
        board[r][c] = player
        counter += 1

        if check_winner(board, player):
            display_board(board)
            print("Player" ,player, "wins!")
            break

        player = 'X' if player == 'O' else 'O'
        if counter == 9:
            display_board(board)
            print("Tie!")
            break
    else:
        print("Error: not empty pisition")