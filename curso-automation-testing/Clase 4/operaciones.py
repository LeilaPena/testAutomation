def sumar (a,b):
    return a + b

def restar (a,b):
    return a - b

def dividir (a,b):
    if b == 0:
        raise  ValueError('No se puede dividir por 0')
    return a / b

def multiplicar (a,b):
    return a * b

def calculadora_simple(operacion,a,b):
    try:
        a = int(a)
        b = int(b)
        
        if operacion == 'sumar':
            return sumar(a,b)
        elif operacion == 'restar':
            return restar(a,b) 
        elif operacion == 'dividir':
            return dividir(a,b) 
        elif operacion == 'multiplicar':
            return multiplicar(a,b) 
        else:
            return KeyError
    except ZeroDivisionError: 
        return  'Error: no se puede dividir por cero'
    except ValueError:
        return 'Error: los valores deben ser numericos'

print(calculadora_simple('sumar',1,1))
print(calculadora_simple('restar',1,1))
print(calculadora_simple('dividir',1,1))
print(calculadora_simple('multiplicar',1,1))
print(calculadora_simple('dividir',1,0))
print(calculadora_simple('sumar','R',1))
print(calculadora_simple('asdf',1,1))