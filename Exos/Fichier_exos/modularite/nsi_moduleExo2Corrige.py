import random as rd
import nsi_dates as dates
from matplotlib import pyplot as plt

def calculeNombreDates() -> int:
    """Cette fonction renvoie le nombre dates à choisir aléatoirement
        avant de couvrir les 366 possibles.
        Il s'agit d'une expérience aléatoire.
    """
    cpt = 0  # variable compteur
    nbreDatesCouvertes = 0  # nombre de dates couvertes entre 1 et 366
    # traitement
    ens = dates.creerEnsemble()  # création d'un ensemble vide
    while nbreDatesCouvertes < 366:
        cpt += 1  # un choix supplémentaire
        date = rd.randint(1, 366)  # choix aléatoire d'une date
        if not dates.estPresent(date, ens):  # si pas déjà choisie
            nbreDatesCouvertes += 1  # une date couverte de plus
            dates.ajouteElement(date, ens)  # on l'ajoute à l'ensemble
    return cpt

def nombreMoyenEleves(n : int) -> float:
    """Cette fonction renvoie le nombre moyen d'élèves dans une école
        pour fêter chaque jour un anniversaire quand on répète n fois
        l'expérience aléatoire.
        Pré-condition : n est un entier naturel non nul.
    """
    # pré-condition
    assert isinstance(n, int) and n > 0
    # traitement
    acc = 0  # accumulateur
    for _ in range(n):
        acc = acc + calculeNombreDates()
    return acc / n

def repeteExperience(n : int) -> list:
    """Cette fonction répète n fois l'expérience aléatoire
        modélisée par la fonction calculeNombreDates et
        renvoie les résultats dans un tableau.
        Pré-condition : n est un entier naturel non nul.
    """
    # pré-condition
    assert isinstance(n, int) and n > 0
    # traitement
    return [calculeNombreDates() for _ in range(n)]

def produitHistogramme(listeEntiers : list) -> None:
    """Cette fonction produit un histogramme à partir d'une
        liste de nombres entiers naturels non nuls.
        Pré-condition :
            listeDates est un tableau non vide.
        Post-condition :
            l'instruction plt.show() affiche l'histogramme.
    """
    # pré-condition
    assert isinstance(listeEntiers, list) and\
           len(listeEntiers) != 0
    # traitement
    plt.hist(listeEntiers, bins = 30, edgecolor = 'black',\
             color = 'red')
    return None
