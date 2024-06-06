matriz_simple=[
    [1,2,3],
    [4,5,6]
]
#imprimir matriz completa tal cual la vez arriba
print("1) Imprimir matriz")
for elemento in matriz_simple:
    print(elemento)

#imprimir el elemento según la posición en la matriz
print("2) Imprimir un elemento por posición")
print(matriz_simple[1][0])

#imprime todos los elementos en orden
print("3) imprimir todos los elementos")
for fila in matriz_simple:
    for elemento in fila:
        print(elemento, end=" ")
print()

matriz_3D = [
    [
        [1,2,3],
        [4,5,6],
    ],
    [
        [7,8,9],
        [10,11,12],
    ],
    [
        [13,14,15],
        [16,17,18],
    ]
]
for capa in matriz_3D:
    for fila in capa:
        for elemento in fila:
            print(elemento, end=" ")
        print()
    print()
