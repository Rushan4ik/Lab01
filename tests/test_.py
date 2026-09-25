import pytest

from toolkit import __main__


def test_calc1():
    res = __main__.calc("22+9")
    assert res == 31

def test_calc2():
    res = __main__.calc(" 170 - 4")
    assert res == 166

def test_calc3():
    res = __main__.calc("9*0")
    assert res == 0

def test_calc4():
    res = __main__.calc("2/5")
    assert res == 0.4

def test_calc5():
    res = __main__.calc("10*9 - 9")
    assert res == 81

def test_calc6():
    res = __main__.calc("9*9/9")
    assert res == 9

def test_calc7():
    res = __main__.calc("100--3")
    assert res == 103



@pytest.mark.xfail
def test_calc_empty_expression():
    res = __main__.calc("")
    assert res is None

@pytest.mark.xfail
def test_calc_unknown_character():
    res = __main__.calc("2+abc")
    assert res is None

@pytest.mark.xfail
def test_calc_missing_operand():
    res = __main__.calc("5+")
    assert res is None

@pytest.mark.xfail
def test_calc_two_operators():
    res = __main__.calc("3+*4")
    assert res is None

@pytest.mark.xfail
def test_calc_division_by_zero():
    res = __main__.calc("10/0")
    assert res is None







def test_converter_1():
    res = __main__.convert(45.8, 'c', 'f')
    assert abs(res - 114.44) < 10e-6

def test_converter_2():
    res = __main__.convert(59.0, 'f', 'c')
    assert abs(res - 15.0) < 10e-6

def test_converter_3():
    res = __main__.convert(0.0, 'k', 'c')
    assert abs(res + 273) < 10e-6

def test_converter_4():
    res = __main__.convert(250.0, 'g', 'kg')
    assert abs(res - 0.25) < 10e-6

def test_converter_5():
    res = __main__.convert(150.0, 'mm', 'cm')
    assert abs(res - 15.0) < 10e-6

def test_converter_6():
    res = __main__.convert(1.5, 'km', 'm')
    assert abs(res - 1500.0) < 10e-6

#Negative tests

@pytest.mark.xfail
def test_converter_unknown_from_unit():
    res = __main__.convert(10.0, 'qwerty', 'c')
    assert res is None

@pytest.mark.xfail
def test_converter_unknown_unit():
    res = __main__.convert(13.0, 'c', 'asd')
    assert res is None

@pytest.mark.xfail
def test_converter_incompatible_categories():
    res = __main__.convert(17.0, 'c', 'km')
    assert res is None

@pytest.mark.xfail
def test_converter_length_to_temp():
    res = __main__.convert(167.0, 'mm', 'f')
    assert res is None

@pytest.mark.xfail
def test_converter_wrong_value():
    res = __main__.convert("fdwf", 'c', 'f')
    assert res is None

@pytest.mark.xfail
def test_converter_below_absolute_zero():
    res = __main__.convert(-303.0, 'c', 'k')
    assert res is None