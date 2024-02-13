def sommeEntiers(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est itérative.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # traitement
    acc = 0  # un accumulateur de somme
    for k in range(1, n + 1):
        acc = acc + k
    return acc

# pour suivre avec le débogueur
sommeEntiers(3)


def sommeEntiers_rec(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est récursive.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # appel récursif
    if n > 0:
        return sommeEntiers_rec(n - 1) + n
    else:
        return 0  # cas de base

# pour suivre avec le débogueur
sommeEntiers_rec(3)


def _somme_rec(n : int) -> int:
    """Cette fonction est le cœur récursif de la fonction somme.
        Elle est encapsulée.
    """
    if n > 0:
        return _somme_rec(n - 1) + n
    else:
        return 0

def somme(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est récursive.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # appel récursif principal
    return _somme_rec(n)

# pour suivre avec le débogueur
somme(3)


def somme2(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est récursive.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # moteur récursif interne
    def somme_rec(n : int) -> int:
        if n > 0:
            return somme_rec(n - 1) + n
        else:
            return 0
    # appel récursif principal
    return somme_rec(n)

# pour suivre avec le débogueur
somme2(3)


def somme3(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est récursive terminale.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # moteur récursif interne
    def somme_rec(n : int, acc : int) -> int:
        if n > 0:  # descente et calcul
            return somme_rec(n - 1, acc + n)
        else:  # renvoi valeur accumulateur
            return acc  # cas de base
    # appel récursif principal
    return somme_rec(n, 0)  # acc initialisé à 0

# pour suivre avec le débogueur
somme3(3)