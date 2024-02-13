import random as rd

from nsi_triRapide import triRapide as tri


# fonction utilitaire
def est_trie(tab : list) -> bool:
    """Cette fonction renvoie la valeur True si les valeurs des éléments
        du tableau tab sont rangées en ordre croissant et False sinon.
    """
    n = len(tab)
    for i in range(1, n):
        if tab[i] < tab[i-1]:
            return False
    return True


# fonctions de tests
def test_tab1():
    tab = []
    assert est_trie(tri(tab))


def test_tab2():
    tab = [5]
    assert est_trie(tri(tab))
    

def test_tab3():
    tab = [1, 3]
    assert est_trie(tri(tab))
    

def test_tab4():
    tab = [3, 1]
    assert est_trie(tri(tab))
    

def test_tab5():
    tab = [1, 3, 5]
    assert est_trie(tri(tab))
    

def test_tab6():
    tab = [5, 3, 1]
    assert est_trie(tri(tab))
    

def test_tab7():
    tab = [rd.randint(-10, 10) for _ in range(8)]
    assert est_trie(tri(tab))
    

def test_tab8():
    tab = [rd.random() for _ in range(8)]
    assert est_trie(tri(tab))
    

def test_tab9():
    tab = [-1*rd.random() for _ in range(8)]
    assert est_trie(tri(tab))
    
