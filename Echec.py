position = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "8" : 0, "7" : 1, "6" : 2, "5" : 3, "4" : 4, "3" : 5, "2" : 6, "1" : 7}
horizontal = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G", 7 : "H"}
vertical = {0 : "8", 1 : "7", 2 : "6", 3 : "5", 4 : "4", 5 : "3", 6 : "2", 7 : "1"}

class Piece :

    def __init__(self, team=None):
        self.couleur=team
        self.representation="p"
        self.nom = "pion"

    def can_moove (self, ligne, case, destination, board):
        pass

    def __str__(self):
        if self.couleur=="white":
            self.representation=self.representation.upper()
        return self.representation

class Pion(Piece):

    def __init__(self, team):
        super().__init__(team=team)

    def can_moove (self, ligne, case, destination, board):
        if case == destination[1]:
            if self.couleur == "white" and isinstance(board[destination[0]][destination[1]], Piece) is False:
                if destination[0] == ligne-1:
                    return True
                elif destination[0] == ligne-2 and ligne == 6 :
                    if isinstance(board[ligne-1][case], Piece) is False :
                        return True
            elif self.couleur == "black" and isinstance(board[destination[0]][destination[1]], Piece) is False:
                if destination[0] == ligne+1 :
                    return True
                elif destination[0] == ligne+2 and ligne == 1 :
                    if isinstance(board[ligne+1][case], Piece) is False :
                        return True

        elif isinstance(board[destination[0]][destination[1]], Piece):
            if self.couleur == "white" and destination[0] == ligne-1:
                if case - 1 == destination[1] or case + 1 == destination[1]:
                    return True
            if self.couleur == "black" and destination[0] == ligne+1:
                if case - 1 == destination[1] or case + 1 == destination[1]:
                    return True

class Tour(Piece):

    def __init__(self, team):
        super().__init__(team=team)
        self.representation="t"
        self.nom = "tour"
    
    def can_moove (self, ligne, case, destination, board):
        check_passage=True
        if case == destination[1] and ligne != destination[0]:
            if ligne >= destination[0] :
                espace = ligne - destination[0]
                for i in range (1, espace) :
                    if isinstance (board[ligne - i][case], Piece):
                        check_passage=False
                if check_passage is True:
                    return True
            elif ligne <= destination[0]  : 
                espace = destination[0] - ligne
                for i in range (1, espace) :
                    if isinstance (board[ligne + i][case], Piece):
                        check_passage=False
                if check_passage is True :
                    return True
        elif destination[0] == ligne and case != destination [1]:
            if case >= destination[1] :
                espace = case - destination[1]
                for i in range (1, espace) :
                    if isinstance (board[ligne][case - i], Piece):
                        check_passage=False
                if check_passage is True:
                    return True
            elif case <= destination[0]  : 
                espace = destination[1] - case
                for i in range (1, espace) :
                    if isinstance (board[ligne][case + i], Piece):
                        check_passage=False
                if check_passage is True :
                    return True


class Cavalier(Piece):

    def __init__(self, team):
        super().__init__(team=team)
        self.representation="c"
        self.nom = "cavalier"

    def can_moove (self, ligne, case, destination, board):
        if ligne - 1 == destination[0] or ligne + 1 == destination[0]:
            if case - 2 == destination[1] or case + 2 == destination[1]:
                return True
        elif case - 1 == destination[1] or case +1 == destination [1]:
            if ligne - 2 == destination[0] or ligne + 2 == destination [0]:
                return True   
        
class Fou(Piece):

    def __init__(self, team):
        super().__init__(team=team)
        self.representation="f"
        self.nom = "fou"
        
    def can_moove (self, ligne, case, destination, board):
        check_passage = True
        if ligne - destination [0] == case - destination[1] or ligne + case == destination[0] + destination[1]:
            if ligne > destination[0]:
                distance = ligne - destination[0]
                if case > destination[1]:
                    for i in range (1, distance):
                        if isinstance(board[ligne - i][case - i], Piece):
                            check_passage = False
                else :
                    for i in range (1, distance):
                        if isinstance(board[ligne - i][case + i], Piece):
                            check_passage = False
            else :
                distance = destination[0] - ligne
                if case > destination[1]:
                    for i in range (1, distance):
                        if isinstance(board[ligne + i][case - i], Piece):
                            check_passage = False
                else :
                    for i in range (1, distance):
                        if isinstance(board[ligne + i][case + i], Piece):
                            check_passage = False
            return check_passage            
        
