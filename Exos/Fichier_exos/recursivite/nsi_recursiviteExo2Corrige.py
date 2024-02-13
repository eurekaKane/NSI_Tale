def hanoi(n : int) -> list:
    """Renvoie la liste des déplacements
        des disques pour une pile initiale
        de n disques au départ.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # traitement
    depart = [k for k in range(n, 0, -1)]
    # les 3 tours sont des piles
    intermediaire : list = list()
    arrivee : list = list()
    result : list = list()
    # étiquettes des 3 tours pour l'affichage
    etiquettes = ('d', 'i', 'a')
    # pour gérer les tours avec un indice
    piles = (depart, intermediaire, arrivee)
    # deplacer
    def deplacer(n : int, d : int,\
                 a : int) -> None:
        # ajout du déplacement
        result.append((n, etiquettes[d], etiquettes[a]))
        # réalisation du déplacement
        piles[a].append(piles[d].pop())
        return None
    # coeur récursif
    def hanoi_rec(n : int, d : int, i : int,\
                  a : int) -> None:
        if n > 1:
            hanoi_rec(n - 1, d, a, i)
            deplacer(n, d, a)
            hanoi_rec(n - 1, i, d, a)
        elif n == 1:
            deplacer(n, d, a)
        return None
    # appel récursif principal
    hanoi_rec(n, 0, 1, 2)
    return result


def afficherHanoi(tab : list) -> None:
    """Affiche les déplacements des disques renvoyés par
        la fonction hanoi de manière concrète.
        tab possède un nombre impair d'éléments quand il
        n'est pas vide.
    """
    # coeur récursif 
    def affiche_rec(g : int, d : int) -> None:
        """Affichage des éléments du tableau d'indices
            compris entre g et d - 1.
            Algorithme diviser pour régner.
        """
        if d - g <= 3:  # régner
            for i in range(g, d):
                # côte à côte avec une espace
                print(tab[i], end = ' ')
            print()  # à la ligne
        else:
            # diviser
            m = g + (d - g) // 2  # indice du milieu
            # appel récursif sur la partie gauche
            affiche_rec(g, m)  # régner
            # affichage du milieu avec un décalage
            print(tab[m][0]*'  ' + str(tab[m]))  # combiner
            # appel récursif sur la partie droite
            affiche_rec(m + 1, d)  # régner
        return None
    # appel récursif principal
    affiche_rec(0, len(tab))  # tableau entier
    return None


def deplacementsHanoi(n : int) -> int:
    """Renvoie le nombre de déplacements de disques réalisés
        pour déplacer la pile de n disques depuis la tour de
        départ jusqu'à celle d'arrivée.
        Cette fonction est récursive.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # coeur récursif
    def dH_rec(n : int, acc : int) -> int:
        """Paradigme fonctionnel."""
        if n == 0:
            return acc
        else:
            return dH_rec(n - 1, 2 * acc + 1)
    # appel principal
    return dH_rec(n, 0)   
    

if __name__ == "__main__":
    afficherHanoi(hanoi(4))
    print()
    print("Nombre de déplacements de disques :",\
          deplacementsHanoi(4))