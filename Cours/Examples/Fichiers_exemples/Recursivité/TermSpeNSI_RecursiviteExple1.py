def rebours_rec(n : int) -> None:
    """Cette fonction récursive affiche un compte à rebours.
    La valeur de n doit être un entier naturel.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0 
    # traitement
    print(n, end = " ; ")  # affichage
    if n == 0:
        print("Partez !")
    else:
        rebours_rec(n - 1)  # appel récursif
    return None

rebours_rec(3)