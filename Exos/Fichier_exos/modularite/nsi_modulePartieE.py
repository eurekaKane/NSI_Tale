"""Offre des fonctions pour la gestion d'un ensemble de
    jours de naissances.
"""

def creerEnsemble() -> list:
    """Cette fonction renvoie un ensemble vide.
        Par exemple : ens = creerEnsemble()
    """
    # une table de hachage à 23 éléments
    return [[] for _ in range(23)]  # tableaux dynamiques vides

def estPresent(val, ens : list) -> bool:
    """Cette fonction renvoie la valeur True si la valeur
        val se trouve dans l'ensemble nommé ens créé avec
        la fonction creerEnsemble.
        Par exemple estPresent(45, ens)
    """
    h = val % 23  # haché de elt
    for elt in ens[h]:  # parcours des collisions
        if elt == val:
            return True
    return False

def ajouteElement(val, ens : list) -> None:
    """Cette fonction ajoute la valeur val à l'ensemble
        ens créé avec la fonction creerEnsemble.
        Cet ajout est réalisé en place.
        Par exemple ajouteElement(24, ens)
    """
    h = val % 23  # haché de elt
    ens[h].append(val)  # ajout aux collisions
    return None