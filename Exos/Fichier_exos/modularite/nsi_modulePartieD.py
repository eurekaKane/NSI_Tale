"""Offre des fonctions pour la gestion d'un ensemble de
    jours de naissances.
"""

def creerEnsemble() -> list:
    """Cette fonction renvoie un ensemble vide.
        Par exemple : ens = creerEnsemble()
    """
    return [0]*6  # 6 entiers à 0 encodés sur 64 bits

def estPresent(val, ens : list) -> bool:
    """Cette fonction renvoie la valeur True si la valeur
        val se trouve dans l'ensemble nommé ens créé avec
        la fonction creerEnsemble.
        Par exemple estPresent(45, ens)
    """
    j, i = divmod(val, 64)  # quotient et reste
    return ens[j] & (1<<i) != 0

def ajouteElement(val, ens : list) -> None:
    """Cette fonction ajoute la valeur val à l'ensemble
        ens créé avec la fonction creerEnsemble.
        Cet ajout est réalisé en place.
        Par exemple ajouteElement(24, ens)
    """
    j, i = divmod(val, 64)  # quotient et reste
    ens[j] = ens[j] | (1<<i)
    return None