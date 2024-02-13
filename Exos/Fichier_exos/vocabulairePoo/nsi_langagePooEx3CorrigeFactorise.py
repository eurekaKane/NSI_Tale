"""Une autre modélisation du lièvre et la tortue."""


# modules requis
import turtle as tl
import random as rd


# constantes du module
largeur = 600  # pour l'écran
hauteur = 400
fond = "#80FF30"
xmin, xmax = -300 + 50, 300 - 50
ymin, ymax = -200 + 50, 200 - 50


# une classe pour tous
class Animal:
    """Une classe pour les lièvres et les tortues."""
    
    def __init__(self):
        tl.hideturtle()
        # une instance de Turtle
        self.a = tl.Turtle()
    
    
    def get_ind(self) -> tl.Turtle:
        """Renvoie un individu animal sur lequel il est
            possible d'agir avec les méthodes turtle.
        """
        return self.a
    
    
    def get_pos(self) -> tuple:
        """Renvoie la position de l'animal."""
        return self.get_ind().pos()
    
    
    def teleporter(self):
        """Téléporte l'instance à sa position initiale."""
        self.get_ind().penup()
        self.get_ind().goto(rd.randint(xmin, xmax), rd.randint(ymin, ymax))
        self.get_ind().pendown()
        return None
    
    
    def distance(self, other) -> float:
        """Renvoie la distance entre l'instance et une autre
            instance.
        """
        return self.get_ind().distance(other.get_pos())
    
    
    def aller_vers(self, other):
        """Déplace l'animal vers la position d'une autre instance."""
        # orientation de l'animal
        visee = self.get_ind().towards(other.get_pos())
        orientation = self.get_ind().heading()
        angle = visee - orientation
        # contraintes du lièvre
        # cas angle obtus
        if angle < -180:
            angle = 360 + angle  # 0 <= angle < 180
        elif angle > 180:
            angle = angle - 360  # -180 <= angle < 0
        # traitements angle aigu
        if angle < -20:
            self.get_ind().right(20)
        elif angle > 20:
            self.get_ind().left(20)
        elif angle < 0:
            self.get_ind().right(-1 * angle)
        else:
            self.get_ind().left(angle)
        # distance à parcourir par l'animal
        ecart = self.distance(other)
        if ecart > 20:
            self.get_ind().forward(20)
        else:
            self.get_ind().forward(ecart)
        return None
        
    
    def corriger(self):
        """Corrige la direction si l'instance est trop près
            du bord de l'écran.
        """
        # position et direction de l'instance
        x, y = self.get_pos()
        direction = self.get_ind().heading()
        # correction de la direction comme un rebond
        if x <= xmin:
            if 90 <= direction <= 180:
                self.get_ind().right(90)
            elif 180 < direction <= 270:
                self.get_ind().left(90)
        elif x >= xmax:
            if 0 <= direction <= 90:
                self.get_ind().left(90)
            elif 270 <= direction <= 360:
                self.get_ind().right(90)
        if y <= ymin:
            if 180 <= direction <= 270:
                self.get_ind().right(90)
            elif 270 < direction <= 360:
                self.get_ind().left(90)
        elif y >= ymax:
            if 0 <= direction <= 90:
                self.get_ind().right(90)
            elif 90 < direction <= 180:
                self.get_ind().left(90)
        return None
    
        
    def deplacer(self):
        """déplacement aléatoire de l'animal"""
        # contraintes de la tortue
        angle = rd.randint(-30, 30)
        # orientation
        if angle > 0:
            self.get_ind().left(angle)
        else:
            self.get_ind().right(-1*angle)
        # tests au bord
        self.corriger()
        # déplacement
        dist = rd.randint(5, 20)
        self.get_ind().forward(dist)
        return None
    
        
# fonctions de l'interface
def lievre() -> Animal:
    """Creer un lièvre au centre et renvoie son instance."""
    a = Animal()
    a.get_ind().shape("lievre.gif")
    a.get_ind().pencolor("#FF0080")
    return a


def tortue() -> Animal:
    """Creer une tortue, la place à une position aléatoire
        sur l'écran et renvoie son instance.
    """
    tor = Animal()
    tor.get_ind().shape("tortue.gif")
    tor.get_ind().pencolor("#8000FF")
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
    l = lievre()  # instance pour un lièvre
    t = tortue()  # instance pour une tortue
    while True:
        t.deplacer()  # la tortue se déplace
        l.aller_vers(t)  # le lièvre la poursuit
        if l.distance(t) < 5:
            break
    # boucle de gestion d'évènements
    ecran.mainloop()