#Jeu de Puissance 4 avec deux joueurs (X et O).
#Pour gagner 4 pions doivent être aligné horizontalement, verticalement ou diagonalement.
#Le jeu se joue sur le terminal en tour par tour.

# Définir la taille du plateau et le nombre de pions nécessaires pour gagner
taille_grille = 7
pions_pour_gagner = 4

# Définir l'état de la grille vide
grille = [[' ' for _ in range(taille_grille)] for _ in range(taille_grille)]

# Fonction pour afficher la grille
def afficher_grille():
    for ligne in grille:
        print(' | '.join(ligne))
        print('-----')

# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(joueur):
    for ligne in grille:
        for i in range(taille_grille - pions_pour_gagner + 1):
            if all([case == joueur for case in ligne[i:i+pions_pour_gagner]]):
                return True

    for col in range(taille_grille):
        for ligne in range(taille_grille - pions_pour_gagner + 1):
            if all([grille[ligne+i][col] == joueur for i in range(pions_pour_gagner)]):
                return True

    for ligne in range(taille_grille - pions_pour_gagner + 1):
        for col in range(taille_grille - pions_pour_gagner + 1):
            if all([grille[ligne+i][col+i] == joueur for i in range(pions_pour_gagner)]):
                return True

    for ligne in range(taille_grille - pions_pour_gagner + 1):
        for col in range(pions_pour_gagner - 1, taille_grille):
            if all([grille[ligne+i][col-i] == joueur for i in range(pions_pour_gagner)]):
                return True

    return False

# Fonction pour gérer le tour d'un joueur
def jouer_tour(joueur, col):
    for ligne in reversed(range(taille_grille)):
        if grille[ligne][col-1] == ' ':
            grille[ligne][col-1] = joueur
            if verifier_victoire(joueur):
                afficher_grille()
                print(f'Le joueur {joueur} a gagné !')
                return True
            break
    afficher_grille()
    return False

# Fonction pour gérer la boucle de jeu
def jouer_partie():
    joueur = 'X'
    jeu_en_cours = True
    while jeu_en_cours:
        col = int(input(f'Joueur {joueur}, entrez un numéro de colonne pour placer votre pion (1-{taille_grille}): '))
        if col < 1 or col > taille_grille:
            print('La colonne renseignée est invalide. Veuillez rejouer.')
        elif not jouer_tour(joueur, col):
            joueur = 'O' if joueur == 'X' else 'X'
        else:
            jeu_en_cours = False

# Démarrer le jeu
jouer_partie()
