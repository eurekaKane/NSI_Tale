"""Offre des fonctions pour la gestion d'un ensemble de
    jours de naissances.
"""

def creerEnsemble() -> set:
    """Cette fonction renvoie un ensemble vide.
        Par exemple : ens = creerEnsemble()
    """
    return set()

def estPresent(val, ens : set) -> bool:
    """Cette fonction renvoie la valeur True si la valeur
        val se trouve dans l'ensemble nommé ens créé avec
        la fonction creerEnsemble.
        Par exemple estPresent(45, ens)
    """
    return val in ens

def ajouteElement(val, ens : set) -> None:
    """Cette fonction ajoute la valeur val à l'ensemble
        ens créé avec la fonction creerEnsemble.
        Cet ajout est réalisé en place.
        Par exemple ajouteElement(24, ens)
    """
    ens.add(val)
    return None