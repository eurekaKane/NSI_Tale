"""Une seconde implémentation d'un point du plan géométrique."""

# un point est un tableau à deux éléments

import math

# quelques opérations

def creer_point(x : float, y : float) -> list:
    """Renvoie un point créé à partir de ses deux coordonnées."""
    return [x, y]  # renvoi du tableau formé des deux coordonnées

def distance_origine(point : list) -> float:
    """Renvoie la distance à l'origine du point."""
    x, y = point[0], point[1]  # extraction des coordonnées
    return math.sqrt(x**2 + y**2)  # calcul de la distance

def distance(point1 : list, point2 : list) -> float:
    """Renvoie la distance entre deux points."""
    # extraction des coordonnées pour les deux points
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )  # calcul de la distance

def image_translation(point : list, vecteur : list) -> list:
    """Renvoie l'image du point par la translation de vecteur."""
    # extraction des coordonnées du point et du vecteur
    xp, yp = point[0], point[1]
    xv, yv = vecteur[0], vecteur[1]
    return [xp + xv, yp + yv]  # calcul et renvoi du point image