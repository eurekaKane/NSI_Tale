"""Une modélisation du lièvre et la tortue."""


# modules requis
import turtle as tl
import random as rd


# constantes du module
largeur = 600
hauteur = 400
fond = "#80FF30"
xmin, xmax = -300 + 50, 300 - 50
ymin, ymax = -200 + 50, 200 - 50


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
        return self.l
    
    
    def get_pos(self) -> tuple:
        """Renvoie la position du lièvre."""
        return self.get_ind().pos()
        
    
    def aller_vers(self, pos : tuple):
        """Déplace le lièvre vers la position pos."""
        x, y = pos  # dépaquetage du tuple
        # orientation du lièvre
        visee = self.get_ind().towards(x, y)
        orientation = self.get_ind().heading()
        angle = visee - orientation
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
        # distance à parcourir par le lièvre
        ecart = self.get_ind().distance(x, y)
        if ecart > 20:
            self.get_ind().forward(20)
        else:
            self.get_ind().forward(ecart)
        return None
        
        
class Tortue:
    """Une classe pour les tortues."""
    
    def __init__(self):
        tl.hideturtle()
        self.t = tl.Turtle(shape = "tortue.gif")  # une instance de Turtle
        self.t.pencolor("#8000FF")
    
    
    def get_ind(self) -> tl.Turtle:
        """Renvoie un individu tortue sur lequel il est
            possible d'agir avec les méthodes turtle.
        """
        return self.t
    
    
    def get_pos(self) -> tuple:
        """Renvoie la position de la tortue."""
        return self.get_ind().pos()
    
    
    def teleporter(self):
        """Téléporte l'instance à sa position initiale."""
        self.get_ind().penup()
        self.get_ind().goto(rd.randint(xmin, xmax), rd.randint(ymin, ymax))
        self.get_ind().pendown()
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
        """déplacement aléatoire de la tortue"""
        angle = rd.randint(-30, 30)
        # orientation
        if angle > 0:
            self.get_ind().left(angle)
        else:
            self.get_ind().right(-1*angle)
        # tests au bord
        self.corriger()
        # distance
        dist = rd.randint(5, 20)
        self.get_ind().forward(dist)
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
    l1 = lievre()  # instance d'un lièvre
    t1 = tortue()  # instance d'une tortue
    while True:
        t1.deplacer()  # la tortue se déplace
        l1.aller_vers(t1.get_pos())  # le lièvre la poursuit
        if l1.get_ind().distance(t1.get_pos()) < 5:
            break
    # boucle de gestion d'évènements
    ecran.mainloop()