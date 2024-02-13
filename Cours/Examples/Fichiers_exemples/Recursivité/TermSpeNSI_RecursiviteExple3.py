from typing import Tuple
import turtle as trt

# des fonctions utilitaires

def traceAngleDroit(L : int, l : int) -> None:
    """Cette fonction trace un angle droit par un déplacement
        horizontal de L pixels puis vertical à gauche de l pixels.
        L'orientation de la tortue est modifiée.
        L et l sont deux entiers naturels.
    """
    trt.forward(L)
    trt.left(90)
    trt.forward(l)
    return None

def deplaceTortue(vec : Tuple[int, int]) -> None:
    """Cette fonction déplace la position courante
        du vecteur de coordonnées vec.
        L'orientation de la tortue est conservée.
        vec est un tuple de deux entiers relatifs.
    """
    x, y = vec
    trt.penup()
    traceAngleDroit(x, y)
    trt.right(90)  # rétablissement de l'orientation
    trt.pendown()
    return None

def traceRectangle(L : int, l : int) -> None:
    """Cette fonction trace un rectangle de largeur L et de
        hauteur l avec le coin inférieur gauche à la position
        courante et dans la direction courante.
        L'orientation de la tortue est conservée.
        L et l sont deux entiers naturels.
    """
    for _ in range(2):
        traceAngleDroit(L, l)
        trt.left(90)
    return None

def dessineMarche(L : int, l : int, couleur : str) -> None:
    """Cette fonction dessine un rectangle plein de la couleur couleur, de largueur
        L et de hauteur l avec le coin inférieur gauche à la position courante
        et dans la direction courante.
        L'orientation de la tortue est conservée.
        L et l sont deux entiers naturels.
        couleur est le code hexadécimal de la couleur comme chaîne de caractères.
    """
    trt.color(couleur)
    trt.begin_fill()
    traceRectangle(L, l)
    trt.end_fill()
    return None

# pour dessiner un escalier
def escalier1(n : int, L : int = 30, l : int = 15) -> None:
    """Cette fonction dessine n marches simples de largeur L et de hauteur l.
        L'orientation de la tortue est conservée.
        Cette fonction est récursive.
    """
    assert isinstance(n, int) and n >= 0  # pré-conditions sur n
    if n > 0:
        traceAngleDroit(L, l)
        trt.right(90)
        escalier1(n - 1)
    return None

def escalier2(n : int, L : int = 30, l : int = 15, couleur : str = "#008080") -> None:
    """Cette fonction dessine un escalier de n marches de largeur L et de hauteur l
        dans la couleur couleur.
        L'orientation de la tortue est conservée.
        Elle est récursive.
    """
    assert isinstance(n, int) and n >= 0  # pré-conditions sur n
    if n > 0:
        dessineMarche(L, l, couleur)
        deplaceTortue((L // 2, l))
        escalier2(n - 1)  # appel récursif
    return None

if __name__ == "__main__":
    escalier1(3)
    trt.done()