class Roi(Piece):

    def __init__(self, team):
        super().__init__(team=team)
        self.representation="r"
        self.nom = "roi"

    def can_moove (self, ligne, case, destination, board):
        if ligne - 1 == destination[0] or ligne + 1 == destination[0]:
            if case - 1 == destination[1] or case + 1 == destination[1] or case == destination[1]:
                return True
        elif ligne == destination[0]:
            if case - 1 == destination[0] or case + 1 == destination [0]:
                return True
    
class Dame(Piece):

    def __init__(self, team):
        super().__init__(team=team)
        self.representation="d"
        self.nom = "dame"

    def can_moove (self, ligne, case, destination, board):
        check_passage=True
        if case == destination[1] and ligne != destination[0]:
            if ligne >= destination[0] :
                espace = ligne - destination[0]
                for i in range (1, espace) :
                    if isinstance (board[ligne - i][case], Piece):
                        check_passage=False
                if check_passage is True:
                    return True
            elif ligne <= destination[0]  : 
                espace = destination[0] - ligne
                for i in range (1, espace) :
                    if isinstance (board[ligne + i][case], Piece):
                        check_passage=False
                if check_passage is True :
                    return True
        elif destination[0] == ligne and case != destination [1]:
            if case >= destination[1] :
                espace = case - destination[1]
                for i in range (1, espace) :
                    if isinstance (board[ligne][case - i], Piece):
                        check_passage=False
                if check_passage is True:
                    return True
            elif case <= destination[0]  : 
                espace = destination[1] - case
                for i in range (1, espace) :
                    if isinstance (board[ligne][case + i], Piece):
                        check_passage=False
                if check_passage is True :
                    return True

        elif ligne - destination [0] == case - destination[1] or ligne + case == destination[0] + destination[1]:
            if ligne > destination[0]:
                distance = ligne - destination[0]
                if case > destination[1]:
                    for i in range (1, distance):
                        if isinstance(board[ligne - i][case - i], Piece):
                            check_passage = False
                else :
                    for i in range (1, distance):
                        if isinstance(board[ligne - i][case + i], Piece):
                            check_passage = False
            else :
                distance = destination[0] - ligne
                if case > destination[1]:
                    for i in range (1, distance):
                        if isinstance(board[ligne + i][case - i], Piece):
                            check_passage = False
                else :
                    for i in range (1, distance):
                        if isinstance(board[ligne + i][case + i], Piece):
                            check_passage = False
            return check_passage

def initialisation_plateau ():
    #Creation des lignes de pions
    whiterow_pawn=[]
    blackrow_pawn=[]
    for n in range(8):
        globals()["pion" + str(n+1)] = Pion ("white")
        whiterow_pawn.append(globals()["pion" + str(n+1)])

    for n in range(10, 18):
        globals()["pion" + str(n+1)] = Pion ("black")
        blackrow_pawn.append(globals()["pion" + str(n+1)])

    #Creation ligne piece blanche
    tour1= Tour("white")
    tour2= Tour("white")
    cavalier1 = Cavalier("white")
    cavalier2 = Cavalier("white")
    fou1 = Fou("white")
    fou2 = Fou("white")
    roi1 = Roi("white")
    dame1 = Dame("white")
    
    whiterow_piece=[]
    whiterow_piece.append(tour1)
    whiterow_piece.append(cavalier1)
    whiterow_piece.append(fou1)
    whiterow_piece.append(roi1)
    whiterow_piece.append(dame1)
    whiterow_piece.append(fou2)
    whiterow_piece.append(cavalier2)
    whiterow_piece.append(tour2)

    #Creation ligne piece noir
    tour11= Tour("black")
    tour12= Tour("black")
    cavalier11 = Cavalier("black")
    cavalier12 = Cavalier("black")
    fou11 = Fou("black")
    fou12 = Fou("black")
    roi11 = Roi("black")
    dame11 = Dame("black")
   
    blackrow_piece=[]
    blackrow_piece.append(tour11)
    blackrow_piece.append(cavalier11)
    blackrow_piece.append(fou11)
    blackrow_piece.append(roi11)
    blackrow_piece.append(dame11)
    blackrow_piece.append(fou12)
    blackrow_piece.append(cavalier12)
    blackrow_piece.append(tour12)

    #Creation des lignes de cases vides
    for i in range (4):
        globals()["ligne_vide" + str(i+1)] = []
        for j in range (8):
            globals()["ligne_vide" + str(i+1)].append(" ")

    #On remplit le plateau
    board = [blackrow_piece, blackrow_pawn, ligne_vide1, ligne_vide2, ligne_vide3, ligne_vide4, whiterow_pawn, whiterow_piece]
    return board

