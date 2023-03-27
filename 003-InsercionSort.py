"""
Created on Sun Mar 26 2023

@author: Adan Alvarez
"""

import random

# Generar una lista de 10 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]
print("\n\nLista original:", numeros)

# Algoritmo de ordenamiento por inserción
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        j = i - 1
        # Insertar el elemento i en la posición correcta en la lista ordenada
        while j >= 0 and lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            j -= 1

insertion_sort(numeros)
print("Lista ordenada:", numeros)
