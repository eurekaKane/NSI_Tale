"""Ce module offre des fonctions qui permettent de vérifier
    et d'illustrer le paradoxe des anniversaires dans la
    version suivante.
    Dans une assemblée de 23 personnes, il y a une chance
    sur deux qu'au moins deux d'entre elles soient nées le
    même jour calendaire.
"""


import random as rd
import nsi_dates as dates
from matplotlib import pyplot as plt


def _verifieEntierPositif(n) -> None:
    """Cette fonction lève une exception ValueError si les
        pré-conditions portant sur l'argument entier n ne
        sont pas vérifiées.
    """
    if not(isinstance(n, int) and n > 0):
        raise ValueError("L'argument " + str(n) + " est invalide")
    return None


def _verifieListeNonVide(l) -> None:
    """Cette fonction lève une exception ValueError si les
        pré-conditions portant sur l'argument liste l ne
        sont pas vérifiées.
    """
    if not(isinstance(l, list) and len(l) != 0):
        raise ValueError("L'argument est invalide")
    return None

def _genereDates() -> list:
    """Cette fonction renvoie un objet de type list dont les
        23 valeurs sont des entiers aléatoires compris entre
        1 et 366.
        La valeur renvoyée modélise une série de 23 dates
        calendaires d'anniversaire.
    """
    return [rd.randint(1, 366) for _ in range(23)]


def _contientDoublon(tab : list) -> bool:
    """Cette fonction renvoie la valeur True si le tableau
        tab contient au moins un doublon.
        Elle renvoie False sinon.
    """
    # création d'un ensemble de dates vide
    dejaVus = dates.creerEnsemble()
    for elt in tab:  # pour chaque date du tableau
        # elt a-t-il été déjà vu ?
        if dates.estPresent(elt, dejaVus):
            return True  # c'est un doublon
        # sinon il est ajouté dans l'ensemble
        dates.ajouteElement(elt, dejaVus)
    return False  # il n'y a pas eu d'interruption


def frequenceSucces(n : int) -> float:
    """Cette fonction renvoie la fréquence de succès de
        présence d'un doublon lors de n répétitions du choix
        de 23 dates au hasard.
        Pré-condition : n est un entier naturel non nul.
    """
    # pré-condition
    _verifieEntierPositif(n)
    # traitement
    acc = 0
    for _ in range(n):
        if _contientDoublon(_genereDates()):
            acc += 1  # un succès de plus
    return acc / n


def repeteFrequence(nbSeries : int, nbRepet : int) -> list:
    """Cette fonction renvoie la liste des fréquences
        observées sur nbSeries de nbRepet répétitions de
        l'expérience.
        Pré-conditions : nbSeries et nbRepet sont deux
        entiers naturels non nuls.
    """
    # pré-conditions
    _verifieEntierPositif(nbSeries)
    _verifieEntierPositif(nbRepet)
    # traitement
    return [frequenceSucces(nbRepet) for _ in range(nbSeries)]


def frequenceCumuleeSucces(n : int) -> list:
    """Cette fonction cumule le nombre de succès sur n
        répétitions de l'expérience aléatoire du paradoxe
        des anniversaires et renvoie les n valeurs de la
        fréquence cumulée des succès.
        Pré-condition : n est un entier naturel non nul.
    """
    # pré-condition
    _verifieEntierPositif(n)
    # traitement
    acc = 0  # accumulateur de succès
    freq = [0.]*n  # initialisation des fréquences cumulées
    for i in range(1, n + 1):
        if _contientDoublon(_genereDates()):
            acc += 1
        freq[i - 1] = acc / i
    return freq


def produitNuagePoints(listeFrequences : list) -> None:
    """Cette fonction produit un nuage de points à partir
        d'un tableau de nombres flottants compris entre 0 et
        1.
        Pré-condition :
            listeFrequences est non vide.
        Post-condition :
            l'instruction plt.show() affiche le nuage.
    """
    # pré-condition
    _verifieListeNonVide(listeFrequences)
    # traitement
    n = len(listeFrequences)  # nombre de points
    x = list(range(1, n + 1))  # abscisses des points
    plt.plot(x, listeFrequences, 'b.')  # des points bleus
    plt.grid()  # une grille pour la lecture
    # un segment rouge d'équation y = 0.5
    plt.plot([0, n], [0.5, 0.5], 'r')
    return None


# programme principal
if __name__ == "__main__":
    produitNuagePoints(frequenceCumuleeSucces(500))
    plt.show()
