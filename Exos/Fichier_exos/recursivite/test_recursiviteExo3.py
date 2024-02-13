from nsi_recursiviteExo3Corrige import\
     u as func

def test_calculeU_1():
    assert func(0) == 0

def test_calculeU_2():
    assert func(1) == 1

def test_calculeU_3():
    assert func(2) == 1

def test_calculeU_4():
    assert func(3) == 2

def test_calculeU_5():
    assert func(4) == 3

def test_calculeU_6():
    assert func(5) == 5

def test_calculeU_7():
    assert func(6) == 8
