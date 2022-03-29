import Calculator
import  pytest

@pytest.mark.parametrize("a,b,c",[(3,2,5),(10,12,22),(2,5,7),(7,8,15)])
def test_add(a,b,c):
    result=Calculator.add(a,b)
    assert c==result

@pytest.mark.parametrize("a,b,c",[(3,2,1),(10,8,2)])
def test_sub(a,b,c):
    result=Calculator.sub(a,b)
    assert c==result

@pytest.mark.parametrize("a,b,c",[(3,2,6),(2,5,10)])
def test_mult(a,b,c):
    result=Calculator.mult(a,b)
    assert c==result

@pytest.mark.parametrize("a,b,c",[(4,2,2),(10,5,2)])
def test_div(a,b,c):
    result=Calculator.divide(a,b)
    assert c==result