def affiche (board):
    print("\n")
    print("  A B C D E F G H")
    print("  ________________")
    m = 8
    for ligne in board:
        ligne_str = ""
        ligne_str = str(m) + "|" + ligne_str
        for case in ligne:
            ligne_str=ligne_str+ str(case) + " "
        ligne_str=ligne_str+"|"
        print (ligne_str)
        m -= 1
    print ("  ----------------")
    print("\n")

#On vérifie l'entrée du joueur
def coord (destination):
    bon = False
    while bon is False :
        destination = destination.upper()
        if len(destination) == 2:
            if destination[0] in position and destination[1] in position:
                destination = [position[destination[1]], position[destination[0]]]
                bon = True
                return destination
            else :
                print ("Veuillez entrer une destination correcte")
                destination = input()
        else :
            print ("Veuillez entrer une destination correcte")
            destination = input()

#On verefie que le joueur blanc ne peut bouger que les blancs et inversement
def meme_equipe (destination, board, joueur):
    if joueur is True :
        if isinstance(board[destination[0]][destination[1]], Piece):
            if board[destination[0]][destination[1]].couleur == "white" :
                return True
            else :
                return False
        else :
            return False
    if joueur is False :
        if isinstance(board[destination[0]][destination[1]], Piece):
            if board[destination[0]][destination[1]].couleur == "black" :
                return True
            else :
                return False
        else :
            return False

#on vérifie quelles pieces peuvent acceder a la case
def check_mvt (destination, board, joueur):
    possibilite = []
    for i in range (8) :
        for j in range (8) :
            if isinstance(board[i][j], str) is False:
                if board[i][j].couleur == "white" and joueur is True :
                    verif = board[i][j].can_moove(i, j, destination, board)
                    if verif is True and meme_equipe(destination, board, joueur) is False:
                        possibilite.append([i, j])
                if board[i][j].couleur == "black" and joueur is False :
                    verif = board[i][j].can_moove(i, j, destination, board)
                    if verif is True and meme_equipe(destination, board, joueur) is False:
                        possibilite.append([i, j])
    return possibilite

#On effectue le deplacement et le choix de la piece si necessaire
def mouvement (destination, possibilite, board):
    if len(possibilite) == 1 :
        board[destination[0]][destination[1]]= board[possibilite[0][0]][possibilite[0][1]]
        board[possibilite[0][0]][possibilite[0][1]]=" "
    else :
        print ("Voici la liste des pièces pouvant y acceder")
        i = 1
        for option in possibilite :
            if isinstance(board[option[0]][option[1]], Piece):
                piece = board[option[0]][option[1]].nom
                pos=str(horizontal[option[1]]) + str(vertical[option[0]])
                print (i,". ", piece, " en ", pos)
                i += 1
        choix = int(input("Entrer le numéro correspondant a votre choix"))
        board[destination[0]][destination[1]] = board[possibilite[choix-1][0]][possibilite[choix-1][1]]
        board[possibilite[choix-1][0]][possibilite[choix-1][1]] = " "
    
    board=promotion(board, destination)          
    return board

