"""Une première implémentation d'une pile."""

# avec un tableau dynamique

def creer_pile() -> list:
    """Renvoie une pile vide."""
    return []

def est_pile_vide(pile : list) -> bool:
    """Renvoie True si la pile est vide, False sinon."""
    return len(pile) == 0

def taille_pile(pile : list) -> int:
    """Renvoie le nombre d'éléments de la pile."""
    return len(pile)

def empiler(elt, pile : list) -> None:
    """Empile l'élément elt dans la pile.
        Réalisation en place.
    """
    pile.append(elt)
    return None

def depiler(pile : list):
    """Renvoie le sommet de la pile supposée non vide et le retire."""
    # pré-condition
    assert not est_pile_vide(pile), "La pile est vide !"
    # traitement
    return pile.pop()

def sommet(pile : list):
    """Renvoie le sommet de la pile supposée non vide sans le retirer."""
    # pré-condition
    assert not est_pile_vide(pile), "La pile est vide !"
    # traitement
    return pile[len(pile)-1]  # par indice du dernier élément

def afficher_pile(pile : list) -> str:
    """Affiche les éléments de la pile du bas au sommet."""
    result = ""
    for elt in pile:  # parcours par valeurs
        result += str(elt) + " | "  # modification en place
    return result[:-3]  # pas d'affichage des 3 derniers caractères

def enumerer_pile(pile : list) -> list:
    """Renvoie une valeur énumérable pour parcourir
        les éléments de la pile du sol au sommet.
    """
    # définition d'un tableau dynamique en compréhension
    return [elt for elt in pile]  # parcours par valeurs