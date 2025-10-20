import pytest
import operaciones

#def test_sumar():
#   assert operaciones.sumar(2,4) == 6


#raises devuelve expresiones de errores, sirve para testear expresiones
def  test_division_por_cero():
    with  pytest.raises(ValueError):
        operaciones.dividir(10,0)

#decoradores

#oarametrize, pasa  primero un string y dsp una lista. Los string son los dos valores y luego el resultado esperado
@pytest.mark.parametrize("a,b,resultadoEsperado", [
    (2,5,7), #numeros positivos
    (-4,-2,-6) #numeros negativos
])
def test_sumar_varios(a,b,resultadoEsperado):
    assert operaciones.sumar(a,b) == resultadoEsperado

def  test_restar_con_fixture(numeros):
    a,b = numeros
    assert operaciones.restar(a,b) ==  0

def test_sumar_con_fixture(numeros):
    a,b=numeros
    assert operaciones.sumar(a,b) == 10

#decoradores/markers personalizados. Sirve  para  solo ejecutar un test en especifico
# @pytest.mark.listo
# def test_sumar_listo():
#     assert operaciones.sumar(1,3) == 4


def test_estructura_dicc():
    data = {"nombre":"Luisa", "edad":34}
    #chequea si estos valores estan en el diccionario
    assert "nombre" in data
    assert "edad" in data
    #chequea que el tipo de dato sea el pedido
    assert isinstance(data["nombre"], str)
    assert isinstance(data["edad"], int)

def test_estructura_list():
    items = [{"id":1, "id":2}]

    assert all('id' in item for item in items)