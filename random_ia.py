import random

def random_ia(board, ia_signe):
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = ia_signe
            break
    return board