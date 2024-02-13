def u(n : int) -> int:
    """Renvoie la valeur du terme u(n).
        Cette fonction est itérative.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # traitement
    a = 0  # terme 0 ou k - 2
    b = 1  # terme 1 ou k - 1
    for _ in range(1, n + 1):  # pour u(k)
        tmp = a
        a = b  # mise à jour de u(k-2)
        b = tmp + b  # calcul u(k-2)+u(k-1)
        # ou a, b = b, a + b
    return a  # renvoie u(n)


def calculeU(n : int) -> int:
    """Renvoie la valeur du terme u(n).
        Cette fonction est récursive.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # traitement
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculeU(n - 2) + calculeU(n - 1)


def calculMemoisation(n : int) -> int:
    """Renvoie la valeur du terme u(n).
        Cette fonction est récursive.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # traitement
    dicoMemo = {0 : 0, 1 : 1}
    # coeur récursif
    def calculeU_rec(n : int) -> int:
        if n > 1 and n not in dicoMemo.keys():
            # premier calcul de u(n)
            dicoMemo[n] = calculeU_rec(n - 2) +\
                          calculeU_rec(n - 1)
        # sinon u(n) a déjà été calculée
        return dicoMemo[n]  # dans tous les cas
    # appel récursif principal
    return calculeU_rec(n)


def calculFonctionnel(n : int) -> int:
    """Renvoie la valeur du terme u(n).
        Cette fonction est récursive.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # coeur récursif
    def calculeU_rec(n : int, a : int,\
                     b : int) -> int:
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            return calculeU_rec(n - 1, b, a + b)
    # appel récursif principal
    return calculeU_rec(n, 0, 1)
        