class Calculadora:
    def add(self, a, b):
        return a + b
    
    from calculadora import Calculadora

def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

# Cambio para probar