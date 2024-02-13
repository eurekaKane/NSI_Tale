"""Ce module offre des fonctions qui permettent de vérifier
    le paradoxe des anniversaires dans la version suivante.
    Dans une assemblée de 23 personnes, il y a une chance
    sur deux qu'au moins deux d'entre elles soient nées le
    même jour calendaire.
"""

import random as rd
import nsi_dates as dates


def genereDates() -> list:
    """Cette fonction renvoie un objet de type list dont les 23 valeurs
    sont des entiers aléatoires compris entre 1 et 366.
        La valeur renvoyée modélise une série de 23 dates d'anniversaire.
    """
    return [rd.randint(1, 366) for _ in range(23)]

def contientDoublon(tab : list) -> bool:
    """Cette fonction renvoie la valeur True si le tableau passé en
        argument contient au moins un doublon.
        Elle renvoie False sinon.
    """
    dejaVus = dates.creerEnsemble()  # création d'un ensemble de dates vide
    for elt in tab:  # pour chaque date de la liste
        if dates.estPresent(elt, dejaVus):  # si elt est déjà dans l'ensemble
            return True  # c'est un doublon
        dates.ajouteElement(elt, dejaVus)  # sinon il est ajouté
    return False  # il n'y a pas eu d'interruption