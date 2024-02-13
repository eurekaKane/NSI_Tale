"""Offre des fonctions pour la gestion d'un ensemble de
    jours de naissances compris entre 1 et 366.
"""

from typing import List

Ensemble = List[int]  # une structure de données adaptée

def _verifiePreConditions(val, ens) -> None:
    """Cette fonction lève une exception ValueError si les pré-conditions
        portant sur les arguments val et ens ne sont pas vérifiées.
    """
    if not isinstance(val, int):
        raise ValueError("Le premier argument est un entier naturel")
    if not (isinstance(ens, list) and len(ens) == 6 and isinstance(ens[0], int)):
        raise ValueError("Le second argument doit avoir été créé avec creerEnsemble.")
    return None

def creerEnsemble() -> Ensemble:
    """Cette fonction renvoie un ensemble vide.
        Par exemple : ens = creerEnsemble()
    """
    return [0]*6  # 6 entiers à 0 encodés sur 64 bits

def estPresent(val : int, ens : Ensemble) -> bool:
    """Cette fonction renvoie la valeur True si la valeur
        val se trouve dans l'ensemble nommé ens créé avec
        la fonction creerEnsemble.
        Par exemple estPresent(45, ens)
    """
    # pré-conditions
    _verifiePreConditions(val, ens)
    # validité de la valeur de val
    if val < 1 or val > 366:
        return False
    # sinon
    j, i = divmod(val, 64)  # quotient et reste
    return ens[j] & (1<<i) != 0

def ajouteElement(val : int, ens : Ensemble) -> None:
    """Cette fonction ajoute la valeur val à l'ensemble
        ens créé avec la fonction creerEnsemble.
        Cet ajout est réalisé en place.
        Par exemple ajouteElement(24, ens)
    """
    # pré-conditions
    _verifiePreConditions(val, ens)
    # validité de la valeur de val
    if val < 1 or val > 366:
        raise ValueError("Le premier argument " + str(val) + " est invalide.")
    # sinon
    j, i = divmod(val, 64)  # quotient et reste
    ens[j] = ens[j] | (1<<i)
    return None