# Examen: I parcial inteligencia artificial
# Objetivo: Numeros amigos
# Autor: Camila Sampson
# Fecha: 17/02/2020
# Link del repositorio: https://github.com/SampsonRubio/primer_parcial_IA

# ---------------------------------------------Ejercicio 1----------------------------------------------


def numeros_amigos(x, y):
    sumx = 0
    sumy = 0
    i = 0
    j = 0
    for i in range(1, x):
        if(x % i == 0):
            sumx += i
    for j in range(1, y):
        if(y % j == 0):
            sumy += j
    if(x == sumy and y == sumx):
        print(str(x) + ' , ' + str(y))
        return True
    else:
        return False


def primer_ejercicio():
    sumatoria = 0
    i = 0
    j = 0
    for i in range(219, 10000):
        for j in range(219, 10000):
            if ((i != j) and (numeros_amigos(i, j) == True)):
                sumatoria = sumatoria + i + j


primer_ejercicio()
