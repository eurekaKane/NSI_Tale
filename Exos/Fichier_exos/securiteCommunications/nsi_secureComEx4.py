def seuil(q : float, s : float) -> int:
    """Renvoie la première valeur de n un entier naturel
        pour laquelle q puissance n est inférieur à s.
        Pré-conditions : 0 < q < 1 et 0 < s <= 1
    """
    # pré-conditions
    assert q > 0 and q < 1
    assert s > 0 and s <= 1
    # traitement
    n = 0
    while q**n > s:
        n = n + 1
    return n

# programme principal
if __name__ == "__main__":
    print([seuil(0.5, s) for s in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]])
