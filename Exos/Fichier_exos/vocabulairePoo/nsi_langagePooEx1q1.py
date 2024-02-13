import time 
import sys

class Chrono:
    """Une classe pour représenter et manipuler des temps mesurés en
        hours, minutes et seconds entières.
    """
    hourMax : int = 24
    
    def __init__(self, h : int, m : int, s : int):
        # invariant 0 <= h < hourMax et 0 <= m < 60 et 0 <= s < 60
        self._hours = h % Chrono.hourMax
        self._minutes = m % 60
        self._seconds = s % 60
        self._status = True
        self._key = 'space'
    
    def get_hours(self) -> int:
        """renvoie les hours du chronomètre."""
        return self._hours
    
    def get_minutes(self) -> int:
        """renvoie les minutes du chronomètre."""
        return self._minutes
    
    def get_seconds(self) -> int:
        """renvoie les seconds du chronomètre."""
        return self._seconds
    
    def set_hours(self, h : int) -> None:
        """ajoute h hours au chronomètre modulo 24 hourMax."""
        self._hours = (self._hours + h) % Chrono.hourMax
        return None
    
    def set_minutes(self, m : int) -> None:
        """ajoute m minutes au chronomètre en ajustant les hours."""
        tmp_minutes = self._minutes + m
        self._minutes = tmp_minutes % 60
        self.set_hours(tmp_minutes // 60)
        return None
    
    def set_seconds(self, s : int) -> None:
        """ajoute s seconds au chronomètre en ajustant minutes et hours."""
        tmp_seconds = self._seconds + s
        self._seconds = tmp_seconds % 60
        self.set_minutes(tmp_seconds // 60)
        return None
    
    def dispChrono(self):
        h = self.get_hours()
        m = self.get_minutes()
        s = self.get_seconds()
        
        return (f"{h : 2}h {m : 2}m {s : 2}s")
        
    
    def resetChrono(self):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0
        
    def stopChrono(self):
        self.status = False
    
    def startChrono(self):
        self._status = True
        while self._status:
            if keyboard.is_pressed(self._key):
                self.stopChrono()
            time.sleep(1)
            self.set_seconds(1)
            print(self.dispChrono(), end="\r")
            
class Clock:
    
    def __init__(self):
        
            

class Display:
    









def __init__(self, h, m, s):
        self._chrono = Chrono(h, m, s)
        #self._clock = Clock()
        #self._timer = timer(h, m, s)
        
    def dispChrono(self):
        h = self._chrono.get_hours
        m = self._chrono.get_minutes()
        s = self._chrono.get_seconds()
        
        print(f"{h}H {m}M {s}S", end="\r")
    
    def dispTimer(self):
        pass
    
    def dispClock(self):
        pass


