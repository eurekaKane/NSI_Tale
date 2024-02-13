def factorielle_rec(n : int) -> int:
    """Cette fonction renvoie la valeur de n! où
    n est un entier naturel.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # traitement
    if n <= 1:
        return 1  # on renvoie 1
    else:
        return n * factorielle_rec(n - 1)  # on renvoie n * u(n-1)
    
factorielle_rec(3)


def factorielle_rec_1(n : int) -> int:
    """Cette fonction renvoie la valeur de n! où
    n est un entier naturel.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # traitement
    if n <= 1:
        return 1  # on renvoie 1
    else:
        return factorielle_rec_1(n - 1) * n  # on renvoie n * u(n-1)
    
factorielle_rec_1(3)


def factorielle_rec_2(n : int, acc : int = 1) -> int:
    """Cette fonction renvoie la valeur de n! où
    n est un entier naturel.
    acc est un accumulateur multiplicatif qui renverra
    le résultat.
    Cette fonction est récursive terminale.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # traitement
    if n <= 1:
        # on renvoie la valeur de acc
        return acc
    else:
        # on appelle la fonction en effectuant le produit
        return factorielle_rec_2(n - 1, acc * n)

factorielle_rec_2(3)

def factorielle_rec_3(n : int) -> int:
    """Cette fonction renvoie la valeur de n! où
    n est un entier naturel.
    Elle est récursive terminale.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # moteur récursif
    def fact_rec(n : int, acc : int) -> int:
        if n <= 1:
            # on renvoie la valeur de acc
            return acc
        else:
            # on appelle la fonction en effectuant le produit
            return fact_rec(n - 1, acc * n)
    # appel principal
    return fact_rec(n, 1)  # acc initialisé à 1

factorielle_rec_3(3)