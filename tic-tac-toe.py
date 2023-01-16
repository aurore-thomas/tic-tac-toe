import random
from random_ia import random_ia as easy_ia
from hardcore_ia import hardcore_ia 

# ---------------------------------------------
# PARTIE COMMUNE A TOUS LES TYPES DE JEUX
# ---------------------------------------------

def empty_board():
    # Création du tableau :
    board = [" ", " ", " ", 
            " ", " ", " ", 
            " ", " ", " "]
    return board

def display(board):
    # Affichage du tableau de jeu :
    print(board[0], "|", board[1], "|", board[2], "         1 | 2 | 3")
    print("--+---+--", "         --+---+--")
    print(board[3], "|", board[4], "|", board[5], "         4 | 5 | 6")
    print("--+---+--", "         --+---+--")
    print(board[6], "|", board[7], "|", board[8], "         7 | 8 | 9 \n")

def game(player, board):
    # Création d'une fonction qui prend en paramètres un joueur.
    # Cette fonction annonce quel joueur doit jouer, lui donne le choix de la case 
    # et la refuse si celle-ci est invalide.
    answer = int(input("Où voulez-vous poser votre pion ? Entrez le numéro de la case : "))
    print("\n")

    # Cas où la réponse n'est pas valide
    while (answer > 9) or (answer < 1) or (board[answer - 1] != " "):
        print("La réponse n'est pas valide, choisissez une autre case !")
        answer = int(input("Où voulez-vous poser votre pion ? Entrez le numéro de la case VALIDE : "))

    board[answer - 1] = player 
    # Car l'index commence à 0
    
    # On affiche le tableau actualisé :
    return board

def endgame(board):
    # Conditions pour gagner : 
    if (board[0] == board[1]) and (board[1] == board[2]) and (board[0] != " "):
        print("\nRésultats : \n")
        display(board)
        return True
    elif (board[3] == board[4]) and (board[4] == board[5]) and (board[3] != " "):
        print("\nRésultats : \n")
        display(board)
        return True
    elif (board[6] == board[7]) and (board[7] == board[8]) and (board[6] != " "):
        print("\nRésultats : \n")
        display(board)
        return True
    elif (board[0] == board[3]) and (board[3] == board[6]) and (board[0] != " "):
        print("\nRésultats : \n")
        display(board)
        return True
    elif (board[1] == board[4]) and (board[4] == board[7]) and (board[1] != " "):
        print("\nRésultats : \n")
        display(board)
        return True
    elif (board[2] == board[5]) and (board[5] == board[8]) and (board[2] != " "):
        print("\nRésultats : \n")
        display(board)
        return True
    elif (board[0] == board[4]) and (board[4] == board[8]) and (board[0] != " "):
        print("\nRésultats : \n")
        display(board)
        return True
    elif (board[2] == board[4]) and (board[4] == board[6]) and (board[2] != " "):
        print("\nRésultats : \n")
        display(board)
        return True
    else:
        return False


# ---------------------------------------------
#               MODES DE JEU
# ---------------------------------------------

def menu(choix_jeu):
    board = empty_board()
    signe = ""

    print(colors.lightgrey,
        """
    __________________________________
    Choisissez un mode de jeu : 
        1 - Joueur VS Joueur
        2 - Joueur VS IA (Mode facile)
        3 - Joueur VS IA (Mode difficile)
        4 - Quitter le jeu
    __________________________________
    """)

    choix_jeu = int(input("Entrez le numéro du mode de jeu : "))
    match choix_jeu:
        case 1:
            j_vs_j()
        case 2:
            ia_game_easy(board, signe)
        case 3:
            ia_game_hard(board, signe)
        case 4:
            quit("Dommage, à bientôt !")

# Mode Joueur VS Joueur:
def j_vs_j():
    board = empty_board()
    rounds = 0
    choix_partie = 0
    name_one = input("Entrez le nom du joueur X : ")
    name_two = input("Entrez le nom du joueur O : ")

    while True: 
        display(board)
        if (rounds % 2 == 0):
            print("C'est au tour de", name_one)
            game("X", board)
        else:
            print("C'est au tour de", name_two)
            game("O", board)
        
        if (endgame(board)):
            if (rounds % 2 == 0):
                print(colors.lightblue,name_one, "a gagné la partie !")
                again_pvp(choix_partie)
            else:
                print(colors.lightred,name_two, "a gagné la partie !") 
                again_pvp(choix_partie)

        rounds +=1
        # Cas du match nul
        if rounds == 9:
            display(board)
            print("Match nul")
            again_pvp(choix_partie)
           
