"""
Created on Sun Mar 26 2023

@author: Adan Alvarez
"""

import random

# Generar una lista de 10 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]
print("\n\nLista original:", numeros)

# Algoritmo de ordenamiento por selección
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Encontrar el elemento mínimo en la lista no ordenada
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambiar el elemento mínimo con el primer elemento de la lista no ordenada
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

selection_sort(numeros)
print("Lista ordenada:", numeros)