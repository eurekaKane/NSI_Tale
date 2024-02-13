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
        # à compléter


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
        # à compléter
        
    # appel récursif principal
    return  # à compléter