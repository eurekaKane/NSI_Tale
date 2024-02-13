# fonction utilitaire
def est_trie(tab : list) -> bool:
    """Cette fonction renvoie la valeur True si les valeurs des éléments
        du tableau tab sont rangées en ordre croissant et False sinon.
    """
    n = len(tab)
    for i in range(1, n):
        if tab[i] < tab[i-1]:
            return False
    return True


# recherche dichotomique version itérative
def rechercheDichotomique(val, tab : list) -> bool:
    """Cette fonction renvoie True si la valeur de val est
        présente dans le tableau tab.
        La valeur de val est supposée d'un type comparable
        avec celui ou ceux des éléments de tab.
        Le tableau tab est supposé trié.
    """
    # pré-conditions
    assert isinstance(tab, list)
    assert est_trie(tab)
    # traitement
    n = len(tab)
    g = 0
    d = n - 1
    while g <= d:
        m = (g + d) // 2
        if tab[m] > val:
            d = m - 1  # val est à gauche
        elif tab[m] < val:
            g = m + 1  # val est à droite
        else:
            return True  # val trouvée à l'indice m
    return False  # val absente du tableau


# recherche dichotomique version récursive
def rechercheDichotomique_rec(val, tab : list) -> bool:
    """Cette fonction renvoie True si la valeur de val est
        présente dans le tableau tab.
        La valeur de val est supposée d'un type comparable
        avec celui ou ceux des éléments de tab.
        Le tableau tab est supposé trié.
        Cette fonction est récursive.
    """
    # pré-conditions
    assert isinstance(tab, list)
    assert est_trie(tab)
    # coeur récursif
    def findDico_rec(val, tab : list, g : int, d : int) -> bool:
        if g <= d:
            m = (g + d) // 2
            if tab[m] > val:  # val est à gauche
                return findDico_rec(val, tab, g, m - 1)
            elif tab[m] < val:  # val est à droite
                return findDico_rec(val, tab, m + 1, d)
            else:  # val est trouvée
                return True
        # sinon val est absente
        return False
    return findDico_rec(val, tab, 0, len(tab) - 1)