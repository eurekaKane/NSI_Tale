"""Une deuxième implémentation d'une file."""

# avec deux piles de taille maximale non fixée
# une File est un tuple à 2 éléments qui sont 2 piles

from nsi_pile_1_corrige import *

# une fonction utilitaire

def transpiler(file : tuple) -> None:
    """Transpile les éléments de la pile d'ajouts dans
        celle de retrait.
        Modification en place.
    """
    pileIn, pileOut = file  # dépaquetage du tuple
    while not est_pile_vide(pileIn):
        empiler(depiler(pileIn), pileOut)
    return None

# les fonctions de l'interface

def creer_file() -> tuple:
    """Renvoie une file vide."""
    # traitement
    return (creer_pile(), creer_pile())  # la File est vide

def est_file_vide(file : tuple) -> bool:
    """Renvoie True si la file est vide, False sinon."""
    pileIn, pileOut = file  # dépaquetage du tuple
    return est_pile_vide(pileIn) and est_pile_vide(pileOut)

def taille_file(file : tuple) -> int:
    """Renvoie le nombre d'éléments de la file."""
    pileIn, pileOut = file  # dépaquetage du tuple
    return taille_pile(pileIn) + taille_pile(pileOut)

def enfiler(elt, file : tuple) -> None:
    """Enfile l'élément elt en queue de la file si elle n'est pas pleine.
        Modification en place.
    """
    # traitement
    pileIn, _ = file  # dépaquetage du tuple
    empiler(elt, pileIn)  # en place
    return None

def defiler(file : tuple) -> None:
    """Renvoie la tête de la file supposée non vide passée
        en argument.
    """
    # pré-condition
    assert not est_file_vide(file), "La file est vide !"
    # traitement
    _, pileOut = file  # dépaquetage du tuple
    if est_pile_vide(pileOut):
        transpiler(file)
    # là il est certain que pileOut n'est pas vide
    return depiler(pileOut)

def tete(file : tuple):
    """Renvoie la tête de la file supposée non vide sans le retirer.
        La file peut être modifiée en place.
    """
    # pré-condition
    assert not est_file_vide(file), "La file est vide !"
    # traitement
    _, pileOut = file  # dépaquetage du tuple
    if est_pile_vide(pileOut):
        transpiler(file)  # opérations en place
    return sommet(pileOut)  # la tête est au sommet des retraits

def afficher_file(file : tuple) -> str:
    """Affiche les éléments de la file de la queue à la tête."""
    pileIn, pileOut = file  # dépaquetage du tuple
    result = "|"
    for elt in enumerer_pile(pileOut):
        result += " " + str(elt) + " |" # ajout à droite
    for elt in enumerer_pile(pileIn):
        result = "| " + str(elt) + " " + result  # ajout à gauche
    if est_file_vide(file):
        result = ""
    return result  # renvoi de la chaîne de caractères
