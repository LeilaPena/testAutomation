#Tipos de variable
varString = 'Soy una cadena de texto'
varInt= 12
varFloat = 12.5 
varBool = True

#Salida de datos
print(varString)

#Ingresar tipo de datosd
datoIngresado= input('Ingresa un dato')
print(datoIngresado)
#El dato que devuelve es siempre un string

#Convertir tipos de dato
datoEnteroIngresado= int(input('Ingresa un numero entero'))
print(type(datoEnteroIngresado))

#Operaciones de matemática
suma = 2 + 3
potencia = 2**2
divison = 10/5 
#para que devuelva sin decimal, se ponen dos //
resto = 4%2
operadorRelacional1 = 5 > 2
operadorRelacional2 = 5 < 2
operadorRelacional3 = 5 != 2
operadorRelacional4 = 5 == 2


#Operadores lógicos
edad = 19
licencia = True
not(edad >= 18 and licencia == True)

#Condicionales
puntuacion = int(input("Ingrese una nota"))

if puntuacion >= 9:
    print("Excelente")
elif puntuacion >= 5:
    print ("Bien")
else:
    print("Desaprobado")

#Bucles
# range(stop)
# range(start, stop)
# range (start, stop, step) 

for i in range (0,11,2):
    print (i)

for i in range(12):
    if i == 4:
        break
    print(i)
#tmb esta continue

i=  1
while i <=5:
    print(i)
    i= i + 1 #i +=1