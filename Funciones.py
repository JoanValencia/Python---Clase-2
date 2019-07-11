from random import randint
"""
lista = []

while len(lista) < 3:           #3 numeros aleatorios usando while
    numero = randint(1,9)
    if numero not in lista:
        lista.append(numero)

print lista
"""


def generar_lista(tam):         #3 numeros aleatorios usando una Función
    lista = []
    
    while len(lista) < tam:
        numero = randint(1,9)
        if numero not in lista:
            lista.append(numero)
    return lista
#print generar_lista(3)

def suma(lista):
    acum = 0
    for i in lista:
        acum +=i
    return acum
#lista = generar_lista(3)
#print lista
#print suma(lista)

def fibo(n):
    if n in [1,2]:
        return 1
    return fibo(n-1) + fibo(n-2)

def suma_rec(lista):            #Función recursiva
    if lista == []:
        return 0
    return lista[0] + suma_rec(lista[1:])


def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

    
lista = generar_lista(8)
print lista
print suma(lista), suma_rec(lista)
print ordenar(lista)
print fibo(5)
print [fibo(x) for x in range(1,11)]
