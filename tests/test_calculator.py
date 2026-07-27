from src import calculator as calc
import pytest



addtest_value=[(5,10,15),(4,5,9),(8,8,16),(-10,-10,-20)]
dividetest_value=[(10,5,2),(20,10,2),(15,3,5)]
@pytest.mark.parametrize("a,b,sum",addtest_value)
def test_add(a,b,sum):
    assert calc.add(a, b) == sum
    
@pytest.mark.APRIL
def test_substract():
    assert calc.substract(5, 4) == 1
    assert calc.substract(10, 5) == 5
@pytest.mark.parametrize("a,b,mul", dividetest_value)
def test_divide(a,b,mul):
    assert calc.divide(a, b) == mul
    with pytest.raises(ValueError):
        calc.divide(a, 0)

def test_multbly():
    assert calc.multibly(5, 6) == 3    
    assert calc.multibly(6, 6) == 36
    assert calc.multibly(5, 5) == 25