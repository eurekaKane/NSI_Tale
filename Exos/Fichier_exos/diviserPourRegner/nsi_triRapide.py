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
        # à compléter
    return tabGauche, tabDroit  # renvoi des deux tableaux


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
        # à compléter
        
    # copie superficielle du tableau
    copieTab = list(tab)
    # appel récursif principal
    return quickSort_rec(copieTab)