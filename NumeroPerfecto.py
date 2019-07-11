def divisores(num):
    return [x for x in range(1,num) if num % x == 0]
"""
def divisores_rec(num,aux):             #Función recursiva
    if aux == num:
        return []
    if num % aux == 0:
        return [aux] + divisores_rec(num,aux+1)
    return divisores_rec(num,aux+1)
#print divisores(10), divisores_rec(6,1)
"""
""" 
def perfecto(num,div):
    sumdif = sum(div)
    if num == sumdif:
        return str(num) + " es un numero perfecto"
    return str(num) + " no es un numero perfecto"
print perfecto(10,divisores(10))
"""
def perfecto1(numero):
    return sum(divisores(numero)) == numero
"""
n = inmput("Ingrese el numero  evaluar: ")
if perfecto1(n):
    print str(n) + " es perfecto"
else:
    print str(n) + " no es perfecto"
"""
n = 1                                   #Genera lista de los primeros 4 números perfectos
lista = []
while len(lista) < 4:
    if perfecto1(n):
        lista.append(n)
        print str(n) + " es perfecto"
        n += 1
    else:
        n += 1
print lista
    