# Mode Joueur VS IA Facile:
def ia_game_easy(board, signe):
    board = empty_board()
    rounds = 0
    choix_partie = 0

    name_player = input("Entrez le nom du joueur : ")
    signe = input("Voulez-vous jouer X ou O ? ")
    if signe == "X":
        ia_signe = "O"
    else:
        ia_signe = "X"

    while True: 
        display(board)
        if (rounds % 2 == 0):
            if ia_signe == "X":
                print("C'est au tour de l'IA")
                easy_ia(board, ia_signe)
            else:
                print("C'est votre tour")
                game(signe, board)
        else:
            if ia_signe == "O":
                print("C'est au tour de l'IA")
                easy_ia(board, ia_signe )
            else:
                print("C'est votre tour")
                game(signe, board)
            
        
        if (endgame(board)):
            print("Fin de la partie")
            if ia_signe == "X" and rounds % 2 == 0:
                print(colors.lightred,"L'IA a gagné cette partie")
                again_pvia_easy(choix_partie)
            elif ia_signe == "O" and rounds % 2 != 0:
                print(colors.lightred, "L'IA a gagné cette partie")
                again_pvia_easy(choix_partie)
            else:
                print(colors.lightblue, "Vous avez gagné cette partie!")
                again_pvia_easy(choix_partie)

        rounds +=1
        # Cas du match nul
        if rounds == 9:
            display(board)
            print("Match nul")
            again_pvia_easy(choix_partie)

# Mode Joueur VS IA Difficile:
def ia_game_hard(board, signe):
    board = empty_board()
    rounds = 0
    choix_partie = 0

    name_player = input("Entrez le nom du joueur : ")
    signe = input("Voulez-vous jouer X ou O ? ")
    if signe == "X":
        ia_signe = "O"
    else:
        ia_signe = "X"

    while True: 
        display(board)
        if (rounds % 2 == 0):
            if ia_signe == "X":
                print("C'est au tour de l'IA")
                hardcore_ia(board, ia_signe)
            else:
                print("C'est votre tour")
                game(signe, board)
        else:
            if ia_signe == "O":
                print("C'est au tour de l'IA")
                hardcore_ia(board, ia_signe)
            else:
                print("C'est votre tour")
                game(signe, board)
            
        
        if (endgame(board)):
            print("Fin de la partie")
            if ia_signe == "X" and rounds % 2 == 0:
                print(colors.lightred, "L'IA a gagné cette partie")
                again_pvia_hard(choix_partie)
            elif ia_signe == "O" and rounds % 2 != 0:
                print(colors.lightred, "L'IA a gagné cette partie")
                again_pvia_hard(choix_partie)
            else:
                print(colors.lightblue, "Vous avez gagné !")
                again_pvia_hard(choix_partie)

        rounds +=1
        
        # Cas du match nul
        if rounds == 9:
            display(board)
            print("Match nul")
            again_pvia_hard(choix_partie)


# ---------------------------------------------
#              RELANCER LE JEU
# ---------------------------------------------

def again_pvp(choix_partie):
    print(colors.lightgrey,
        """
    __________________________________
    Que voulez-vous faire ?
        1 - Refaire une partie
        2 - Retour au menu principal
        3 - Quitter le jeu
    __________________________________
    """)

    choix_partie = int(input("Entrez le numéro : "))
    match choix_partie:
        case 1:
            j_vs_j()
        case 2:
            main()
        case 3:
            quit("Merci d'avoir joué, à bientôt !")

def again_pvia_easy(choix_partie):
    board = []
    signe = " "
    
    print(colors.lightgrey,"""
    __________________________________
    Que voulez-vous faire ?
        1 - Refaire une partie
        2 - Retour au menu principal
        3 - Quitter le jeu
    __________________________________
    """)

    choix_partie = int(input("Entrez le numéro : "))
    match choix_partie:
        case 1:
            ia_game_easy(board, signe)
        case 2:
            main()
        case 3:
            quit("Merci d'avoir joué, à bientôt !")

def again_pvia_hard(choix_partie):
    board = []
    signe = " "
    print(colors.lightgrey,"""
    __________________________________
    Que voulez-vous faire ?
        1 - Refaire une partie
        2 - Retour au menu principal
        3 - Quitter le jeu
    __________________________________
    """)

    choix_partie = int(input("Entrez le numéro : "))
    match choix_partie:
        case 1:
            ia_game_hard(board, signe)
        case 2:
            main()
        case 3:
            quit("Merci d'avoir joué, à bientôt !")

# ---------------------------------------------
#                    MAIN
# ---------------------------------------------
class colors:
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

def main():
    print(colors.lightred,
    """
 _____  _  ____     _____  ____  ____     _____  ____  _____
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____
""")

    choix_jeu = 0
    menu(choix_jeu)
        
main()