import random
rounds = 0

def hardcore_ia(board, ia_signe):

    while rounds < 9:
        move = random.randint(0,8)
        # ---------------------------------------------
        #                    MODE DEFENSE
        # ---------------------------------------------
        
        # Ligne 1:
        if board[0] == board[1] and board[0] != " ":
            board[2] = ia_signe
            return board
        elif board[0] == board[2] and board[0] != " ":
            board[1] = ia_signe
        elif board[1] == board[2] and board[1] != " ":
            board[0] = ia_signe
        
        # Ligne 2:
        elif board[3] == board[4] and board[3] != " ":
            board[5] = ia_signe
        elif board[3] == board[5] and board[3] != " ":
            board[4] = ia_signe
        elif board[4] == board[5] and board[4] != " ":
            board[3] = ia_signe

        # Ligne 3:
        elif board[6] == board[7] and board[6] != " ":
            board[8] = ia_signe
        elif board[6] == board[8] and board[6] != " ":
            board[7] = ia_signe
        elif board[7] == board[8] and board[7] != " ":
            board[6] = ia_signe
        
        # Colonne 1:
        elif board[0] == board[3] and board[0] != " ":
            board[6] = ia_signe
        elif board[0] == board[6] and board[0] != " ":
            board[3] = ia_signe
        elif board[3] == board[6] and board[3] != " ":
            board[0] = ia_signe
        
        # Colonne 2:
        elif board[1] == board[4] and board[1] != " ":
            board[7] = ia_signe
        elif board[1] == board[7] and board[1] != " ":
            board[4] = ia_signe
        elif board[4] == board[7] and board[4] != " ":
            board[1] = ia_signe
        
        # Colonne 3:
        elif board[2] == board[5] and board[2] != " ":
            board[8] = ia_signe
        elif board[2] == board[8] and board[2] != " ":
            board[5] = ia_signe
        elif board[5] == board[8] and board[5] != " ":
            board[2] = ia_signe
        
        # Diagonale gauche:
        elif board[0] == board[4] and board[0] != " ":
            board[8] = ia_signe
        elif board[0] == board[8] and board[0] != " ":
            board[4] = ia_signe
        elif board[4] == board[8] and board[4] != " ":
            board[0] = ia_signe
        
        # Diagonale droite:
        elif board[6] == board[4] and board[6] != " ":
            board[2] = ia_signe
        elif board[6] == board[2] and board[6] != " ":
            board[4] = ia_signe
        elif board[2] == board[4] and board[2] != " ":
            board[6] = ia_signe
        
        else:
            while board[move] != " ":
                move = random.randint(0,8)
            board[move] = ia_signe
            return board
    
        break
    return board