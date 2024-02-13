import turtle as trt

def dragon(n : int, s : int = 1) -> None:
    """Cette fonction dessine une courbe du dragon
        de taille n.
        Elle est récursive.
    """
    if n == 0:
        trt.forward(5)
    else:
        dragon(n - 1, 1)
        trt.right(s * 90)
        dragon(n - 1, -1)
    return None

if __name__ == "__main__":
    trt.speed('fastest')
    dragon(8)
    trt.hideturtle()
    trt.done()