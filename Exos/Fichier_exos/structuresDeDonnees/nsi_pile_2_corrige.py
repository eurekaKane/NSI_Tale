"""Une deuxième implémentation d'une pile."""

# avec un tableau et un attribut de suivi du remplissage
# une Pile est un tuple à deux éléments : 1 tableau de taille fixée n
# et 1 indice d'insertion de l'élément suivant à empiler

def creer_pile(n : int) -> tuple:
    """Renvoie une pile vide de taille maximum égale à n."""
    # pré-condition
    assert isinstance(n, int) and n > 0, "La taille maximum est un entier non nul."
    # traitement
    return ([None]*n, 0)  # la Pile est vide

def est_pile_vide(pile : tuple) -> bool:
    """Renvoie True si la pile est vide, False sinon."""
    _, ind_ins = pile  # dépaquetage du tuple
    return ind_ins == 0

def est_pile_pleine(pile : tuple) -> bool:
    """Renvoie True si la pile est pleine, False sinon."""
    tab, ind_ins = pile  # dépaquetage du tuple
    return ind_ins == len(tab)

def taille_pile(pile : tuple) -> int:
    """Renvoie le nombre d'éléments de la pile."""
    _, ind_ins = pile  # dépaquetage du tuple
    return ind_ins

def empiler(elt, pile : tuple) -> tuple:
    """Empile l'élément elt dans la pile si elle n'est pas pleine.
        Renvoie un nouvel objet.
    """
    # pré-condition
    assert not est_pile_pleine(pile), "La pile est pleine !"
    # traitement
    tab, ind_ins = pile  # dépaquetage du tuple
    tab[ind_ins] = elt  # ajout du nouvel élément
    return (tab, ind_ins + 1)  # nouvelle pile, incrémentation de l'indice

def depiler(pile : tuple) -> tuple:
    """Renvoie une nouvelle pile en supprimant le sommet de la
        pile supposée non vide passée en argument."""
    # pré-condition
    assert not est_pile_vide(pile), "La pile est vide !"
    # traitement
    tab, ind_ins = pile  # dépaquetage du tuple
    return (tab, ind_ins - 1)  # nouvelle pile, décrémentation de l'indice

def sommet(pile : tuple):
    """Renvoie le sommet de la pile supposée non vide sans le retirer."""
    # pré-condition
    assert not est_pile_vide(pile), "La pile est vide !"
    # traitement
    tab, ind_ins = pile  # dépaquetage du tuple
    return tab[ind_ins - 1]  # le sommet est à l'indice précédent

def afficher_pile(pile : tuple) -> str:
    """Affiche les éléments de la pile du bas au sommet."""
    tab, ind_ins = pile  # dépaquetage du tuple
    result = ""
    for i in range(ind_ins - 1):  # parcours par indice
        result += str(tab[i]) + " | "  # modification en place
    if ind_ins > 0:  # si la pile n'est pas vide
        result += str(tab[ind_ins - 1])  # ajout du dernier élément
    return result  # renvoi de la chaîne de caractères