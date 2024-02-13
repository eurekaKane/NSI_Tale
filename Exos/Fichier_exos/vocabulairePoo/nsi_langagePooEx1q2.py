class Chrono:
    """Une classe pour représenter et manipuler des temps mesurés en
        heures, minutes et secondes entières.
    """
    heureMax : int = 24
    _modulo = heureMax * 3600
    
    def __init__(self, h : int, m : int, s : int):
        # invariant 0 <= self._temps < heureMax * 3600
        pass
        
    # à compléter