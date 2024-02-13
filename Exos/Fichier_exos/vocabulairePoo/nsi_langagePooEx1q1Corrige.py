# fonction utilitaire
def n_str_digits(n : int, nbDigits : int = 2) -> str:
    """Renvoie une chaîne de caractères de longueur
        nbDigits représentant l'entier naturel n.
        Pré-condition : le nombre de chiffres de n
            est inférieur ou égal à nbDigits.
    """
    # pré-conditions
    assert isinstance(n, int) and n >= 0
    assert isinstance(nbDigits, int) and len(str(n)) <= nbDigits
    # traitement
    return '0'*(nbDigits - len(str(n))) + str(n)


# la classe Chrono
class Chrono:
    """Une classe pour représenter et manipuler des temps mesurés en
        heures, minutes et secondes entières.
    """
    heureMax : int = 24
    
    def __init__(self, h : int, m : int, s : int):
        # invariant 0 <= h < heureMax et 0 <= m < 60 et 0 <= s < 60
        self._heures = h % Chrono.heureMax
        self._minutes = m % 60
        self._secondes = s % 60
    
    def get_heures(self) -> int:
        """renvoie les heures du chronomètre."""
        return self._heures
    
    def get_minutes(self) -> int:
        """renvoie les minutes du chronomètre."""
        return self._minutes
    
    def get_secondes(self) -> int:
        """renvoie les secondes du chronomètre."""
        return self._secondes
    
    def set_heures(self, h : int) -> None:
        """ajoute h heures au chronomètre modulo 24 heureMax."""
        self._heures = (self._heures + h) % Chrono.heureMax
        return None
    
    def set_minutes(self, m : int) -> None:
        """ajoute m minutes au chronomètre en ajustant les heures."""
        tmp_minutes = self._minutes + m
        self._minutes = tmp_minutes % 60
        self.set_heures(tmp_minutes // 60)
        return None
    
    def set_secondes(self, s : int) -> None:
        """ajoute s secondes au chronomètre en ajustant minutes et heures."""
        tmp_secondes = self._secondes + s
        self._secondes = tmp_secondes % 60
        self.set_minutes(tmp_secondes // 60)
        return None
    
    def ajoute(self, other):
        """Ajoute un chronomètre au chronomètre et renvoie un
            nouveau chronomètre."""
        tmp_s = self._secondes + other.get_secondes()
        tmp_m = self._minutes + other.get_minutes() + tmp_s // 60
        tmp_h = self._heures + other.get_heures() + tmp_m // 60
        return Chrono(tmp_h, tmp_m, tmp_s)
    
    def __add__(self, other):
        """Ajoute deux chronomètres par l'opérateur + et renvoie un
            nouveau chronomètre."""
        return self.ajoute(other)
    
    def __iadd__(self, other):
        """Ajoute en place un chronomètre par l'opérateur +=."""
        self.set_secondes(other.get_secondes())
        self.set_minutes(other.get_minutes())
        self.set_heures(other.get_heures())
        return self
    
    def __str__(self) -> str:
        s = str(self._secondes)
        m = str(self._minutes)
        h = str(self._heures)
        return h + 'h ' + m + 'm ' + s + 's'
    
    def __repr__(self) -> str:
        s = n_str_digits(self._secondes)
        m = n_str_digits(self._minutes)
        h = n_str_digits(self._heures)
        return h + ':' + m + ':' + s
    
    def __hash__(self):
        pass
    
    def __eq__(self, other) -> bool:
        """renvoie True si les deux chronomètres affichent les mêmes
            temps.
            Appel par self == other.
        """
        eq1 = self._secondes == other._secondes
        eq2 = self._minutes == other._minutes
        eq3 = self._heures == other._heures
        return eq1 and eq2 and eq3
    
    def __ne__(self, other) -> bool:
        """renvoie True si les deux chronomètres n'affichent pas les
            mêmes temps.
            Appel par self != other.
        """
        return not(self == other)
    
    def __lt__(self, other) -> bool:
        """Renvoie True si le premier chronomètre affiche un temps
            strictement inférieur au second.
            Appel par self < other.
        """
        ineq1 = self._heures < other._heures
        ineq2 = self._minutes < other._minutes
        ineq3 = self._secondes < other._secondes
        eq1 = self._heures == other._heures
        eq2 = self._minutes == other._minutes
        return ineq1 or (eq1 and ineq2) or (eq1 and eq2 and ineq3)
    
    def __le__(self, other) -> bool:
        """Renvoie True si le premier chronomètre affiche un temps
            inférieur ou égal au second.
            Appel par self <= other.
        """
        return (self < other) or (self == other)
    
    def __gt__(self, other) -> bool:
        """Renvoie True si le premier chronomètre affiche un temps
            strictement supérieur au second.
            Appel par self > other.
        """
        return other < self
    
    def __ge__(self, other) -> bool:
        """Renvoie True si le premier chronomètre affiche un temps
            supérieur ou égal au second.
            Appel par self >= other.
        """
        return other <= self
    