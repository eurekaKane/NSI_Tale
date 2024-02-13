from nsi_triRapide import _separe as func


def test_separe1():
    tab = []
    val = 5.1
    assert func(tab, val) == ([], [])


def test_separe2():
    tab = [5]
    val = 3
    assert func(tab, val) == ([], [5])


def test_separe3():
    tab = [5]
    val = 7
    assert func(tab, val) == ([5], [])


def test_separe4():
    tab = [-2, 6, -1.2, 3.4]
    val = 3.4
    assert func(tab, val) == ([-2, -1.2, 3.4], [6])


def test_separe5():
    tab = [-1, 8, 7.2, -3.2, 7.2, 12.57, 1]
    val = 7.2
    assert func(tab, val) == ([-1, 7.2, -3.2, 7.2, 1], [8, 12.57])

