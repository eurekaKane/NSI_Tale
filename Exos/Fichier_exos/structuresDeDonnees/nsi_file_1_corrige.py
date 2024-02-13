"""Une première implémentation d'une file."""

# avec un tableau et un attribut de suivi du remplissage
# une File est un tuple à deux éléments : 1 tableau de taille fixée n
# et 1 indice d'insertion de l'élément suivant à enfiler
# la tête est en indice 0 si la file n'est pas vide

def creer_file(n : int) -> tuple:
    """Renvoie une file vide de taille maximum égale à n."""
    # pré-condition
    assert isinstance(n, int) and n > 0, "La taille maximum est un entier non nul."
    # traitement
    return ([None]*n, 0)  # la File est vide

def est_file_vide(file : tuple) -> bool:
    """Renvoie True si la file est vide, False sinon."""
    _, ind_ins = file  # dépaquetage du tuple
    return ind_ins == 0  # prochaîne insertion à 0

def est_file_pleine(file : tuple) -> bool:
    """Renvoie True si la file est pleine, False sinon."""
    tab, ind_ins = file  # dépaquetage du tuple
    return ind_ins == len(tab)

def taille_file(file : tuple) -> int:
    """Renvoie le nombre d'éléments de la file."""
    _, ind_ins = file  # dépaquetage du tuple
    return ind_ins  # car on commence à 0

def enfiler(elt, file : tuple) -> tuple:
    """Enfile l'élément elt en queue de la file si elle n'est pas pleine.
        Renvoie un nouvel objet.
    """
    # pré-condition
    assert not est_file_pleine(file), "La file est pleine !"
    # traitement
    tab, ind_ins = file  # dépaquetage du tuple
    tab[ind_ins] = elt  # ajout du nouvel élément
    return (tab, ind_ins + 1)  # nouvelle file, incrémentation de l'indice

def defiler(file : tuple) -> tuple:
    """Renvoie une nouvelle file en supprimant le sommet de la
        pile supposée non vide passée en argument."""
    # pré-condition
    assert not est_file_vide(file), "La file est vide !"
    # traitement
    tab, ind_ins = file  # dépaquetage du tuple
    for i in range(1, ind_ins):
        tab[i - 1] = tab[i]  # décalage de chaque élément vers l'indice 0
    return (tab, ind_ins - 1)  # nouvelle file, décrémentation de l'indice

def tete(file : tuple):
    """Renvoie la tête de la file supposée non vide sans le retirer."""
    # pré-condition
    assert not est_file_vide(file), "La file est vide !"
    # traitement
    tab, _ = file  # dépaquetage du tuple
    return tab[0]  # la tête est à l'indice 0

def afficher_file(file : tuple) -> str:
    """Affiche les éléments de la file de la queue à la tête."""
    tab, ind_ins = file  # dépaquetage du tuple
    result = "|"
    for i in range(ind_ins):  # parcours par indice
        result = "| " + str(tab[i]) + " " + result  # modification en place
    if ind_ins == 0:  # si la file est vide
        result = ""  # renvoi d'une chaîne vide
    return result  # renvoi de la chaîne de caractères
