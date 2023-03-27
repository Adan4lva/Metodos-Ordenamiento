"""
Created on Sun Mar 26 2023

@author: Adan Alvarez
"""

import random

# Generar una lista de 10 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]
print("\n\nLista original:", numeros)

# Algoritmo de ordenamiento rápido
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = [x for x in lista[1:] if x <= pivot]
        mayores = [x for x in lista[1:] if x > pivot]
        return quick_sort(menores) + [pivot] + quick_sort(mayores)

numeros_ordenados = quick_sort(numeros)
print("Lista ordenada:", numeros_ordenados)