from nsi_expressionParenthesee import *

# fonctions de test
def test_1():
    expression = "2 + 5"
    assert analyse_expression(expression)

def test_2():
    expression = "(2 + 5)"
    assert analyse_expression(expression)
    
def test_3():
    expression = "2 + 5 * ("
    assert not analyse_expression(expression)

def test_4():
    expression = "2 + 5 )"
    assert not analyse_expression(expression)

def test_5():
    expression = "[2 + 5 ("
    assert not analyse_expression(expression)

def test_6():
    expression = "[2 + ( 5 * 2 ) ]"
    assert analyse_expression(expression)

def test_7():
    expression = "[2 + ( 5 * 2 ) "
    assert not analyse_expression(expression)

def test_8():
    expression = "{'a' : [(10, 20), (5,6)], 'b' : ([10, 20], 30)}"
    assert analyse_expression(expression)

def test_9():
    expression = "{'a' : [(10, 20), (5,6)], 'b' : [10, 20], 30)}"
    assert not analyse_expression(expression)
