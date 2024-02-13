import nsi_moduleDoublon as doublon
from matplotlib import pyplot as plt

def moyenne(nbRepetitions : int) -> float:
    acc = 0
    for _ in range(nbRepetitions):
        tab = doublon.genereDates()
        if doublon.contientDoublon(tab):
            acc = acc + 1
    return acc / nbRepetitions

def serieMoyennes(nbSeries : int, nbRepet : int) -> list:
    return [moyenne(nbRepet) for _ in range(nbSeries)]

def nuagePoints(tab : list) -> None:
    plt.plot(tab, 'r+')
    return None