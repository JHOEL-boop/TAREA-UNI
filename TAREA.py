def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return i, j  # Retorna la posición en la que se encontró el valor
    return None  # Si no se encuentra, retorna None

# Definición de una matriz 3x3 con valores numéricos
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Valor a buscar
valor_buscado = 50

# Llamada a la función de búsqueda
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar resultados
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición: {posicion}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")

