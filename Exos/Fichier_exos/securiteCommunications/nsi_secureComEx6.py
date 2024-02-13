import hashlib
import time
import random as rd


# variable globale
alphabet = [chr(k) for k in range(33, 126)]  # alphabet étendu
# alphabet = list(map(chr, range(33, 126) ) )  # alphabet étendu
rd.shuffle(alphabet)  # mélange en place de l'alphabet


def hache_sha1(chaine : str):
    """Renvoie le haché d'une chaîne de caractères selon la méthode
        de hachage sha1.
    """
    octets = chaine.encode()  # en objet de type byte
    hache = hashlib.sha1(octets)  # objet haché
    return hache.hexdigest()  # renvoi en hexadécimal


def cree_sel(taille : int) -> str:
    """Renvoie un sel aléatoire de longueur taille.
        Les caractères sont choisis dans l'alphabet ascii.
    """
    sel = [rd.choice(alphabet) for _ in range(taille)]  # taille choix au hasard
    # sel = list(map(lambda x : rd.choice(alphabet), range(taille) ) )
    return "".join(sel)  # renvoi comme chaîne de caractères
    

def hache_mdpSel(sel, mdp):
    """Renvoie le sel et le haché avec sel d'un mot de passe selon la
        méthode de hachage sha1.
    """
    octets = (sel + mdp).encode()  # en objet de type byte
    hache = hashlib.sha1(octets)  # objet haché
    return sel, hache.hexdigest()  # renvoi en hexadécimal


def test_hache(n : int) -> float:
    """Renvoie la durée en seconde nécessaire pour hacher n fois de suite
        le même mot de passe.
    """
    debut = time.time()
    for _ in range(n):
        hache_sha1("C'est mon mot de passe")
    fin = time.time()
    return fin - debut