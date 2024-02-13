class Fraction:
    """Une classe pour opérer sur des nombres rationnels.
        Le dénominateur est un nombre entier strictement positif.
    """
    
    def __init__(self, num : int, den : int):
        # exception levée si den <= 0
        if not( isinstance(num, int) and isinstance(den, int) ):
            raise TypeError("Les valeurs du numérateur et du dénominateurs sont des nombres entiers.")
        elif den <= 0:
            raise ValueError("La valeur du dénominateur doit être strictement positive.")
        # cas normal
        p = Fraction.pgcd(num, den)
        self._numerateur = num // p
        self._denominateur = den // p
    
    def delta(self, other) -> int:
        p1 = self._numerateur * other.get_den()
        p2 = self._denominateur * other.get_num()
        return p1 - p2
    
    def get_num(self) -> int:
        """Renvoie le numérateur d'une instance de la classe."""
        return self._numerateur
    
    def get_den(self) -> int:
        """Renvoie le numérateur d'une instance de la classe."""
        return self._denominateur
    
    def affiche(self) -> str:
        """Pour afficher une fraction."""
        return str(self._numerateur) + '/' + str(self._denominateur)
        
    def __str__(self) -> str:
        """Pour afficher via print."""
        return self.affiche()
    
    def __repr__(self) -> str:
        """Pour afficher dans la console."""
        return self.affiche()
    
    def est_nul(self):
        """renvoie True si la fraction est égale à 0."""
        return self._numerateur == 0
    
    def ajoute(self, other):
        """Renvoie la fraction somme comme nouvel objet."""
        # calcul du numérateur et du dénominateur
        num = self._numerateur * other.get_den() +\
              self._denominateur * other.get_num()
        den = self._denominateur * other.get_den()
        # renvoi de la nouvelle fraction
        return Fraction(num, den)
    
    def divise(self, other):
        """Renvoie la fraction quotient comme nouvel objet."""
        if other.est_nul():
            raise ZeroDivisionError("On ne peut pas diviser par zéro.")
        else:
            # calcul du numérateur et du dénominateur
            num = self._numerateur * other.get_den()
            den = self._denominateur * other.get_num()
            # renvoi de la nouvelle fraction
            return Fraction(num, den)
    
    def soustrait(self, other):
        """Renvoie la fraction différence comme nouvel objet."""
        # calcul du numérateur et du dénominateur
        num = self._numerateur * other.get_den() -\
              self._denominateur * other.get_num()
        den = self._denominateur * other.get_den()
        # renvoi de la nouvelle fraction
        return Fraction(num, den)
    
    def multiplie(self, other):
        """Renvoie la fraction produit comme nouvel objet."""
        # calcul du numérateur et du dénominateur
        num = self._numerateur * other.get_num()
        den = self._denominateur * other.get_den()
        # renvoi de la nouvelle fraction
        return Fraction(num, den)
    
    def est_inferieur(self, other):
        """Renvoie True si la fraction est inférieure à l'autre."""
        return self.delta(other) < 0
    
    def est_egal(self, other):
        """Renvoie True si les deux fractions sont égales."""
        return self.delta(other) == 0
    
    def __add__(self, other):
        """Renvoie self + other"""
        return self.ajoute(other)
    
    def __sub__(self, other):
        """Renvoie self - other"""
        return self.soustrait(other)
    
    def __mul__(self, other):
        """Renvoie self * other"""
        return self.multiplie(other)
    
    def __truediv__(self, other):
        """Renvoie self / other"""
        return self.divise(other)
    
    def __hash__(self):
        pass
    
    def __eq__(self, other) -> bool:
        """Renvoie True si les deux fractions sont égales.
            Appel self == other.
        """
        return self.est_egal(other)
    
    def __ne__(self, other) -> bool:
        """Renvoie True si les deux fractions ne sont pas égales.
            Appel self != other.
        """
        return not(self.est_egal(other))
    
    def __lt__(self, other) -> bool:
        """Renvoie True si la fraction est inférieure à l'autre.
            Appel self < other.
        """
        return self.est_inferieur(other)
    
    def __le__(self, other) -> bool:
        """Renvoie True si la fraction est inférieure ou égale à l'autre.
            Appel self <= other.
        """
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other) -> bool:
        """Renvoie True si la fraction est supérieure à l'autre.
            Appel self > other.
        """
        return other.est_inferieur(self)
    
    def __ge__(self, other) -> bool:
        """Renvoie True si la fraction est supérieure ou égale à l'autre.
            Appel self >= other.
        """
        return other.__le__(self)
    
    @staticmethod
    def pgcd(n : int, m : int) -> int:
        """Renvoie le PGCD des deux nombres entiers naturels.
            Cette fonction est récursive.
            Algorithme d'Euclide.
        """
        if m == 0:
            return n
        else:
            return Fraction.pgcd(m, n % m)
        