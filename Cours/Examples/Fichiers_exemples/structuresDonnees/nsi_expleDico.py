"""Un exemple d'implémentation d'une structure de Dictionnaire."""

# Avec une fonction de hachage des clefs et adaptation aux collisions

# constante et fonctions utilitaires
hashMax = 7  # taille de la table

def hachage_str(chaine : str) -> int:
    """Renvoie le haché de la chaîne de caractères."""
    result = 0  # initialisation à 0
    for c in chaine:  # parcours par caractère
        result = result + ord(c)  # ajout du code du caractère
    return result % hashMax  # reste pour entrer dans la table

def extraire_cles(liste : list) -> set:
    """Renvoie l'ensemble des clés ayant le même haché."""
    return {elt[0] for elt in liste}  # en compréhension


# la structure

def creer_dico():
    """Renvoie un dictionnaire vide"""
    return [None]*hashMax

def est_cle(clef : str, dico : list) -> bool:
    """Renvoie True si la valeur de clef est une clé du dictionnaire dico.
        Renvoie False sinon.
    """
    h = hachage_str(clef)  # la valeur de la clé est hachée
    return dico[h] is not None and clef in extraire_cles(dico[h])

def taille_dico(dico : list) -> int:
    """Renvoie le nombre d'associations du dictionnaire."""
    cpt = 0
    for liste in dico:  # pour chaque listes d'associations
        if liste is not None:  # s'il y en a une
            cpt = cpt + len(liste)  # ajout du nombre d'associations avec clé de même haché
    return cpt

def ajouter_asso(clef : str, val, dico : list) -> None:
    """Ajoute l'association (clef, val) au dictionnaire dico si elle n'y
        est pas encore.
        Le cas échéant, le dictionnaire est modifié en place.
    """
    h = hachage_str(clef)  # la valeur de la clé est hachée
    if dico[h] is None:
        dico[h] = []  # sa valeur est initialisée par une liste vide
    elif clef in extraire_cles(dico[h]):
        return None  # la clé est déjà présente
    dico[h].append((clef, val))  # ajout de l'association
    return None

def valeur_cle(clef : str, dico : list):
    """Renvoie la valeur associée à la clé si celle-ci est bien une
        clé du dictionnaire.
        Provoque une erreur d'assertion sinon.
    """
    # pré-condition
    assert est_cle(clef, dico), "La clef n'est pas dans le dictionnaire."
    # traitement
    h = hachage_str(clef)  # la valeur de la clé est hachée
    for c, v in dico[h]:  # dépaquetage de chaque tuple du tableau
        if c == clef:
            return v
    return None

def cles_dico(dico : list) -> list:
    """Renvoie un énumérateur des clés du dictionnaire."""
    result = []  # une liste vide
    for liste in dico:  # pour chaque liste éventuelle
        if liste is not None:  # si elle n'est pas vide
            for c, _ in liste:  # dépaquetage de chaque tuple
                result.append(c)  # ajout de la clé
    return result

def valeurs_dico(dico : list) -> list:
    """Renvoie un énumérateur des valeurs du dictionnaire."""
    result = []  # une liste vide
    for liste in dico:  # pour chaque liste éventuelle
        if liste is not None:  # si elle n'est pas vide
            for _, v in liste:  # dépaquetage de chaque tuple
                result.append(v)  # ajout de la valeur
    return result

def changer_valeur(clef : str, val, dico : list) -> None:
    """Change la valeur associée à la clé clef par val dans le
        dictionnaire dico si cette clé est présente.
        Provoque une erreur d'assertion sinon.
    """
    # pré-condition
    assert est_cle(clef, dico), "La clef n'est pas dans le dictionnaire."
    # traitement
    h = hachage_str(clef)  # la valeur de la clé est hachée
    newListe = []  # nouvelle liste de tuples
    for c, v in dico[h]:  # dépaquetage des tuples
        if c == clef:  # si c'est la bonne clé
            newListe.append((clef, val))  # ajout avec nouvelle valeur
        else:
            newListe.append((c, v))  # on replace l'association
    dico[h] = newListe
    return None
            
def retirer_cle(clef : str, dico : list) -> None:
    """Retire la clé clef du dictionnaire dico si elle est présente.
        Provoque une erreur d'assertion sinon.
    """
    # pré-condition
    assert est_cle(clef, dico), "La clef n'est pas dans le dictionnaire."
    # traitement
    h = hachage_str(clef)  # la valeur de la clé est hachée
    newListe = []  # nouvelle liste de tuples
    for c, v in dico[h]:  # dépaquetage des tuples
        if c != clef:  # si ce n'est pas la bonne clé
            newListe.append((c, v))  # on la replace
    dico[h] = newListe
    return None