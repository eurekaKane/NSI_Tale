import random as rd
from typing import Tuple


def _separe(tab : list, val) -> Tuple[list, list]:
    """Cette fonction sépare les éléments du tableau tab en deux
        sous-tableaux, celui des éléments dont la valeur est
        inférieure ou égale à val d'une part et les autres
        d'autre part.
    """
    # initialisation avec deux tableaux vides
    tabGauche, tabDroit = [], []
    # séparation
    for elt in tab:
        if elt <= val:
            tabGauche.append(elt)
        else:
            tabDroit.append(elt)
    return tabGauche, tabDroit  # renvoi des deux tableaux

# tests adaptés
assert _separe([5], 3) == ([], [5])
assert _separe([5], 6) == ([5], [])
assert _separe([-2, 6, -1.2, 3.4], 3.4) == ([-2, -1.2, 3.4], [6])
assert _separe([-1, 8, 7, -3.2, 12.57, 1], 1) == ([-1, -3.2, 1], [8, 7, 12.57])


def triRapide(tab : list) -> list:
    """Cette fonction renvoie un tableau composé des éléments
        de tab triés en ordre croissant.
        Elle met en œuvre l'algorithme de tri rapide.
        Elle est récursive.
    """
    # pré-condition
    assert isinstance(tab, list), "L'argument est un tableau."
    # moteur récursif
    def quickSort_rec(tab : list) -> list:
        if len(tab) <= 1:
            return tab  # régner
        else:
            # choix aléatoire du pivot
            indPivot = rd.randint(0, len(tab) - 1)  # indice pivot
            pivot = tab[indPivot]  # valeur du pivot
            del(tab[indPivot])  # retrait du tableau
            # diviser
            tabInf, tabSup = _separe(tab, pivot)
            # appels récursifs régner
            tabTrieGauche = quickSort_rec(tabInf)  # à gauche
            tabTrieDroit = quickSort_rec(tabSup)  # à droite
            # combiner
            return tabTrieGauche + [pivot] + tabTrieDroit
    # copie superficielle du tableau
    copieTab = list(tab)
    # appel récursif principal
    return quickSort_rec(copieTab)