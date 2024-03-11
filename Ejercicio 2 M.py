import numpy as np

def ordenar_fila_matriz(matrix, fila):
    matrix[fila] = np.sort(matrix[fila])
    return matrix

# Crear una matriz de ejemplo de 3x3
matriz = np.array([[9, 2, 5], [7, 1, 8], [4, 6, 3]])

# Imprimir la matriz original
print("Matriz original:")
print(matriz)

# Ordenar la segunda fila de la matriz
matriz_ordenada = ordenar_fila_matriz(matriz, 1)

# Imprimir la matriz con la fila ordenada
print("\nMatriz con la segunda fila ordenada:")
print(matriz_ordenada) 
