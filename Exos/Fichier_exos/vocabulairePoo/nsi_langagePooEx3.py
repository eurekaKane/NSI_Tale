"""Une modélisation du lièvre et la tortue."""


# modules requis
import turtle as tl
import random as rd


# constantes du module
largeur = 600
hauteur = 400
fond = "#80FF30"
xmin, xmax = -300 + 50, 300 - 50
ymin, ymax = -200 + 47, 200 - 47


# les classes
class Lievre:
    """Une classe pour les lièvres."""
    
    def __init__(self):
        tl.hideturtle()
        # une instance de Turtle
        self.l = tl.Turtle(shape = "lievre.gif")
        self.l.pencolor("#FF0080")
    
    
    def get_ind(self) -> tl.Turtle:
        """Renvoie un individu lièvre sur lequel il est
            possible d'agir avec les méthodes turtle.
        """
        pass
    
    
    def get_pos(self) -> tuple:
        """Renvoie la position du lièvre."""
        pass
        
    
    def aller_vers(self, pos : tuple):
        """Déplace le lièvre vers la position pos."""
        pass
        return None
        
        
class Tortue:
    """Une classe pour les tortues."""
    
    def __init__(self):
        tl.hideturtle()
        self.t = tl.Turtle(shape = "tortue.gif")  # une instance de Turtle
        self.t.pencolor("#8000FF")
    
    
    def get_ind(self) -> tl.Turtle:
        """Renvoie un individu lièvre sur lequel il est
            possible d'agir avec les méthodes turtle.
        """
        pass
    
    
    def get_pos(self) -> tuple:
        """Renvoie la position de la tortue."""
        pass
    
    
    def teleporter(self):
        """Téléporte l'instance à sa position initiale mais
            aléatoire.
        """
        pass
        return None
    
    
    def deplacer(self):
        """Déplace aléatoirement la tortue sur l'écran."""
        pass
        return None
    
        
# fonctions de l'interface
def lievre() -> Lievre:
    """Creer un lièvre au centre et renvoie son instance."""
    return Lievre()


def tortue() -> Tortue:
    """Creer une tortue, la place à une position aléatoire
        sur l'écran et renvoie son instance.
    """
    tor = Tortue()
    tor.teleporter()
    return tor


# programme principal
if __name__ == "__main__":
    # création d'une instance d'écran
    ecran = tl.Screen()
    # ajustement de ses attributs avec des setters
    ecran.delay(150)  # délai entre 2 dessins en ms
    ecran.addshape("lievre.gif")  # ajout des images
    ecran.addshape("tortue.gif")
    ecran.screensize(largeur, hauteur, fond)  # taille et fond
    ecran.title("Le lièvre et la tortue")  # titre
    # début de l'animation
    t = tortue()
    l = lievre()
    while t.distance(x, y)>= 20:
        t.deplacer(x+randint(-5,5),y+randint(-5,5))
        l.aller-vers()
    
    # boucle de gestion d'évènements
    ecran.mainloop()