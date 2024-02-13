import turtle as trt

def arbreEnY(nbNiv : int, taille : float = 80.0, angle : int = 30) -> None:
    """Cette fonction construit un arbre fractal en Y sur nbNiv niveaux.
        L'arbre de niveau 1 a la taille initiale et l'angle des deux
        branches a pour valeur angle.
        Cette fonction utilise le module turtle avec l'alias trt.
    """
    # pré-conditions
    assert isinstance(nbNiv, int) and nbNiv >= 0
    # traitement
    if nbNiv >= 1:
        trt.forward(taille)  # la tortue avance de taille
        # branche de droite
        trt.right(angle)  # elle tourne vers la droite de angle
        arbreEnY(nbNiv - 1, taille * 0.8)  # appel récursif 1
        # branche de gauche
        trt.left(2 * angle)  # la tortue tourne à gauche de 2 fois angle
        arbreEnY(nbNiv - 1, taille * 0.8)  # appel récursif 2
        # positionnement de la tortue en sortie
        trt.right(angle)  # la tortue est redressée
        trt.back(taille)  # elle recule d'un niveau
    return None

if __name__ == "__main__":
    trt.colormode(255)
    trt.speed('fastest')
    trt.right(-90)
    trt.pendown()
    arbreEnY(3)
    trt.hideturtle()
    trt.done()