#Promotion du pion
def promotion (board, destination):
    if isinstance(board[destination[0]][destination[1]], Piece):
        if board[destination[0]][destination[1]].nom == "pion" :
            if board[destination[0]][destination[1]].couleur == "white" and destination[0] == 0:
                print ("Promotion du pion, comment voulez-vous le promouvoir ?")
                print ("1) dame\n2) tour\n3) cavalier\n4) Fou")
                dame_extra = Dame("white")
                tour_extra = Tour("white")
                cavalier_extra = Cavalier("white")
                fou_extra = Fou("white")
                dico_piece = {1 : dame_extra, 2 : tour_extra, 3 : cavalier_extra, 4 : fou_extra}
                choix_promotion = int(input("Votre choix ? "))
                while choix_promotion not in dico_piece:
                    choix_promotion= int(input("Veuillez entrer une valeur correcte : "))
                board[destination[0]][destination[1]] = dico_piece[choix_promotion]
            if board[destination[0]][destination[1]].couleur == "black" and destination[0] == 7:
                print ("Promotion du pion, comment voulez-vous le promouvoir ?")
                print ("1) dame\n2) tour\n 3) cavalier\n 4) Fou")
                dame_extran = Dame("black")
                tour_extran = Tour("black")
                cavalier_extran = Cavalier("black")
                fou_extran = Fou("black")
                dico_piece = {1 : dame_extran, 2 : tour_extran, 3 : cavalier_extran, 4 : fou_extran}
                choix_promotion = int(input("Votre choix ? "))
                while choix_promotion not in dico_piece:
                    choix_promotion= int(input("Veuillez entrer une valeur correcte : "))
                board[destination[0]][destination[1]] = dico_piece[choix_promotion]
    return board

def pos_roi (board, joueur):
    if joueur is True :
        for i in range (8):
            for j in range (8):
                if isinstance(board[i][j], Piece):
                    if board[i][j].nom == "roi" and board[i][j].couleur == "white":
                        position_roi=[i,j]

    else :
        for i in range (8):
            for j in range (8):
                if isinstance(board[i][j], Piece):
                    if board[i][j].nom == "roi" and board[i][j].couleur == "black":
                        position_roi=[i,j]

    return position_roi

#On regarde si on est en echec et mat
def echec_mat(board, joueur, position_roi):
    possibilite = []
    for i in range (8):
        for j in range (8):
            roi_deplacement = board[position_roi[0]][position_roi[1]].can_moove(position_roi[0], position_roi[1], [i,j], board)
            if roi_deplacement is True and meme_equipe([i,j], board, joueur) is False:
                met_en_echec = check_mvt([i,j], board, not joueur)
                if len(met_en_echec) == 0 :
                    possibilite.append([i, j])
    if len(possibilite)==0:
        return True
    else :
        return False

def main ():
    joueur = False
    fin = False
    board=initialisation_plateau()
    print ("\n--Bienvenu dans le jeu d'Echec de Nicolas Tahon-- \n")
    print ("Pour jouer, il vous suffit d'indiquer une case (ex: b4)")
    print ("Si une seule piece peut s'y rendre, elle s'y rendra !")
    print("En revanche, si plusieurs pièces peuvent y aller, \nalors il faudra choisir parmis la liste qui vous sera proposer en indiquant votre choix (ex: 3)")
    affiche(board)

    while fin is False :
        joueur = not joueur
        if joueur is True:
            print ("Joueur blanc :")
        else :
            print ("Joueur noir :")
        position_roi =  pos_roi(board, joueur)
        met_en_echec = check_mvt(position_roi, board, not joueur)
        if len(met_en_echec) == 0 :
            print ("Ou voulez vous aller ?")
            destination = input()
            destination = coord (destination)
            possibilite = check_mvt(destination, board, joueur)
            while len(possibilite)== 0 :
                print ("Aucune pièce ne peut s'y rendre, choississez une autre case :")
                destination = input()
                destination = coord (destination)
                possibilite = check_mvt(destination, board, joueur)
            board = mouvement(destination, possibilite, board)
            affiche(board)
        else :
            if echec_mat(board, joueur, position_roi) is False :
                print ("Vous etes en echec ! Votre mouvement ?")
                destination = input()
                destination = coord (destination)
                possibilite = check_mvt(destination, board, joueur)
                while len(possibilite)== 0 :
                    print ("Aucune pièce ne peut s'y rendre, choississez une autre case :")
                    destination = input()
                    destination = coord (destination)
                    possibilite = check_mvt(destination, board, joueur)
                board = mouvement(destination, possibilite, board)
                affiche(board)
            else :
                print ("Echet et mat")
                fin = True

main ()