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
        """Ajoute le chrono other au chrono self et renvoie
            un nouveau chrono.
        """
        tmp_secondes = self.get_secondes() +\
                       other.get_secondes()
        tmp_minutes = self.get_minutes() +\
                      other.get_minutes() +\
                      tmp_secondes // 60
        tmp_heures = self.get_heures() +\
                     other.get_heures() +\
                     tmp_minutes // 60
        return Chrono(tmp_heures, tmp_minutes, tmp_secondes)
    
    
    def __add__(self, other):
        return self.ajoute(other)
    
    
    def __iadd__(self, other):
        self.set_secondes(other.get_secondes())
        self.set_minutes(other.get_minutes())
        self.set_heures(other.get_heures())
        return self
    
    
    def affiche(self) -> str:
        """Affiche le chrono sous la forme hms."""
        s = str(self.get_secondes())
        m = str(self.get_minutes())
        h = str(self.get_heures())
        return h + 'h ' + m + 'm ' + s + 's'
    
    
    def __repr__(self) -> str:
        """Affiche le chrono sous la forme ..:..:.."""
        s = str(self.get_secondes())
        m = str(self.get_minutes())
        h = str(self.get_heures())
        return h + ':' + m + ':' + s