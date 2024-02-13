# importation de la structure de Pile
from nsi_pile_1_corrige import *

# associations parenthèses fermante-ouvrante par un dictionnaire
parentheses = {')' : '(', ']' : '[', '}' : '{'}

# fonction d'analyse
def analyse_expression(expression : str) -> bool:
    """Analyse le bon parenthèsage d'expression et renvoie True si
        l'expression est correctement parenthée ou False sinon.
    """
    # pour empiler les parenthèses ouvrantes
    pile = creer_pile()
    # parcours de l'expression
    for c in expression: # parcours par valeurs
        if c in parentheses.values():  # parenthèse ouvrante ?
            empiler(c, pile)
        elif c in parentheses.keys():  # parenthèse fermante ?
            if est_pile_vide(pile) or parentheses[c] != sommet(pile):
                return False
            else:
                depiler(pile)  # parenthèse correctement fermée
    # fin du parcours
    return est_pile_vide(pile)  # True or False conforme à l'attendu
