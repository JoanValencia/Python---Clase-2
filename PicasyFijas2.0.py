"""
Picas y Fijas
5 intentos
fn validación
fn picas
fn fijas
mostrar resultados en matrix [num, picas, fijas]
"""
from random import randint

i = 0
listnum = []
val = False
tam = 3

def generar_aleatorios(tam):
    lista = []
    while len(lista) < tam:
        numero = randint(1,9)
        if numero not in lista:
            lista.append(numero)
    return lista

def solicitud(val):
    if val == False:
        num = raw_input("Ingrese un numero de tres digitos: ")
        listnum = [int(i) for i in list(num)]
    return listnum

def validacion(listnum):
    if len(listnum) == 3:
        val = True
    elif len(listnum) > 3:
        val = False
        print "Ha ingresado mas de tres digitos"
        solicitud(val)
    else:
        val = False
        print "Ha ingresado menos de tres digitos"
        solicitud(val)
    return val

#def comparacion(gen,usr):
#    for i in lista 

listnum = solicitud(val)
print listnum
print generar_aleatorios(tam)
print validacion(listnum)
#print picas(lista,listnum)

"""
def comparar(list1,list2):
    pica = 0
    fija = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            if list1[i] == list2[i]:
                fija += 1
            else:
                pica += 1
"""             
