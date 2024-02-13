from typing import Tuple
import turtle as trt

# des fonctions utilitaires

def traceAngleDroit(L : int, l : int) -> None:
    """Cette fonction trace un angle droit par un déplacement
        horizontal de L pixels puis vertical à gauche de l pixels.
        L'orientation de la tortue est modifiée.
        L et l sont deux entiers naturels.
    """
    trt.forward(L)  # avancer de L pixels
    trt.left(90)  # tourner à gauche de 90° relativement à la direction courante
    trt.forward(l)  # avancer de l pixels
    return None

def deplaceTortue(vec : Tuple[int, int]) -> None:
    """Cette fonction déplace la position courante
        du vecteur de coordonnées vec dans la
        direction courante.
        L'orientation de la tortue est conservée.
        vec est un tuple de deux entiers relatifs.
    """
    x, y = vec
    trt.penup()  # lever le crayon
    trt.forward(x)  # avancer de x pixels
    trt.left(90)  # tourner à gauche de 90° relativement à la direction courante
    trt.forward(y)  # avancer de y pixels
    trt.right(90)  # rétablissement de l'orientation courante
    trt.pendown()  # poser le crayon
    return None

def traceRectangle(L : int, l : int) -> None:
    """Cette fonction trace un rectangle de largeur L et de
        hauteur l avec le coin inférieur gauche à la position
        courante et dans la direction courante.
        L'orientation de la tortue est conservée.
        L et l sont deux entiers naturels.
    """
    for _ in range(2):
        traceAngleDroit(L, l)  # dessin d'un angle droit
        trt.left(90)  # tourne de 90° à gauche par rapport à la direction courante
    return None

def dessineMarche(L : int, l : int, couleur : str) -> None:
    """Cette fonction dessine un rectangle plein de la couleur couleur, de largueur
        L et de hauteur l avec le coin inférieur gauche à la position courante
        et dans la direction courante.
        L'orientation de la tortue est conservée.
        L et l sont deux entiers naturels.
        couleur est le code hexadécimal de la couleur comme chaîne de caractères.
    """
    trt.color(couleur)  # couleur tracé et remplissage
    trt.begin_fill()  # début du remplissage
    traceRectangle(L, l)  # tracé du rectangle à remplir
    trt.end_fill()  # fin du remplissage
    return None

# pour dessiner un escalier
def escalier1(n : int, L : int = 30, l : int = 15) -> None:
    """Cette fonction dessine n marches simples de largeur L et de hauteur l.
        L'orientation de la tortue est conservée.
        Cette fonction est récursive.
    """
    # pré-conditions sur n
    assert isinstance(n, int) and n >= 0
    # moteur récursif
    def escalier_rec(n : int) -> None:
        if n > 0:
            traceAngleDroit(L, l)  # dessiner un angle droit de L sur l
            trt.right(90)  # tourner de 90° à droite relativement à la direction courante
            escalier_rec(n - 1)  # appel récursif
        return None
    # appel principal
    escalier_rec(n)
    return None

def escalier2(n : int, L : int = 30, l : int = 15, couleur : str = "#008080") -> None:
    """Cette fonction dessine un escalier de n marches de largeur L et de hauteur l
        dans la couleur couleur.
        L'orientation de la tortue est conservée.
        Elle est récursive.
    """
    # pré-conditions sur n
    assert isinstance(n, int) and n >= 0
    # moteur récursif
    def escalier_rec(n : int) -> None:
        if n > 0:
            dessineMarche(L, l, couleur)  # dessiner une marche de L sur l en couleur
            deplaceTortue((L // 2, l))  # déplacer la tortue au milieu du côté supérieur
            escalier_rec(n - 1)  # appel récursif
        return None
    # appel récursif principal
    escalier_rec(n)
    return None


# programme principal
if __name__ == "__main__":
    trt.setheading(0)  # pour orienter la tortue vers la droite
    trt.screensize(400, 400)  # pour définir la taille de la fenêtre
    deplaceTortue((-180, -180))  # pour déplacer la tortue au pixel de coordonnées (-180, -180)
    escalier2(6)  # un escalier de 6 marches
    deplaceTortue((-180, 200))
    escalier1(4)  # un escalier simple de 4 marches
    trt.done()  # gestion de la boucle d'évènements