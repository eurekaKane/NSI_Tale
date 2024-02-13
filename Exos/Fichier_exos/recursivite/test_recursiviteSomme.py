from nsi_recursiviteSomme import somme as func

def test_somme0():
    n = 0
    assert func(n) == 0

def test_somme1():
    n = 1
    assert func(n) == 1

def test_somme2():
    n = 2
    assert func(n) == 3

def test_somme3():
    n = 3
    assert func(n) == 6

def test_somme4():
    n = 4
    assert func(n) == 10

def test_somme5():
    n = 5
    assert func(n) == 15

def test_somme100():
    n = 100
    assert func(n) == 5050
