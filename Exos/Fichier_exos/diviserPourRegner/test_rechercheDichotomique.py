"""Module de tests génériques associé au module nsi_rechercheDichotomique.py"""

from nsi_rechercheDichotomique import rechercheDichotomique as func


# fonctions de test
def test_recherche1():
    tab = []
    val = 1
    assert not func(val, tab)


def test_recherche2():
    tab = [8]
    val = 1
    assert not func(val, tab)


def test_recherche3():
    tab = [1]
    val = 1
    assert func(val, tab)


def test_recherche4():
    tab = [1, 3]
    val = 3
    assert func(val, tab)


def test_recherche5():
    tab = [-1, 0, 5]
    val = 0
    assert func(val, tab)


def test_recherche6():
    tab = [0, 1, 1, 2, 3, 3, 5, 8, 13, 21]
    val = 0
    assert func(val, tab)


def test_recherche7():
    tab = [0, 1, 1, 2, 3, 3, 5, 8, 13, 21]
    val = 21
    assert func(val, tab)


def test_recherche8():
    tab = [0, 1, 1, 2, 3, 3, 5, 8, 13, 21]
    val = 13
    assert func(val, tab)


def test_recherche9():
    tab = [0, 1, 1, 2, 3, 3, 5, 8, 13, 21]
    val = -5
    assert not func(val, tab)
