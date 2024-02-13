"""Une première implémentation d'un point du plan géométrique."""

# un point est un tuple à deux éléments

import math

# quelques opérations

def creer_point(x : float, y : float) -> tuple:
    """Renvoie un point créé à partir de ses deux coordonnées."""
    return (x, y)  # renvoi du tuple formé des deux coordonnées

def distance_origine(point : tuple) -> float:
    """Renvoie la distance à l'origine du point."""
    x, y = point  # dépaquetage du tuple
    return math.sqrt(x**2 + y**2)  # calcul de la distance

def distance(point1 : tuple, point2 : tuple) -> float:
    """Renvoie la distance entre deux points."""
    # dépaquetage des deux tuples
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )  # calcul de la distance

def image_translation(point : tuple, vecteur : tuple) -> tuple:
    """Renvoie l'image du point par la translation de vecteur."""
    # dépaquetage du point et du vecteur
    xp, yp = point
    xv, yv = vecteur
    return (xp + xv, yp + yv)  # calcul et renvoi du point image