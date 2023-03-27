"""
Created on Sun Mar 26 2023

@author: Adan Alvarez
"""

import random

# Generar una lista de 10 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]
print("\n\nLista original:", numeros)

# Algoritmo de ordenamiento de burbuja
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

bubble_sort(numeros)
print("Lista ordenada:", numeros)
