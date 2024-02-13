def figure1(n : int) -> None:
    """n est un entier naturel."""
    if n > 0:
        print(n * "*")
        figure1(n - 1)
    return None


def figure2(n : int) -> None:
    """n est un entier naturel."""
    if n > 0:
        figure2(n - 1)
        print(n * "*")
    return None


def figure3(n : int) -> None:
    """n est un entier naturel."""
    for k in range(n, 0, -1):
        print(k * "*")
    return None


def figure4(n : int) -> None:
    """n est un entier naturel."""
    for k in range(1, n + 1):
        print(k * "*")
    return None


def figure5(n : int) -> None:
    """n est un entier naturel."""
    if n > 0:
        figure5(n - 1)
        print(n * "*")
        figure5(n - 1)
    return None


def figure6(n : int) -> None:
    """n est un entier naturel."""
    if n > 1:
        figure6(n - 1)
        print(n * "*")
        figure6(n - 1)
    else:
        print("*")
    return None