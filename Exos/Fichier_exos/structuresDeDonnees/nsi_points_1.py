"""Une première implémentation d'un point du plan géométrique."""

# un point est un tuple à deux éléments

import math

# quelques opérations

def creer_point(x : float, y : float) -> tuple:
    """Renvoie un point créé à partir de ses deux coordonnées."""
    return  # à compléter

def distance_origine(point : tuple) -> float:
    """Renvoie la distance à l'origine du point."""
    x, y = point  # dépaquetage du tuple
    return # à compléter

def distance(point1 : tuple, point2 : tuple) -> float:
    """Renvoie la distance entre deux points."""
    # dépaquetage des deux tuples
    x1, y1 = point1
    x2, y2 = point2
    return # à compléter

def image_translation(point : tuple, vecteur : tuple) -> tuple:
    """Renvoie l'image du point par la translation de vecteur."""
    # à compléter
    return (xp + xv, yp + yv)