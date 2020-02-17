# Examen: I parcial inteligencia artificial
# Objetivo: Sumatoria de numeros primos
# Autor: Camila Sampson
# Fecha: 17/02/2020
# Link del repositorio: https://github.com/SampsonRubio/primer_parcial_IA

# ---------------------------------------------Ejercicio 2----------------------------------------------


def es_primo(n):
    if (n < 2):
        return False
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True


def segundo_ejecicio():
    sum = 0
    for i in range(2, 3000000):
        if es_primo(i):
            sum += i
    print(sum)


segundo_ejecicio()
