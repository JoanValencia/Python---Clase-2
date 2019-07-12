"""
Picas y Fijas
5 intentos
fn validación
fn picas
fn fijas
mostrar resultados en matrix [num, picas, fijas]
"""
# Librerías:
from random import randint

# Declaración de variables:
i = 0
intent = 0
listnum = []
lista = []
val = False
tam = 3
pica = 0
fija = 0
arreglo = []


# Funciones:
def solicitud(val):
    while val == False:
        num = raw_input("Ingrese un numero de tres digitos: ")
        listnum = [int(i) for i in list(num)]
        val = validacion(listnum)
    return listnum

def validacion(listnum):
    if len(listnum) == 3:
        return True
    if len(listnum) > 3:       
        print "Ha ingresado mas de tres digitos"
        return False
    if len(listnum) < 3:      
        print "Ha ingresado menos de tres digitos"
        return False

def generar_aleatorios(tam):
    lista = []
    while len(lista) < tam:
        numero = randint(1,9)
        if numero not in lista:
            lista.append(numero)
    return lista

def comparar(list1,list2):
#    print list1, list2
    pica = 0
    fija = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            if list1[i] == list2[i]:
                fija += 1
            else:
                pica += 1
    return pica, fija


    
    
# Ejecución:              
listnum = solicitud(val)
lista = generar_aleatorios(tam)
pica, fija = comparar(listnum,lista)
print "Tienes " + str(pica) + " pica(s) y " + str(fija) + " fija(s)" 
arreglo.append([listnum,pica,fija])

# Pruebas:
print ""
print arreglo
print pica , fija   
print listnum
print lista
val = validacion(listnum)
print val

#https://github.com/apdaza/python_samples/tree/master/picas%20y%20fijas
           
