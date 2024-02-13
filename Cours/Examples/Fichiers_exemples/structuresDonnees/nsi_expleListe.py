"""Un exemple d'implémentation d'une structure de Liste."""

# avec des variables emboîtées de type tuple

def creer_liste() -> tuple:
    """Renvoie une liste vide."""
    return ()

def est_liste_vide(liste : tuple) -> bool:
    """Renvoie True si liste est vide, False sinon."""
    return liste == ()

def inserer(elt, liste : tuple) -> tuple:
    """Renvoie une nouvelle liste après insertion de elt
        en tête de liste.
    """
    return (elt, liste)  # emboîtement

def tete(liste : tuple):
    """Renvoie la valeur de la tête de liste si celle-ci
        n'est pas vide.
    """
    # pré-condition
    assert not est_liste_vide(liste), "La liste est vide !"
    # traitement
    elt, _ = liste  # dépaquetage du tuple
    return elt

def reste(liste : tuple) -> tuple:
    """Renvoie une nouvelle liste constituée des éléments de
        liste sauf sa tête si liste n'est pas vide.
    """
    # pré-condition
    assert not est_liste_vide(liste), "La liste est vide !"
    # traitement
    _, lst = liste  # dépaquetage du tuple
    return lst

def afficher(liste : tuple) -> str:
    """Affiche les éléments de la file de la queue à la tête."""
    lst = liste  # pour parcourir
    result = "|"
    while not est_liste_vide(lst):
        elt, lst = lst  # dépaquetage et ré-affectation
        result += " " + str(elt) + " |"
    if est_liste_vide(liste):
        result += "|"  # on renvoie alors '||'
    return result  # renvoi de la chaîne de caractères

def enumerer(liste : tuple) -> list:
    """Renvoie une variable d'un type Python permettant le
        parcours de la liste avec la construction in.
    """
    lst = liste  # pour parcourir
    enum = []  # tableau dynamique vide
    while not est_liste_vide(lst):
        elt, lst = lst  # dépaquetage et ré-affectation
        enum.append(elt)  # ajout
    return enum

def taille(liste : tuple) -> int:
    """Renvoie le nombre d'éléments de la liste."""
    lst = liste  # pour parcourir
    cpt = 0  # initialisation du compteur
    while not est_liste_vide(lst):
        _, lst = lst  # dépaquetage et ré-affectation
        cpt = cpt + 1  # incrémentation du compteur
    return cpt

def ieme_element(ind : int, liste : tuple):
    """Renvoie la valeur de l'élément de liste d'indice ind
        si ind est un indice valide.
    """
    # pré-condition
    assert isinstance(ind, int)\
           and ind >= 0 and ind < taille(liste)\
           , "La valeur de l'indice est invalide."
    # traitement
    lst = liste  # pour parcourir
    ind_parcours = 0
    while ind_parcours <= ind:
        elt, lst = lst  # dépaquetage et ré-affectation
        ind_parcours = ind_parcours + 1
    return elt

def ajouter(elt, liste : tuple) -> tuple:
    """Renvoie une nouvelle liste après avoir ajouter elt à
        la fin de liste.
    """
    tmp = enumerer(liste)  # pour énumérer
    n = taille(liste)  # nombre initial d'éléments
    result = creer_liste()  # pour le résultat
    result = inserer(elt, result)  # en dernier
    for i in range(n):
        # parcours inverse de l'énumérateur
        result = inserer(tmp[n - 1 - i], result)
    return result

def inserer_ieme(elt, ind : int, liste : tuple) -> tuple:
    """Renvoie une nouvelle liste après avoir insérer elt
        comme i-ième élément à ind dans liste si cet indice
        est valide.
    """
    # pré-condition
    assert isinstance(ind, int)\
           and ind > 0 and ind < taille(liste)\
           , "La valeur de l'indice est invalide."
    # traitement
    lst = liste  # pour parcourir et renvoyer
    ind_parcours = 0
    tmp = [None] * ind  # pour stocker les éléments précédents
    while ind_parcours < ind:
        val, lst = lst  # dépaquetage et ré-affectation
        tmp[ind - 1 - ind_parcours] = val  # stockage inverse
        ind_parcours = ind_parcours + 1
    # insertion dans lst qui contient la queue du résultat
    lst = inserer(elt, lst)
    # destockage dans le bon ordre
    for val in tmp:
        lst = inserer(val, lst)
    return lst

def substituer(elt, ind : int, liste : tuple) -> tuple:
    """Renvoie une nouvelle liste après avoir substituer elt
        à la valeur du i-ième élément à ind dans liste si
        cet indice est valide.
    """
    # pré-condition
    assert isinstance(ind, int)\
           and ind >= 0 and ind < taille(liste)\
           , "La valeur de l'indice est invalide."
    # traitement
    lst = liste  # pour parcourir et renvoyer
    ind_parcours = 0
    tmp = [None] * ind  # pour stocker les éléments précédents
    while ind_parcours < ind:
        val, lst = lst  # dépaquetage et ré-affectation
        tmp[ind - 1 - ind_parcours] = val  # stockage inverse
        ind_parcours = ind_parcours + 1
    # récupération de la queue de lst et ré-affectation
    lst = reste(lst)
    # nouvelle tête pour lst
    lst = inserer(elt, lst)
    # destockage dans le bon ordre
    for val in tmp:
        lst = inserer(val, lst)
    return lst

def supprimer(ind : int, liste : tuple) -> tuple:
    """Renvoie une nouvelle liste après suppression de
        l'élément d'indice ind dans liste si cet indice est
        valide.
    """
    # pré-condition
    assert isinstance(ind, int)\
           and ind >= 0 and ind < taille(liste)\
           , "La valeur de l'indice est invalide."
    # traitement
    lst = liste  # pour parcourir et renvoyer
    ind_parcours = 0
    tmp = [None] * ind  # pour stocker les éléments précédents
    while ind_parcours < ind:
        val, lst = lst  # dépaquetage et ré-affectation
        tmp[ind - 1 - ind_parcours] = val  # stockage inverse
        ind_parcours = ind_parcours + 1
    # récupération de la queue de lst et ré-affectation
    lst = reste(lst)
    # destockage dans le bon ordre
    for val in tmp:
        lst = inserer(val, lst)
    return lst