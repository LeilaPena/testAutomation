#Estructuras de datos (listas, tuplas, diccionarios)

#listas
mi_lista = ['Arg', 200, True]
           #0      1   2
print(mi_lista[0])
mi_lista.append(5000) #agregar un valor
mi_lista.insert(1,"Paises Bajos")
print(mi_lista)

for i in mi_lista:
    print(i)
#tmb esta pop, index

#tuplas: son inmutables. no se pueden modificar (los de las listas si)
mi_tupla =('Celeste', 200, False)
print(mi_tupla[1])

#diccionarios (clave (key), valor)
persona = {
    'nombre' : "Jaime",
    'apellido':  "Desconocido",
    'edad': 34
}

print(persona['apellido'])
print(persona.keys())
print(persona.values())
print(persona.items())

#Funciones

def saludo (nombre):
    print(f"Hola {nombre}")
    return f'Hola {nombre}'

saludo("nati")

def sumar (a,b):
    return a + b

def calculadora_simple(operacion, a,b):
    if operacion == 'sumar':
        return sumar(a,b)
    else:
        return 'Operación no valida'
    
print(calculadora_simple("sumar",1,1))

try: 
    resultado = 10/0
except  ZeroDivisionError as e:
    print(f'error: {e}')

try:
    numero= int('123')
except ValueError as e:
    print(f'Error: {e}')

try:
    print(persona['documento'])
except KeyError as e:
    print("la clave no existe")