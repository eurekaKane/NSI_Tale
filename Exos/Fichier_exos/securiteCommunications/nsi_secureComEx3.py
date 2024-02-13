def calculPuissanceModulaire(a : int, x : int, p : int) -> int:
    """Renvoie l'entier a^x mod p."""
    # pré-conditions
    assert isinstance(a, int) and isinstance(p, int)\
           and a >= 1 and a < p
    # traitement
    return pow(a, x, p)

# programme principal
def main():
    # saisie sans précaution des paramètres
    p = int(input("Choix d'un nombre premier : "))
    a = int(input("Choix d'un nombre entier compris entre 1 et le nombre premier : "))
    x1 = int(input("Choix secret d'Alice : "))
    x2 = int(input("Choix secret de Bob : "))
    # calculs et échanges
    y1 = calculPuissanceModulaire(a, x1, p)  # calcul Alice
    y2 = calculPuissanceModulaire(a, x2, p)  # calcul Bob
    # vérification clef secrète
    assert calculPuissanceModulaire(y1, x2, p) == calculPuissanceModulaire(y2, x1, p)
    # clef secrète
    k = calculPuissanceModulaire(y2, x1, p)
    return k

if __name__ == "__main__":
    print("valeur de la clef secrète :", main())
