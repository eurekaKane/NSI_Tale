"""Offre des fonctions pour la gestion d'un ensemble de
    jours de naissances.
"""

def creerEnsemble() -> list:
    """Cette fonction renvoie un ensemble vide.
        Par exemple : ens = creerEnsemble()
    """
    return [False]*367  # 367 booléens à False

def estPresent(val, ens : list) -> bool:
    """Cette fonction renvoie la valeur True si la valeur
        val se trouve dans l'ensemble nommé ens créé avec
        la fonction creerEnsemble.
        Par exemple estPresent(45, ens)
    """
    return ens[val]

def ajouteElement(val, ens : list) -> None:
    """Cette fonction ajoute la valeur val à l'ensemble
        ens créé avec la fonction creerEnsemble.
        Cet ajout est réalisé en place.
        Par exemple ajouteElement(24, ens)
    """
    ens[val] = True
    return None