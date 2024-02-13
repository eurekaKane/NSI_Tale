"""Tests pour la recherche de doublons."""

import pytest

from nsi_moduleDoublon import contientDoublon

def test_doublon1():
    tab = []
    assert not contientDoublon(tab)

def test_doublon2():
    tab = [1]
    assert not contientDoublon(tab)

def test_doublon3():
    tab = [1, 2]
    assert not contientDoublon(tab)

def test_doublon4():
    tab = [1, 58, 325, 45]
    assert not contientDoublon(tab)

def test_doublon5():
    tab = [1, 1]
    assert contientDoublon(tab)

def test_doublon6():
    tab = [1, 2, 3, 1]
    assert contientDoublon(tab)

def test_doublon7():
    tab = [2, 1, 9, 4, 1, 25]
    assert contientDoublon(tab)
