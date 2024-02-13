def sommeEntiers(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est itérative.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # traitement
    
    

def sommeEntiers_rec(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est récursive.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # appel récursif
    

# pour suivre avec le débogueur
#sommeEntiers_rec(3)


def _somme_rec(n : int) -> int:
    """Cette fonction est le cœur récursif de la fonction somme.
        Elle est encapsulée.
    """
    

def somme(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est récursive.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # appel récursif principal
    return _somme_rec(n)

# pour suivre avec le débogueur
#somme(3)


def somme2(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est récursive.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # moteur récursif interne
    
    # appel récursif principal
    
# pour suivre avec le débogueur
#somme2(3)


def somme3(n : int) -> int:
    """Cette fonction renvoie la somme des n premiers nombres entiers naturels.
       Elle est récursive terminale.
       La valeur de n est de type int ainsi que la valeur renvoyée.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    # moteur récursif interne
    
    # appel récursif principal
    
# pour suivre avec le débogueur
#somme3(3)
