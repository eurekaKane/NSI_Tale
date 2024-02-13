
def _fusion(tab1 : list, tab2 : list) -> list:
    """Cette fonction renvoie le tableau trié résultant de la
        fusion des tableaux tab1 et tab2 dont les valeurs sont
        rangées dans l'ordre croissant.
    """
    # initialisation du tableau dans lequel aura lieu la fusion.
    result = []
    i2 = 0  # indice de parcours de tab2
    for i1 in range(len(tab1)):  # parcours complet de tab1
        # fusion maximale de tab2 avec garde
        while i2 < len(tab2) and tab2[i2] < tab1[i1]:
            result.append(tab2[i2])
            i2 = i2 + 1
        result.append(tab1[i1])
    # ajout des éléments de tab2 non fusionnés
    for i in range(i2, len(tab2)):
        result.append(tab2[i])
    return result


# Algorithme récursif du tri par partition-fusion
def triFusion(tab : list) -> list:
    """Cette fonction renvoie un tableau composé des éléments
        de tab dont les valeurs ont été triées en ordre croissant.
        Elle met en œuvre l'algorithme du tri fusion.
        Elle est récursive.
    """
    # pré-condition
    assert isinstance(tab, list), "L'argument est un tableau."
    # moteur récursif
    def mergeSort_rec(tab : list) -> list:
        if len(tab) <= 1:
            return tab  # régner
        else:
            # diviser
            i = len(tab) // 2
            tabGauche = [tab[k] for k in range(i)]
            tabDroit = [tab[k] for k in range(i, len(tab))]
            # appels récursifs régner
            tabGaucheTrie = mergeSort_rec(tabGauche)  
            tabDroitTrie = mergeSort_rec(tabDroit)
            # combiner
            return _fusion(tabGaucheTrie, tabDroitTrie)  
    # appel principal
    return mergeSort_rec(tab)