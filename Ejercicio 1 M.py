def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"El valor {valor} se encontró en la posición ({i}, {j})"
    return "El valor no se encontró en la matriz"


# Matriz de ejemplo 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)

valor_a_buscar = 8
print(buscar_valor(matriz, valor_a_buscar))
 
